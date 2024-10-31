import streamlit as st
import info
import pandas as pd

#About Me
def about_me_section():
    st.header("About Me")
    st.image(info.profile_picture, width= 200)
    st.write(info.about_me)
    st.write("---")

about_me_section()

#Sidebar Links
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Follow me on Instagram!")
    insta_link=f'<a href="{info.my_insta}"><img src="{info.insta_image}" alt="Instagram" width= "75" height="75"></a>'
    st.sidebar.markdown(insta_link, unsafe_allow_html=True)
    st.sidebar.text("Follow my Pinterest!")
    pinterest_link= f'<a href="{info.my_pinterest}"><img src="{info.pinterest_image}" alt="Pinterest" width="65" height="65"></a>'
    st.sidebar.markdown(pinterest_link, unsafe_allow_html=True)
    st.sidebar.text("Email Me!")
    email_html= f'<a href= "mailto:{info.my_email_address}"><img src="{info.email_image}" alt= "Email" width= "75" height= "65"></a>'
    st.sidebar.markdown(email_html,unsafe_allow_html=True)

links_section()

#Education
def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f" **Degree:** {education_data['Degree']}")
    st.write(f" **Graduation Date:** {education_data['Graduation Date']}")
    st.write(f" **GPA:** {education_data['GPA']}")
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code":"Course Code",
        "names":"Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I learned"},
        hide_index = True,
                    )
    st.write("---")
education_section(info.education_data, info.course_data)

#Professional Experience
def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title,(job_description,image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width= 250)
        for bullet in job_description:
            expander.write(bullet)
        st.write("---")
experience_section(info.experience_data)
#Projects
def project_section(projects_data):
    st.header("Projects")
    for project_name, project_description in projects_data.items():
        expander= st.expander(f"{project_name}")
        expander.write(project_description)
        st.write("---")
project_section(info.projects_data)

#Skills
def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("My Skills")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill,'')}")
        st.progress(percentage)
        
    st.write("---")
    
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        proficiency_levels = proficiency.split(',')  
        proficiency_icons = [info.spoken_icons.get(spoken, '')] * len(proficiency_levels) 
        for level, icon in zip(proficiency_levels, proficiency_icons):
            st.write(f"{spoken} - {level} {icon}")
skills_section(info.skills_data,info.spoken_data)

#Activites
def activities_section(leadership_data,activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership","Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title,(details,image) in leadership_data.items():
            expander= st.expander(f"{title}")
            expander.image(image,width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title,details in activity_data.items():
            expander= st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
    st.write("---")
activities_section(info.leadership_data,info.activity_data)
    

        
        
        
    
    
    
