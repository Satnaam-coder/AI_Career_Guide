
import pandas as pd

# Load dataset
df = pd.read_csv("data/careers.csv")

def get_career_recommendation(stream, interest):
    results = []

    for index, row in df.iterrows():
        score = 0

        # Stream match
        if stream.lower() in str(row["stream"]).lower():
            score += 2

        # Skills match
        if interest.lower() in str(row["skills"]).lower():
            score += 3

        results.append((row["career"], score, row["description"]))

    # Sort by score
    results = sorted(results, key=lambda x: x[1], reverse=True)

    # Handle no result case
    if not results or all(item[1] == 0 for item in results):
     return [("No Match Found", 0, "Try different interest")]

    return results[:5]