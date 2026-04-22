import pandas as pd

skills_df = pd.read_csv("data/skills.csv")
SKILLS_DB = skills_df["skill"].tolist()

def extract_skills(resume_text):
    """
    This function checks which skills from our skill list
    are present in the resume text.
    """
    resume_text = resume_text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in resume_text:
            found_skills.append(skill)

    return list(set(found_skills))


def calculate_resume_score(found_skills, resume_text):
    """
    Resume score is calculated using simple and logical rules,
    similar to how a human would judge a resume.
    """

    score = 0

    # Skill contribution (max 60)
    skill_score = min(len(found_skills) * 5, 60)
    score += skill_score

    # Experience keywords (max 20)
    experience_keywords = ["internship", "experience", "project", "worked"]
    for word in experience_keywords:
        if word in resume_text.lower():
            score += 5

    # Education presence (max 10)
    education_keywords = ["b.sc", "mca", "b.tech", "degree"]
    for edu in education_keywords:
        if edu in resume_text.lower():
            score += 5
            break

    # Resume length check (max 10)
    if len(resume_text.split()) > 300:
        score += 10

    return min(score, 100)