🤖 Smart Career Guide (AI-Based Career Recommendation System)

📌 Overview

Smart Career Guide is an AI-powered web application designed to help students choose the right career path after 12th grade. The system analyzes user input such as resume, skills, stream, and interests to provide personalized career recommendations, roadmaps, and insights.

---

🚀 Features

🔐 User Authentication

- Secure login and registration system
- Session-based authentication

📄 Resume Analysis

- Upload resume (PDF/DOCX)
- Extract text and detect skills
- Generate resume score

🎯 Career Recommendation System

- Suggests careers based on:
  - Stream (Science, Commerce, Arts)
  - User interests
- Displays match score and description

🗺️ Career Roadmap Generator

- Provides:
  - Required skills
  - Recommended courses
- Helps users plan their career journey

🤖 AI Career Chatbot

- Answers user queries related to careers
- Integrated inside the web app

👨‍💻 Admin Dashboard

- View all registered users
- View resume analysis data
- Download data as CSV

---

🛠️ Tech Stack

- Frontend/UI: Streamlit + HTML + CSS
- Backend: Python
- Database: SQLite
- Libraries Used:
  - Pandas
  - Streamlit
  - SQLite3
  - PDF/DOCX parsers

---

📂 Project Structure

AI_Career_Guidance/
│
├── app.py
├── core/
│   ├── career_engine.py
│   ├── roadmap_generator.py
│   ├── chatbot_engine.py
│   ├── resume_parser.py
│   └── resume_analysis.py
│
├── database/
│   ├── db_manager.py
│   └── career_guide.db
│
├── data/
│   └── careers.csv
│
├── assets/
│   └── style.css
│
├── create_admin.py
├── requirements.txt
└── README.md

---

⚙️ Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/Satnaam-coder/AI_Career_Guide.git
cd AI_Career_Guide

2️⃣ Create virtual environment

python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run the application

streamlit run app.py

---

🔑 Admin Access

Create admin user:

python create_admin.py

Default credentials:

Username: admin
Password: admin123

---

📊 Future Enhancements

- 🌍 Integration with real-world large datasets
- 🤖 Advanced AI chatbot (ChatGPT-like)
- 📊 Data visualization dashboard
- 🎯 Skill gap analysis
- 💼 Job recommendation system

---
👩‍💻 Author

Dimple

---

⭐ Acknowledgment

This project was developed as an end-semester project to demonstrate AI-based career guidance using modern web technologies.

---
