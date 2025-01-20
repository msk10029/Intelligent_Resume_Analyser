# Intelligent Resume Analyzer - Start of the project

# This will be the main entry point for modular development

# Import necessary libraries for the Streamlit app and data analysis
import streamlit as st
from resume_parser import extract_text_from_pdf
from job_parser import parse_job_description
from analyzer import analyze_resume_with_job


# Main function to initialize the Streamlit app
def main():
    st.title("Intelligent Resume Analyzer")

    # Step 1: Input OpenAI API Key
    openai_key = st.text_input("Enter your OpenAI API Key", type="password")
    if openai_key:
        st.success("OpenAI API Key received.")
    else:
        st.warning("Please enter your OpenAI API Key to proceed.")
        return

    # Step 2: Upload Resume
    uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])
    if uploaded_file:
        resume_text = extract_text_from_pdf(uploaded_file)
        st.text_area("Extracted Resume Text", resume_text, height=200)
    else:
        resume_text = None

    # Step 3: Input Job Description
    job_description = st.text_area("Paste the Job Description", height=200)

    # Step 4: Analyze Resume
    if st.button("Analyze Resume"):
        if resume_text and job_description:
            # Pass OpenAI key to the analyzer module
            analysis = analyze_resume_with_job(resume_text, job_description, openai_key=openai_key)
            st.subheader("Analysis Results")
            st.write(analysis)
        else:
            st.warning("Please upload a resume and enter a job description.")

if __name__ == "__main__":
    main()
