import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | "
PAGE_ICON = ":wave:"
NAME = "Blendi Gashi"
DESCRIPTION = """
Data Scientist  Student.
"""

EMAIL = "blendi.gashi@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/blendi-gashi-0807a4276/"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "assets/cv_12_2024.pdf"
profile_pic_file = "assets/profile-pic.jpeg"


profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About","Contact"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="CV.pdf",
            mime="application/octet-stream",
        )

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications")
    st.write(
        """
- ✔️ Extensive experience with spatial-sensor data and algorithm development.
- ✔️ Skilled in Python (FastAPI, Pandas, Numpy), SQL, DBT, and Airflow.
- ✔️ Experienced in visualizing and analyzing sensor data to deliver insights.
- ✔️ Proficient in PowerBI and interactive dashboard development.
"""
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- 👩‍💻 Programming: Python, Java, SQL, 
- 📊 Data Visualization: Pandas, Streamlit
- 🗄️ Databases: PostgreSQL
- 🤖 Machine Learning Bootcamp
"""
    )

    # --- WORK HISTORY ---
    st.write("\n")
    st.subheader("Education")
    st.write("---")

    st.write( "**BSc in Computer Science | University of Prizren**")
    st.write("2023 - 2026")


    

elif page == "About":
    st.title("About Me")
    st.write("""
    Programer and It student with a passion for data science and machine learning. I have experience working with spatial-sensor data and developing algorithms to extract insights from it. I am proficient in Python, SQL, and various data visualization tools. I am currently pursuing a BSc in Computer Science at the University of Prizren, where I am honing my skills and expanding my knowledge in the field of data science.
    """)

    # Show LinkedIn and Email only on the About page
    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")
