import streamlit as st
from pathlib import Path
from PIL import Image
import base64

def image_to_base64(image_path):
    """Convert image to base64 string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "samcv.pdf"
profile_pic = current_dir / "assets" / "profile.png"
linkedin_icon = current_dir / "assets" / "in_logo.png"
github_icon = current_dir / "assets" / "gt_logo.png"
whatsapp_icon = current_dir / "assets" / "wp_logo.png"

# ---------------------GENERAL SETTINGS----------------------------------------------------------------------------

PAGE_TITLE = "DIGITAL CV | SAMEER"
PAGE_ICON = ":wave:"
NAME = "Sameer Raghuwanshi"
DESCRIPTION = """
Enthusiastic and self-driven software engineer with a strong foundation in Python development.
"""
EMAIL = "sameer281797@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": {
        "url": "https://www.linkedin.com/in/sameer-raghuwanshi/",
        "icon": linkedin_icon
    },
    "GitHub": {
        "url": "https://github.com/Sameer281797",
        "icon": github_icon
    },
    "WhatsApp": {
        "url": "https://wa.me/9589415578", 
        "icon": whatsapp_icon
    },
}
PROJECTS = {
    "Projects": "https://github.com/Sameer281797?tab=repositories"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# -------------Load CSS, PDF and Profile PIC----------------------------------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ------------------------------HERO SECTION----------------------------------------------------

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
        mime="application/octet-stream"
    )
    st.write("📫", EMAIL)
    
# SOCIAL LINKS
st.write("\n")
st.markdown("""
    <div style="display: flex; justify-content: left; gap: 20px;">
        <a href="https://www.linkedin.com/in/sameer-raghuwanshi/" target="_blank">
            <img src="data:image/png;base64,{}" width="60"/>
        </a>
        <a href="https://github.com/Sameer281797" target="_blank">
            <img src="data:image/png;base64,{}" width="60"/>
        </a>
        <a href="https://wa.me/9589415578" target="_blank">
            <img src="data:image/png;base64,{}" width="60"/>
        </a>
    </div>
""".format(
    image_to_base64(linkedin_icon), image_to_base64(github_icon), image_to_base64(whatsapp_icon)
), unsafe_allow_html=True)


# --- QUALIFICATIONS ---

st.write('\n')
st.subheader("Qualifications")
st.write("---")

st.write("📝", "**S.A.T.I.  (Samrat Ashok Technological Institute)**")
st.write("Sep '23 - Present")
st.write("► Bachelors in Computer Science Engineering (Blockchain)")
st.write('\n')
st.write("📝", "**S.A.T.I.  (Samrat Ashok Technological Institute)**")
st.write("Jul '20 - Jun '23")
st.write("► Diploma in Computer Science Engineering: --- 7.14 CGPA")

# --- WORK HISTORY ---

st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("💻", "**Customer Service Associate | Tech Mahindra**")
st.write("Jun '24 – Nov '24")
st.write(
    """
- ► Investigated and resolved customer issues related to products and services through various channels.

- ► Took ownership of customer inquiries, ensuring a high level of satisfaction and timely resolution.

- ► Assisted new team members with process workflows and operations, boosting team efficiency.
"""
)

# --- JOB 2
st.write('\n')
st.write("💻", "**Web Development Intern | Iyuram**")
st.write("Sep '22 – Nov '22")
st.write(
    """
- ► Collaborated with other developers in designing solutions for complex problems.

- ► Conducted cross-browser testing to ensure website compatibility and responsiveness.
"""
)

# --- HARD SKILLS --- 

st.write('\n')
st.subheader("Hard Skills")
st.write("---")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.write("✔️ Python")
    st.write("✔️ Flask")
    st.write("✔️ MS-EXCEL")

with col2:
    st.write("✔️ DSA")
    st.write("✔️ Django")
    st.write("✔️ SQL")


# --- Projects ---

st.write('\n')
st.subheader("Projects")
st.write("---")
st.write("Checkout my Github for Projects!")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
