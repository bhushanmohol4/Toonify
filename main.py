import streamlit as st
from UI import *

def main():
    # Setup page
    setup_page()
    
    # Render UI - User inputs
    prompt, genre = render_story_section()
    characters, use_custom_characters = render_character_section()
    style, panels_per_page = render_advanced_settings()
    
    # Generate button
    if st.button("Generate Manga", type="primary"):
        if not prompt:
            st.error("Please enter a story prompt!")
            return
            
        with st.spinner("Generating your manga..."):
            
            # Show success message
            st.success("Manga generated successfully!")
            
            # Display results
            # render_results(prompt, genre, characters, style, panels_per_page)

if __name__ == "__main__":
    main()