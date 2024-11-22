import streamlit as st

import streamlit as st
import json


def setup_page():
    """Setup home page configuration."""
    st.set_page_config(page_title="Manga Generator", layout="wide")
    st.title("🎨 Toonify")
    st.markdown("Create your own manga by providing a prompt and selecting preferences!")

def render_story_section():
    """Render the story input section with prompt and genre selection."""
    col1, col2 = st.columns(2)
    
    with col1:
        prompt = st.text_area(
            "Enter a story prompt",
            placeholder="Example: A story about a young programmer who discovers they can communicate with computers through dreams...",
            height=100
        )
        
    with col2:
        genres = [
            "Action", "Adventure", "Comedy", "Drama", "Fantasy",
            "Horror", "Mystery", "Romance", "Sci-Fi", "Slice of Life"
        ]
        genre = st.selectbox("Select manga genre", genres)
    
    return prompt, genre

def render_character_section():
    """Render the character creation section."""
    st.subheader("Character Creation")
    
    character_creation_method_list = [
            "Define custom characters", "Use default characters", "Generate random characters"
        ]
    character_creation_method = st.selectbox("Select character creation method", character_creation_method_list, index = None)

    characters = None
    
    if character_creation_method == "Define custom characters":
        characters = []
        num_characters = st.number_input(
            "Number of characters", 
            min_value = 1, 
            max_value = 5, 
            value = 1
        )
        
        for i in range(int(num_characters)):
            st.markdown(f"#### Character {i+1}")
            char_name = st.text_input(f"Name", key=f"name_{i}")
            char_role = st.selectbox(
                "Role",
                ["Protagonist", "Antagonist", "Supporting Character"],
                key=f"role_{i}"
            )
            char_desc = st.text_input(
                "Brief description",
                placeholder="Character's appearance and personality...",
                key=f"desc_{i}"
            )
            
            if char_name and char_role and char_desc:
                characters.append({
                    "name": char_name,
                    "role": char_role,
                    "description": char_desc
                })

    elif character_creation_method == "Use default characters":
        characters = []
        num_characters = st.number_input(
            "Number of characters", 
            min_value = 1, 
            max_value = 5, 
            value = 1
        )
        
        for i in range(int(num_characters)):
            st.markdown(f"#### Character {i+1}")
            default_character_names = ["zombie1", "Luffy"]
            char_name = st.selectbox("Name", default_character_names)
            char_role = st.selectbox(
                "Role",
                ["Protagonist", "Antagonist", "Supporting Character"],
                key = f"role_{i}"
            )
            
            if char_name and char_role and char_desc:
                characters.append({
                    "name": char_name,
                    "role": char_role
                })
    
    return characters, character_creation_method

def render_advanced_settings():
    """Render the advanced settings section."""
    st.markdown("---")
    with st.expander("Advanced Settings"):
        style = st.select_slider(
            "Art Style",
            options=["Simple", "Standard", "Detailed"],
            value="Standard"
        )
        panels_per_page = st.slider(
            "Panels per page",
            min_value=2,
            max_value=8,
            value=4
        )
    
    return style, panels_per_page

def render_results(prompt, genre, characters, style, panels_per_page):
    """Render the generation results."""
    display_col1, display_col2 = st.columns([2, 1])
    
    with display_col1:
        st.markdown("### Generated Manga")
        # Replace this placeholder with actual manga display
        st.markdown("*Preview would appear here*")
    
    with display_col2:
        st.markdown("### Generation Details")
        st.write(f"**Prompt:** {prompt}")
        st.write(f"**Genre:** {genre}")
        st.write(f"**Style:** {style}")
        st.write(f"**Panels per page:** {panels_per_page}")
        st.write("**Characters:**")
        characters_str = json.dumps(characters, indent=2) if characters else "Using auto-generated characters"
        st.code(characters_str)