import requests
from PIL import Image
from io import BytesIO
import json
import time
from groq import Groq
from abc import ABC, abstractmethod
from Helpers.JsonHelper import get_value_from_json

def call_flux_api(prompt, genre, characters, style, panels_per_page):
    """
    Make API call to the FLUX model.
    """
    try:
        payload = {
            "prompt": prompt,
            "genre": genre,
            "characters": json.dumps(characters) if characters else "auto",
            "style": style,
            "steps"
            "panels_per_page": panels_per_page
        }
        
        GRADIO_API_URL = "http://172.25.115.66:42420/"
        
        response = requests.post(GRADIO_API_URL, json=payload)
        
        if response.status_code == 200:
            image_bytes = response.content
            return Image.open(BytesIO(image_bytes)), None
        else:
            return None, f"API Error: Status code {response.status_code}"
            
    except Exception as e:
        return None, f"Error calling API: {str(e)}"
    
# Abstract base class for LLM API calls
class LLMProvider(ABC):
    @abstractmethod
    def generate_story(self, prompt, genre, characters):
        pass
    def generate_character_desc(self, story):
        pass
    def generate_story(self, prompt, genre, characters):
        pass

class OpenAIProvider(LLMProvider):
    def __init__(self):
        self.api_key = get_value_from_json("config", "OpenAI_bearer")
        self.endpoint = get_value_from_json("config", "OpenAI_endpoint")
        self.max_retries = get_value_from_json("config", "Max_retries")
        
    def generate_story(self, prompt, genre, characters):
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # Construct the prompt
            system_prompt = get_value_from_json("prompts", "story_generation_system")
            
            character_desc = json.dumps(characters) if characters else "Generate appropriate characters"
            
            llm_prompt = f"""
            {get_value_from_json("prompts", "story_generation_user")}
            Story Prompt: {prompt}
            Genre: {genre}
            Characters: {character_desc}
            """

            for attempt in range(self.max_retries):
                response = requests.post(
                    self.endpoint,
                    headers=headers,
                    json={
                        "model": "gpt-3.5-turbo",
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": llm_prompt}
                        ]
                    }
                )
            
            
                if response.status_code == 200:
                    return response.json(), None
                elif response.status_code == 429:
                    print("Rate limit hit. Retrying...")
                    time.sleep(5)
                else:
                    return None, f"LLM API Error: {response.status_code}"
                
        except Exception as e:
            return None, f"Error generating story: {str(e)}"
    
    def generate_character_desc(self, story):
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # Construct the prompt
            system_prompt = get_value_from_json("prompts", "character_gen_system")
            
            llm_prompt = f"""
            {get_value_from_json("prompts", "character_gen_user")}
            Story: {story}
            """
            
            response = requests.post(
                self.endpoint,
                headers=headers,
                json={
                    "model": "gpt-4o",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": llm_prompt}
                    ]
                }
            )
            
            if response.status_code == 200:
                return response.json(), None
            else:
                return None, f"LLM API Error: {response.status_code}"
                
        except Exception as e:
            return None, f"Error generating story: {str(e)}"

    def generate_manga_panels(self, story, character_desc):
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # Construct the prompt
            system_prompt = get_value_from_json("prompts", "panel_breakdown_system")
            
            llm_prompt = f"""
            {get_value_from_json("prompts", "panel_breakdown_user")}
            Story: {story}
            character descriptions: {character_desc}
            """
            
            response = requests.post(
                self.endpoint,
                headers=headers,
                json={
                    "model": "gpt-4o",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": llm_prompt}
                    ]
                }
            )
            
            if response.status_code == 200:
                return response.json(), None
            else:
                return None, f"LLM API Error: {response.status_code}"
                
        except Exception as e:
            return None, f"Error generating story: {str(e)}"
        
    class GroqProvider(LLMProvider):
        def __init__(self):
            self.api_key = get_value_from_json("config", "Groq_bearer")
            self.max_retries = get_value_from_json("config", "Max_retries")

            
        def generate_story(self, prompt, genre, characters):
            try:
                client = Groq(
                    api_key = self.api_key,
                )
                character_desc = json.dumps(characters) if characters else "Generate appropriate characters"

                llm_prompt = f"""
                {get_value_from_json("prompts", "story_generation_system")}
                {get_value_from_json("prompts", "story_generation_user")}
                Story Prompt: {prompt}
                Genre: {genre}
                Characters: {character_desc}
                """
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"{llm_prompt}",
                        }
                    ],
                    model="llama3-8b-8192",
                )
                
                story = chat_completion.choices[0].message.content
                return story

            except Exception as e:
                return None, f"Error generating story: {str(e)}"
        
        def generate_character_desc(self, story):
            try:
                client = Groq(
                    api_key = self.api_key,
                )

                llm_prompt = f"""
                {get_value_from_json("prompts", "character_gen_system")}
                {get_value_from_json("prompts", "character_gen_user")}
                Story: {story}
                """

                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"{llm_prompt}",
                        }
                    ],
                    model="llama3-8b-8192",
                )
                
                character_desc = chat_completion.choices[0].message.content
                return character_desc
            
            except Exception as e:
                return None, f"Error generating story: {str(e)}"

        def generate_manga_panels(self, story, character_desc):
            try:
                client = Groq(
                    api_key = self.api_key,
                )

                llm_prompt = f"""
                {get_value_from_json("prompts", "panel_breakdown_system")}
                {get_value_from_json("prompts", "panel_breakdown_user")}
                Story: {story}
                character descriptions: {character_desc}
                """

                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"{llm_prompt}",
                        }
                    ],
                    model="llama3-8b-8192",
                )
                
                character_desc = chat_completion.choices[0].message.content
                return character_desc
                    
            except Exception as e:
                return None, f"Error generating story: {str(e)}"