from extractor.skill_extractor import extract_skills
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
    resume_skills=extract_skills(turning_resume_into_text(resume_file),20)
    jd_skills=turning_jd_into_text(turning_jd_into_text(job_file),20)

    result = comapre_skills(resume_skills,jd_skills)
    st.subheader("Matched Skills")
    st.write(result["matched_skills"])

    st.subheader("Missing Skills")
    st.write(result["missing_skills"])

