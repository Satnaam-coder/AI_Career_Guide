import pandas as pd

# Load datasets
careers_df = pd.read_csv("data/careers.csv")
courses_df = pd.read_csv("data/courses.csv")


def generate_roadmap(career_name):
    roadmap = {}

    # Find career
    career_row = careers_df[careers_df["career"].str.lower().str.contains(career_name.lower())]

    if career_row.empty:
        return {"error": "Career not found"}

    # Get skills
    skills = career_row.iloc[0]["skills"].split("|")

    roadmap["career"] = career_name
    roadmap["skills"] = skills

    # Match courses
    recommended_courses = []

    for skill in skills:
        matched = courses_df[courses_df["skill"].str.contains(skill, case=False, na=False)]
        
        for _, row in matched.iterrows():
            recommended_courses.append({
                "course": row["course"],
                "platform": row["platform"],
                "level": row["level"]
            })

    roadmap["courses"] = recommended_courses

    return roadmap

    if not career_name:
        return {"error": "Please enter career name"}
