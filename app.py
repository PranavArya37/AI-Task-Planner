import os
import streamlit as st
import google.generativeai as genai

# --- Configuration ---
try:
    # This works when running locally if you have a .env file
    from dotenv import load_dotenv
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
except:
    # This works when deployed on Streamlit Community Cloud
    # where the secret is stored in st.secrets
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


# --- AI Function (same from task_agent.py) ---
def summarize_tasks(tasks):
    """Makes a call to the Gemini API with a prompt to categorize tasks."""
    if not tasks or not tasks.strip():
        return "Please provide some tasks to plan."

    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    You are a smart task planning agent. Your goal is to help users prioritize.
    Given the following list of tasks, categorize them into 3 priority buckets: High, Medium, and Low.

    Tasks:
    {tasks}

    Return the response in a clear, well-formatted list.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, I couldn't process the tasks. Please check the API key and try again."


# --- Streamlit User Interface ---

# page title and icon
st.set_page_config(page_title="AI Task Planner", page_icon="🤖")

st.title("🤖 AI Task Planner")
st.markdown("Welcome! I'm your AI agent. Provide me with a list of tasks, and I'll sort them into High, Medium, and Low priority buckets for you.")

# two columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Input Your Tasks")
    # Method 1: Text Area for manual input
    task_input = st.text_area(
        "Paste your tasks here (one task per line):", 
        height=200,
        placeholder="- Reply to customer support tickets\n- Write the monthly newsletter\n- Fix login bug"
    )

with col2:
    st.subheader("📄 Or Upload a File")
    # Method 2: File uploader
    uploaded_file = st.file_uploader("Upload a .txt file with your tasks:", type=['txt'])

# The "Plan My Tasks" button to trigger the analysis
if st.button("Plan My Tasks", type="primary"):
    tasks_to_process = ""
    # Prioritize the text area, but fall back to the uploaded file
    if task_input:
        tasks_to_process = task_input
    elif uploaded_file is not None:
        # To read a file uploaded with Streamlit, we need to decode it
        tasks_to_process = uploaded_file.getvalue().decode("utf-8")

    # If there are tasks to process, show a spinner and run the AI
    if tasks_to_process:
        with st.spinner('🤖 The AI agent is analyzing your tasks...'):
            summary = summarize_tasks(tasks_to_process)
            st.subheader("✅ Your Prioritized Task Plan")
            # st.markdown() renders the output with proper formatting
            st.markdown(summary)
    else:
        # Show an error if the button is clicked with no input
        st.error("Please enter some tasks or upload a file first!")

st.markdown("---")
st.markdown("Made with ❤️ by **[Pranav Arya](https://pranavarya.in)**")