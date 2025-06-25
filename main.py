from extractor.skill_extractor import extract_skills

sample_resume = """
Experienced software engineer with expertise in Python, machine learning, and backend development.
Worked with TensorFlow, Flask, and AWS. Built scalable APIs and NLP tools.
"""

print(extract_skills(sample_resume))