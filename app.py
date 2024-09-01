import streamlit as st

st.title("My Autobiography and Portfolio")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Autobiography", "Portfolio", "Contact"])

# Autobiography page
if page == "Autobiography":
    st.header("About Me")
    st.image("picture1.jpg", width=300)
    st.subheader("Hello, I'm Leemar A. Paner !")
    st.write("""
        I am a 4th-year Bachelor of Science in Information Technology (BSIT) student at Cebu Institute of Technology University. 
        I currently live in Casamira, Naga South. I have a passion for creating visually appealing and user-friendly interfaces. 
        I am dedicated to crafting digital experiences that are not only functional but also enjoyable.
    """)

# Portfolio page
elif page == "Portfolio":
    st.header("My Portfolio")
    
    st.subheader("Project 1: Capstone")
    st.write("""Role: UI/UX Designer""")
    st.write("""
        This capstone project investigates the process Wildcat Innovation Labs, an incubator program, uses to review and select startups for its program. 
        The project is likely to involve analyzing the current process, identifying areas for improvement, 
        and potentially developing or recommending a new system for evaluating and selecting promising startups.
    """)
    st.image("Capstone.jpg", width=400)
    
    st.subheader("Project 2: Event Tracker")
    st.write("""Role: UI/UX Designer""")
    st.write("""
        Event Tracker is your go-to portal for staying updated on all the latest events happening in your university. 
        With our comprehensive event listings, you can easily find and explore a wide range of activities, from workshops and seminars to concerts and sports events. 
        Stay connected with the vibrant campus community and never miss out on the fun!
    """)
    st.image("EventTracker.jpg", width=400)
    
    st.subheader("Project 3: Focusify")
    st.write("""Role: UI/UX Designer""")
    st.write("""
        Enhance students' study sessions by providing a comprehensive study tool. 
        It aims to improve focus, time management, and overall productivity during study sessions. 
        The customizable timers will help users stay on track, and the music feature is designed to create a conducive study environment. 
        The goal is to optimize the study experience for students, making it more enjoyable and effective.
    """)
    st.image("Focusify.jpg", width=400)

# Contact page
elif page == "Contact":
    st.header("Contact Me")
    
    st.subheader("Get in Touch")
    st.write("Feel free to reach out to me through any of the following channels:")
    
    st.write("**Email:** leemarpaner321@gmail.com")
    st.write("**Phone:** +63 906 430 9984")
    
    st.write("You can also use the form below to send me a message directly.")
    
    # Contact form
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    if st.button("Send Message"):
        if name and email and message:
            st.success(f"Thank you {name}! Your message has been sent.")
        else:
            st.error("Please fill out all fields before sending.")

# Footer
st.sidebar.title("About")
st.sidebar.info("This is my simple Streamlit application to showcase my autobiography and portfolio.")
