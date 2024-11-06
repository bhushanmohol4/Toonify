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