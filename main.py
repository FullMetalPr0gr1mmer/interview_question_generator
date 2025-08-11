from extractor.skill_extractor import *
import streamlit as st
import pdfplumber
import io
from matcher.skill_matcher import comapre_skills

"extract resumes into a single string"
def turning_resume_into_text(resume_file):
    txt=""
    if resume_file:
        with pdfplumber.open(io.BytesIO(resume_file.read())) as pdf:
            for page in pdf.pages:
                txt += page.extract_text() or ""
    return txt
def turning_jd_into_text(job_file):
    txt=""
    if job_file:
        txt = job_file.read().decode("utf-8")
    return txt


st.subheader("Upload Resume")
resume_file  = st.file_uploader("Upload your resumes (.PDF)",type=["pdf"])

st.subheader("Job Descriptions")
job_file = st.file_uploader("Upload job decriptions (.TXT)",type=["txt"])

st.title("Interview Skill Analyzer")

if st.button("Analyze"):
    resume_skills=extract_skills_semantic(turning_resume_into_text(resume_file))
    jd_skills=extract_skills_semantic(turning_jd_into_text(job_file))
    print("///////////////////////////////////////////////////////////////////////////////////////")
    print(resume_skills)
    print(jd_skills)

    result = comapre_skills(resume_skills,jd_skills)
    st.subheader("Matched Skills")
    st.write(result["matched_skills"])

    st.subheader("Missing Skills")
    st.write(result["missing_skills"])

'''print(turning_resume_into_text(resume_file))
print(turning_jd_into_text(job_file))'''