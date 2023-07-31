import streamlit as st

# Add a title to the app
st.markdown('<h1 style="color:blue;">WELCOME TO YOUR CLINIC</h1>', unsafe_allow_html=True)
# Add a selection option in the sidebar
selected_project = st.sidebar.selectbox("Choose the part you want to check", ("Brain Detection", "Pneumonia Detection"))

# Load the selected project based on user choice
if selected_project == "Brain Detection":
    # Import and run the main_brain.py from project_brain
    import main_brain
    main_brain.run()

elif selected_project == "Pneumonia Detection":
    # Import and run the main_chest.py from project_chest
    import main_chest
    main_chest.run()