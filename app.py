from core.career_engine import get_career_recommendation
from core.roadmap_generator import generate_roadmap
from core.chat_engine import chatbot_response

import streamlit as st
from database.db_manager import create_tables
from core.resume_parser import extract_text_from_resume

create_tables()

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "user" not in st.session_state:
    st.session_state.user = None

st.sidebar.title("🔐 Login System")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

from database.db_manager import register_user, login_user

if st.sidebar.button("Register"):
    register_user(username, password)
    st.sidebar.success("Registered!")

if st.sidebar.button("Login"):
    if login_user(username, password):
        st.session_state.user = username
        st.sidebar.success("Login successful")
    else:
        st.sidebar.error("Invalid credentials")

if not st.session_state.user:
    st.warning("Please login first")
    st.stop()

st.set_page_config(page_title="AI Career Guide", layout="wide")
load_css()
create_tables()

st.markdown("<h1>🤖 AI Career Guide</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='badge'>AI Powered Resume & Career Assistant</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📄 Upload Your Resume")
    uploaded_file = st.file_uploader(
        "PDF or DOCX format",
        type=["pdf", "docx"]
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("ℹ️ How It Works")
    st.write("""
    1️⃣ Upload your resume  
    2️⃣ Get AI-based resume score  
    3️⃣ See job market & salary insights  
    4️⃣ Get personalized career roadmap  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

if uploaded_file:
    with st.spinner("Analyzing resume..."):
        resume_text = extract_text_from_resume(uploaded_file)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🔍 Extracted Resume Content")
    st.text_area("Resume Text", resume_text, height=280)
    st.markdown("</div>", unsafe_allow_html=True)

from core.resume_analysis import extract_skills, calculate_resume_score
from database.db_manager import save_resume_analysis

if uploaded_file:
    with st.spinner("Analyzing resume..."):
      resume_text = extract_text_from_resume(uploaded_file)

    skills = extract_skills(resume_text)
    score = calculate_resume_score(skills, resume_text)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 Resume Analysis Result")

    st.write("**Detected Skills:**")
    if skills:
        for skill in skills:
            st.markdown(f"- {skill.capitalize()}")
    else:
        st.write("No major skills detected")

    st.write("**Resume Score:**")
    st.progress(score / 100)
    st.markdown(f"<h3>{score} / 100</h3>", unsafe_allow_html=True)


    from database.db_manager import save_resume_analysis

    # Temporary placeholders (next step me smart banenge)
    suggested_career = "Data Analyst"
    salary_range = "₹4 – 8 LPA"
    
    save_resume_analysis( score, suggested_career, salary_range)

    st.success("Resume analysis saved successfully!")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("## 🎯 Career Recommendation System")

stream = st.selectbox("Select Your Stream", ["Science", "Commerce", "Arts"])
interest = st.text_input("Enter Your Interest (e.g., Python, Finance, Design)")

if st.button("Get Career Suggestions"):
    results = get_career_recommendation(stream, interest)

    if not results:
        st.error("No career found")
    else:
        for career, score, desc in results:
            st.write(f"### {career}")
            st.write(f"Match Score: {score}")
            st.write(f"About: {desc}")
            st.markdown("---")
        
st.markdown("## 🗺️ Career Roadmap Generator")

career_input = st.text_input("Enter Career Name (e.g., Data Scientist)")

if st.button("Generate Roadmap"):
    data = generate_roadmap(career_input)

    if not data or "error" in data:
        st.error(data["error"])
    else:
        st.subheader(f"📌 Career: {data['career']}")

        st.write("### 🔧 Required Skills:")
        for skill in data["skills"]:
            st.write(f"- {skill}")

        st.write("### 📚 Recommended Courses:")
        for course in data["courses"]:
            st.write(f"{course['course']} ({course['platform']}) - {course['level']}")

st.markdown("## 🤖 AI Career Chatbot")

user_query = st.text_input("Ask anything about career...")

if st.button("Ask"):
    response = chatbot_response(user_query)
    st.write("💡", response)

import pandas as pd
import sqlite3

# 👨‍💻 Admin Panel
if st.session_state.user == "admin":

    st.markdown("## 👨‍💻 Admin Dashboard")

    conn = sqlite3.connect("database/career_guide.db")

    # 👤 Users table
    users_df = pd.read_sql("SELECT * FROM users", conn)
    st.subheader("👤 All Users")
    st.dataframe(users_df)

    # 📊 Resume Analysis table
    analysis_df = pd.read_sql("SELECT * FROM resume_analysis", conn)
    st.subheader("📊 Resume Analysis Data")
    st.dataframe(analysis_df)

    # ⬇ Download button
    st.download_button(
        "Download Data",
        analysis_df.to_csv(index=False),
        "analysis_data.csv"
    )

    conn.close()