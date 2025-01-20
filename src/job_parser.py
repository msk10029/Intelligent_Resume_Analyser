# job_parser.py - Module for parsing job descriptions

import re


def parse_job_description(job_description):
    
    keywords = []

    try:
        lines = job_description.split("\n")

        for line in lines:
            
            match = re.findall(r"\b[A-Za-z]+(?:\s[A-Za-z]+)?\b", line)             # Use regex to capture key phrases
            if match:
                keywords.extend(match)
        keywords = list(set(keywords))    # Remove duplicates and clean up the keyword list

    except Exception as e:
        print(f"Error parsing job description: {e}")
        return {}

    return {
        "skills": keywords
    }

# Example usage
if __name__ == "__main__":
    job_desc = """
    We are looking for a Software Engineer with expertise in:
    - Python programming
    - Machine Learning frameworks
    - NLP and data analysis
    
    Additional skills include:
    - Communication
    - Teamwork
    """

    parsed_data = parse_job_description(job_desc)
    print("Parsed Job Description:")
    print(parsed_data)
