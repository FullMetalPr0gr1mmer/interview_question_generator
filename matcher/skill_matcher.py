from jinja2.utils import missing


def comapre_skills(resume_skills,jd_skills):
    resume_skills_set=set([sk.lower() for sk in resume_skills])
    jd_skills_set=set([sk.lower() for sk in jd_skills])
    #returing array of unique skills from both resume and JD

    matching = resume_skills_set & jd_skills_set
    missing = resume_skills_set - jd_skills_set
    # seeks intersection between 2 sets to see matching skills and substration to find  missing one

    return {
        "matched_skills": sorted(matching),
        "missing_skills": sorted(missing)
    }