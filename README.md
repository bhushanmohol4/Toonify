# AI MangaGen: Automated Manga Creation Pipeline

AI MangaGen is a groundbreaking system designed to automate the manga creation process. By integrating user input with advanced AI techniques, it enables the seamless generation of visually consistent, narratively rich manga chapters. Whether you're creating a new manga from scratch or continuing an existing project, AI MangaGen provides a complete solution for story development, character creation, and visual production.

---

## 🚀 *Features*
- *User-Friendly Pipeline*: Minimal input required, with optional customization for enhanced creativity.
- *Storyline Automation*: Generate structured storylines tailored to your chosen genre.
- *Character Continuity*: Ensure consistent character traits across chapters with Chroma DB storage.
- *Dynamic Visuals*: High-quality pose sheets for characters, aligned with the narrative context.
- *Advanced AI Training*: Leverages Low-Rank Adaptations (LoRAs) for stylistically consistent visuals.
- *Monochrome Manga Generation*: Produce polished, black-and-white manga panels in a traditional style.

---

## 📖 *High-Level Architecture*

The AI MangaGen pipeline comprises four main modules:

### *1. User Input*
Users provide:
- *Story Idea*: A brief description of the story they want to create.
- *Genre*: The style or type of manga (e.g., action, romance, fantasy).
- *Character Descriptions (Optional)*: Specific character traits or ideas.

*Flexibility*:
- If continuing an existing project, users can provide the name of their manga.
- If no character details are provided, the system generates them automatically.

---

### *2. Skeleton Generation*
The foundation of the pipeline:
- *Storyline Creation*: Generates a coherent narrative with distinct acts and plot progression based on the user's input.
- *Character Descriptions*: Produces detailed character profiles aligned with the story context.
- *Chroma DB*: Stores character data for use in future chapters, ensuring continuity.

---

### *3. Character Generation*
Transforms text descriptions into visual character representations:
- *Pose Sheets*: High-quality, dynamic pose sheets for all characters, showcasing various actions and emotions.
- These visuals serve as the basis for consistent character depictions across panels and chapters.

---

### *4. Flux Training*
Enhances visual quality and consistency:
- *LoRAs Training*: Trains Low-Rank Adaptations (LoRAs) using generated pose sheets.
- This ensures characters and scenes remain stylistically coherent throughout the manga.

---

### *5. Manga Generation*
Creates the final manga chapter:
- *Textual Panels*: Detailed descriptions of each panel, covering scenes, interactions, and settings.
- *Visual Rendering*: Textual panels are processed through a Flux Monochrome Model to generate polished, black-and-white manga illustrations.

---

## 🔮 *Future Enhancements*
- *Color Manga Support*: Expand capabilities to produce colored manga panels.
- *Dialogue Generation*: AI-driven speech bubble creation for richer storytelling.
- *Genre Expansion*: Support additional manga genres and artistic styles.
- *Interactive Editing*: Allow users to manually adjust character designs and panel layouts.

---

## 📦 *Installation*

To get started with AI MangaGen, follow these steps:

1. Clone this repository:
   ```bash
   https://github.com/bhushanmohol4/Toonify.git
## 📧 *Contact*
For inquiries, feedback, or collaboration opportunities, feel free to reach out:

- *Email*: shekharsomani101@gmail.com, rbrishabh76@gmail.com, bhushanmohol4@gmail.com
   
