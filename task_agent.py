import os
from dotenv import load_dotenv

import google.generativeai as genai

# load env
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# read task from file
def read_tasks(filepath):
    with open(filepath, "r") as f:
        return f.read()

# make a call to gemini with prompt to categorize our tasks

def summarize_tasks(tasks):
    """
    Makes a call to the Gemini API with a prompt to categorize tasks.
    """
    # Instantiate the model from the new library
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    You are a smart task planning agent. Given a list of tasks, categorize them into 3 priority buckets:
    1. High Priority: Tasks that are urgent and important.
    2. Medium Priority: Tasks that are important but not urgent.
    3. Low Priority: Tasks that are neither urgent nor important.

    Tasks:
    {tasks}

    Return the response in the following format:
    High Priority:
    - Task 1
    - Task 2

    Medium Priority:
    - Task 1
    - Task 2

    Low Priority:
    - Task 1
    - Task 2
    """
    
    response = model.generate_content(prompt)

    try:
        return response.text
    except ValueError:
        print("Response was blocked or failed. Feedback:", response.prompt_feedback)
        return "Could not generate summary."

if __name__ == "__main__":
    try:
        task_text = read_tasks("tasks.txt")
        summary = summarize_tasks(task_text)
        print("\n🤖 Task Summary 🤖\n")
        print("-" * 30)
        print(summary)
    except FileNotFoundError:
        print("Error: tasks.txt not found. Please create the file with your tasks.")