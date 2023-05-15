from pathlib import Path
import streamlit as st
from PIL import Image

# SET PATH (RELATIVE TO app.py)
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# GENERAL SETTINGS
PAGE_TITLE = "CV | Mark McDougall"
PAGE_ICON = "📊"
NAME = "Mark McDougall"
DESCRIPTION = "Data Analyst, assisting businesses in making data-driven decisions."

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
st.write("#") # ADD SPACE
cols = st.columns(len(SOCIAL_MEDIA))
for col, (name, link) in zip(cols, SOCIAL_MEDIA.items()):    
    col.write(f"[{name}]({link})")

# EXPERIENCE AND QUALIFICATIONS
st.write("#")
st.subheader("Experience and Qualifications")
st.write(
    """
    - 8 years experience extracting actionable insights from data
    - Strong knowledge and hands-on experience in data analysis using Python and SQL
    - 3 years experience working remotely with international teams in multiple timezones
    - Experience leading projects in an agile environment and mentoring junior team members
    """
)

# SKILLS
st.write("#")
st.subheader("Skills")
st.write(
    """
    - Data Analysis: Python (Pandas, Numpy, Scikit-learn), SQL
    - Data Visualisation: Python (Holoviz, Plotly, hvplot, Panel, Matplotlib, Seaborn)
    - Geospatial Data Analysis and Mapping: Python (GeoPandas, Geoviews, Shapely, Cartopy)
    - Data Pipelines: Python (Pandas, Numpy, SQLAlchemy, Requests), SQL
    - Databases: PostgreSQL, SQLite, MS SQL Server
    - Containerisation: Docker
    - Version Control: Git, GitHub
    - Agile: Jira, Confluence
    - Customer Interaction: Salesforce
    """
)

# WORK HISTORY 
st.write("#")
st.subheader("Work History")
st.write("---") # ADD LINE BREAK

# JOB 1
st.write("**Data Analyst | S and P Global Platts**")
st.write("September 2021 - March 2023")
st.write(
    """
    * Supported two development teams in the migration of approximately 150 datasets to DataBricks through end-to-end analysis of existing dataflows
    * Used Python, SQL and DataBricks to produce an automated, twice daily email report that alerted the Data Collections team to any issues with datasets missing data
    * Produced a workflow in Python that allowed external customers to access and process data using an api
    * Performed software releases of the BAU team’s data fixes to the Production environment
    * Greatly improved the onboarding of new BAU team members by identifying current processes and writing documentation
    """
)

# JOB 2
st.write("**Data Analyst | B and PO**")
st.write("April 2019 - March 2021")
st.write(
    """
    * Delivered bespoke analytics reports for multinational, household name clients
    * Produced interactive presales reports to assist the sales team in winning new business
    * Delivered a new geospatial analytics method that resulted in multiple new clients and tens of thousands of pounds in revenue
    * Sourced, cleaned and transformed freely available online datasets from multiple reputable sources to produce richer, original datasets with actionable business value, saving my employer tens of thousands annually in data costs
    """
)

# JOB 3
st.write("**Data Analyst | Adapptive**")
st.write("April 2017 - April 2019")
st.write(
    """
    * In collaboration with four developers, led the successful delivery of multiple new features and the full redesign of the existing functionality of the Adapptive advertising software product
    * Produced mock data datasets to enable the development, testing and demonstration of new software features
    * Managed a team of four developers and a data analyst when my boss was frequently working remotely at another office
    * Recruited, trained and mentored a new data analyst
    """
)

# JOB 4
st.write("**Data Analyst | Red Fox Media**")
st.write("January 2015 - April 2017")
st.write(
    """
    * Designed, trafficked, managed and optimized ad campaigns, including the production of customer data segments
    * Cleaned, processed, updated and managed client data files and third-party data sources
    """
)

# PROJECTS
st.write("#")
st.subheader("Projects")
st.write("---") 
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


