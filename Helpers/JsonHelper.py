import json

def getDataFromJSON(input):
    manga_name = list(input.keys())[0]
    print(f"Manga Name: {manga_name}")

    manga_data = input[manga_name]
    story = manga_data["story"]
    character_def = manga_data["characters"]

    # Create a hierarchical structure
    hierarchical_data = {
        manga_name: {
            "story": story,
            "characters": {}
        }
    }

    # Add characters to the hierarchical structure
    for character, description in character_def.items():
        print(f"Processing character: {character}")
        hierarchical_data[manga_name]["characters"][character] = description

    return hierarchical_data

def clean_llm_json(text):
    """
    Extracts JSON content from the LLM response and returns a formatted JSON string.
    """
    try:
        # Find the start and end positions of the JSON object
        start = text.find("{")
        end = text.rfind("}") + 1

        # Extract the JSON string
        json_str = text[start:end]

        # Parse the JSON string
        parsed_json = json.loads(json_str)

        # Return formatted JSON string with indentation
        return json.dumps(parsed_json, indent=2)
    except (json.JSONDecodeError, ValueError) as e:
        return f"Error parsing JSON: {str(e)}"

def get_value_from_json(file_name, key_path):
    """
    Retrieve value from JSON data given a key path.
    """
    with open(f"{file_name}.json", "r") as file:
        data = json.load(file)

    keys = key_path.split(".")
    current_data = data

    for key in keys:
        current_data = current_data.get(key)
        if current_data is None:
            return None
    
    return current_data