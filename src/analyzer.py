# analyzer.py - Module for analyzing resumes against job descriptions using OpenAI

from openai import OpenAI
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_keywords(text):
    
    doc = nlp(text)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return keywords

def extract_skills_with_openai(job_description,client):
    
    prompt = f"""
    Extract a list of skills from the following job description:
    {job_description}
    Provide the skills as a comma-separated list.
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant that extracts skills from job descriptions."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    #skills_text = response.choices[0].message["content"].strip()
    skills_text = response.choices[0].message.content.strip()
    # print("Skills extracted")
    # print(skills_text)
    
    skills = skills_text.split(",")
    skills = [skill.strip() for skill in skills if skill.strip()]
    return skills

def match_skills_with_openai(resume_text, job_skills,client):
    
    prompt = f"""
    Match the following skills from the resume with the required job skills:
    Resume Skills: {resume_text}
    Job Skills: {', '.join(job_skills)}
    Provide the matched skills strictly as a list and the unmatched skills strictly as another list.
    Example: 
    Matched Skills: ['Java Programming', 'Neural Network', 'NLP and Data Analysis', 'Communication']
    Unmatched Skills: ['Teamwork']
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant that matches skills from resumes with job descriptions."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    skills_text = response.choices[0].message.content.strip()
    # print("Match and Unmatch")
    # print(skills_text)
    matched_skills = []
    missing_skills = []
    for line in skills_text.split("\n"):
        if "Matched Skills:" in line:
            matched_skills = [skill.strip() for skill in line.replace("Matched Skills:", "").split(",") if skill.strip()]
        elif "Unmatched Skills:" in line:
            missing_skills = [skill.strip() for skill in line.replace("Unmatched Skills:", "").split(",") if skill.strip()]

    return matched_skills, missing_skills

def analyze_resume_with_job(resume_text, job_description, openai_key):
    
    client = OpenAI(api_key=openai_key)
    job_skills = extract_skills_with_openai(job_description,client)
    matched_skills, missing_skills = match_skills_with_openai(resume_text, job_skills,client)
    match_percentage = round((len(matched_skills) / len(job_skills)) * 100, 2) if job_skills else 0

    results = {
        "match_percentage": match_percentage,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }

    return results


if __name__ == "__main__":
    resume_text = "Python Machine Learning Communication NLP Data Analysis"
    job_description = """
    We are looking for a Software Engineer with expertise in:
    - Python programming
    - Machine Learning frameworks
    - NLP and data analysis
    
    Additional skills include:
    - Communication
    - Teamwork
    """

    analysis_results = analyze_resume_with_job(resume_text, job_description)
    print("Analysis Results:")
    print(analysis_results)
