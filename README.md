# Intelligent Resume Analyzer

## Description
The **Intelligent Resume Analyzer** is an AI-powered tool that compares resumes with job descriptions to evaluate compatibility. It extracts skills, calculates a match percentage, and highlights matched and unmatched skills, providing valuable insights for job seekers and recruiters.

## Features
- **Resume Parsing:** Extracts text from uploaded resumes (PDF format).
- **Job Description Analysis:** Extracts key skills and requirements from job descriptions.
- **Skill Matching:** Identifies matched and unmatched skills between the resume and job description.
- **Match Percentage:** Provides an overall compatibility score.
- **Interactive Interface:** Built with Streamlit for easy user interaction.

## Technology Stack
- **Python**: Core programming language.
- **Streamlit**: Web interface for user interaction.
- **OpenAI GPT-4**: Extracts and matches skills with advanced natural language processing.
- **spaCy**: Extracts keywords and entities for preprocessing.
- **pdfplumber**: Parses text from PDF resumes.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/msk10029/Intelligent_Resume_Analyser.git
   cd Intelligent_Resume_Analyser
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   streamlit run intelligent_resume_analyzer.py
   ```

2. Open the app in your browser (default: `http://localhost:8501`).
3. In order to run the application, you need your own OpenAI key.
4. Upload your resume (PDF format) and paste the job description.
5. Click **Analyze Resume**.
6. View the match percentage, matched skills, and unmatched skills.

## Example Output
- **Match Percentage:** 85%
- **Matched Skills:** Python, Machine Learning, Communication
- **Unmatched Skills:** Teamwork, Project Management

## Future Enhancements
- Add recommendations for improving resumes based on unmatched skills.
- Support additional file formats (e.g., DOCX).
- Deploy the application online for public access.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
