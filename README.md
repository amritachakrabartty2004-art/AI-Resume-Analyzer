# AI Resume Analyzer 🚀

An AI-powered web application that analyzes PDF resumes, extracts key technical skills, and provides an optimization score with strategic recommendations.

## Features ✨
- **PDF Extraction**: Seamlessly extracts text from PDF resumes using `PyPDF2`.
- **Skill Categorization**: Automatically detects and groups skills into Programming Languages, Frameworks, Databases, Data Science, and Cloud/DevOps.
- **Optimization Score**: Get a score out of 100 based on industry-standard keywords.
- **Smart Recommendations**: Receive personalized tips to improve your resume's impact.
- **Premium UI**: Modern dark theme with glassmorphism, responsive design, and smooth animations.

## Tech Stack 🛠️
- **Backend**: Python, Flask
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism), JavaScript
- **Libraries**: PyPDF2, Font Awesome, Google Fonts

## Getting Started 🏁

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000` in your browser.

## Project Structure 📂
- `app.py`: Main Flask application logic.
- `templates/`: HTML templates.
- `static/`: CSS, JS, and image assets.
- `uploads/`: Temporary storage for uploaded resumes.
