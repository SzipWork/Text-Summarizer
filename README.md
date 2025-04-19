# Text Summarizer

This is a Streamlit web application that summarizes user-provided text using Google's Gemini 1.5 Pro model via LangChain. The app allows customization of the explanation style and the summary length, making it suitable for a variety of users—from beginners to technical professionals.

---

## Features

- **Text Input**: Accepts any user-entered text for summarization.
- **Explanation Style Options**:
  - Beginner-Friendly
  - Technical
  - Code-Oriented
  - Mathematical
- **Summary Length Options**:
  - Short (1–2 paragraphs)
  - Medium (3–5 paragraphs)
  - Long (detailed explanation)
- **Model Integration**: Utilizes the Gemini 1.5 Pro model through LangChain for high-quality, customizable summarizations.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables
```
GOOGLE_API_KEY=your_google_gemini_api_key
```

### 4. Prepare the Prompt Template
Ensure that template.json is present in the root directory. This file defines the prompt template used by LangChain to structure input for the language model.

### Usage
```bash
streamlit run txt_sum.py
```

### File Structure
```bash
txt_sum.py          # Main Streamlit application
template.json       # Prompt template for LangChain
.env                # Environment variables (excluded from version control)
requirements.txt    # List of required Python packages
```
### Notes

- The application uses LangChain's load_prompt function to load prompt structure from template.json.
- chain.invoke() handles inference with the Gemini 1.5 Pro model.
- Streamlit is used for creating an interactive and accessible frontend.
- Modify template.json to suit specific output needs or domains.

### Contributing
Feel free to submit issues or pull requests to enhance this project.



