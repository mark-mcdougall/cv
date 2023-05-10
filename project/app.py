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
DESCRIPTION = "Data Analyst based in Edinburgh with 8 years of experience, with 3 years working remotely with international teams in multiple timezones."

EMAIL= "mark.mcdougall@hotmail.co.uk"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mark-mcdougall-2944a1129/",
    "GitHub": "https://github.com/mark-mcdougall"
}

PROJECTS = {
    "🌎 Administrative Geography to Postcode Data Augmentation, Conversion and Mapping": "https://github.com/mark-mcdougall/data_analytics/blob/main/projects/geo_projects/mapping/Admim_geo_to_postcode_data_aumentation_and_mapping.ipynb"}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# LOAD CSS, PDF AND IMAGE
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbytes = pdf_file.read()
profile_pic = Image.open(profile_pic)

# TOP SECTION
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download CV",
        data=PDFbytes,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)
