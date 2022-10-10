from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_digital.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sayed Jawid Mortazawi"
PAGE_ICON = ":wave:"
NAME = "Sayed Jawid Mortazawi"
DESCRIPTION = """
        Python🐍 Developer looking for a job both remotely or at place. 
"""


EMAIL = "benjimortal@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com/benjimortal",
    "Whatsapp": "+46 723000247"

}
PROJECTS = {
    "🏆 House price Predictions": "https://github.com/benjimortal/house_repo",
    "🏆 Stock Price": "https://github.com/exout/AI_Python",
    "🏆 Sentiment Analysis": "https://github.com/exout/AI_Python/tree/main/Models/sentiment_analysis",
    "🏆 AI Chatbot": "https://github.com/benjimortal/AI_chatbot",
    "🏆 Space Invaders": "https://github.com/benjimortal/project",


}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 👩‍💻 Python, Flask and Git
- ✔️ 🗄️ Databases: MySQL, SQL, MongoDB 
- ✔️ 💻🤖 Machin Learning
- ✔️ 📊 Data Visualization
- ✔️ 📚 Modeling: Logistic regression, linear regression, decision trees

"""
)

# --- WHAT I DO IN FREE TIME ---
st.write('\n')
st.subheader("Free Time")
st.write("---")

# ---  1
st.write(
    """
    I like to spend my time with my family and friends when I have free time.
    I like to play soccer and be active at gym.
    Playing video games is my favorite things to do in my fee time.
    I like to read books, go to cinema and more.
    My friends like me as a loyal person and trusty.
    I love what I do because I do what I love.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "Studied at Teknikhogskolan in Gutenberg, Sweden")
st.write("2020-2022")
st.write(
    """
- ► Two years of education as python developer with focus on AI
- ► During the education I have built many single projects and with groups

"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")