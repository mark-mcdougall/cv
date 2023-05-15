from pathlib import Path
import streamlit as st
from PIL import Image

# SET PATH
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# GENERAL SETTINGS
PAGE_TITLE = "CV | Mark McDougall"
PAGE_ICON = "📊"
NAME = "Mark McDougall"
DESCRIPTION = "Data Analyst based in Edinburgh with 8 years of experience, 3 years working remotely with international teams in multiple timezones."

EMAIL= "mark.mcdougall@hotmail.co.uk"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mark-mcdougall-2944a1129/",
    "GitHub": "https://github.com/mark-mcdougall"
}

PROJECTS = {
    "🌎 Administrative Geography to Postcode Conversion, Data Augmentation and Mapping": "https://github.com/mark-mcdougall/data_analytics/blob/main/projects/geo_projects/mapping/Admim_geo_to_postcode_data_aumentation_and_mapping.ipynb"
}

# PAGE TITLE AND FAVICON
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# LOAD CSS, CV PDF AND IMAGE
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# PAGE CONTENT
# TOP SECTION
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)

# SOCIAL MEDIA
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for col, (name, link) in zip(cols, SOCIAL_MEDIA.items()):    
    col.write(f"[{name}]({link})")

# EXPERIENCE AND QUALIFICATIONS
st.write("#")
st.subheader("Experience and Qualifications")
st.write(
    """
    - 8 years experience extracting actionable insights from data
    - Creation and management of data pipelines in Python and SQL
    - Data visualisation and dashboarding in Python
    - Geospatial data analysis and mapping in Python
    - 3 years experience working remotely with international teams in multiple timezones
    """
)

# SKILLS
st.write("#")
st.subheader("Skills")
st.write(
    """
    - Data Analysis: Python (Pandas, Numpy), SQL
    - Data Visualisation: Python (Holoviz, Plotly, hvplot, Panel, Matplotlib, Seaborn)
    - Geospatial Data Analysis and Mapping: Python (GeoPandas, Geoviews, Shapely, Cartopy)
    - Data Pipelines: Python (Pandas, Numpy, SQLAlchemy, Requests), SQL
    - Databases: PostgreSQL, SQLite, MS SQL
    - Containerisation: Docker
    - Version Control: Git, GitHub
    - Agile: Jira, Confluence
    - Customer Interaction: Salesforce
    """
)

# PROJECTS
st.write("#")
st.subheader("Projects")
cols = st.columns(len(PROJECTS))
for col, (name, link) in zip(cols, PROJECTS.items()):
    col.write(f"[{name}]({link})")


