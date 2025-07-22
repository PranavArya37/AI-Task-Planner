# 🤖 AI Task Planner

An intelligent web app that uses the **Google Gemini API** to automatically read a list of tasks and categorize them into **High**, **Medium**, and **Low** priority buckets.

### 🔗 [Live Demo](https://aitaskplanner.streamlit.app/)

## 🖼️ Screenshots

<table>
  <tr>
    <th>Manual Input</th>
    <th>File Upload</th>
  </tr>
  <tr>
    <td><img src="https://private-user-images.githubusercontent.com/43077165/469198571-7a70660e-dcb0-4c99-b312-13914a36564b.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTMxODg4OTQsIm5iZiI6MTc1MzE4ODU5NCwicGF0aCI6Ii80MzA3NzE2NS80NjkxOTg1NzEtN2E3MDY2MGUtZGNiMC00Yzk5LWIzMTItMTM5MTRhMzY1NjRiLmpwZWc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzIyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcyMlQxMjQ5NTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mYmNiOWNjNGJkNTQ2N2YzMDg5Y2MwMTdmMmQyYjk0MDdlY2Y1YjY0MmUwZWVhNjQ5MDYzY2Y1NmM4YjEwMDkyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9._EuH9guj_pg7wSv2uj8GzhzA6oPJw5nkqgadomfUopM" width="500" alt="Text Area for manual input" /></td>
    <td><img src="https://private-user-images.githubusercontent.com/43077165/469196104-b5dfefbf-609b-48f8-b52f-977c1e57f3ad.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTMxODg2MDgsIm5iZiI6MTc1MzE4ODMwOCwicGF0aCI6Ii80MzA3NzE2NS80NjkxOTYxMDQtYjVkZmVmYmYtNjA5Yi00OGY4LWI1MmYtOTc3YzFlNTdmM2FkLmpwZWc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzIyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcyMlQxMjQ1MDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hOTJlNWJkYzE3NzRkZGU5NWM2MWY5YzhlYzQ5N2E4MWIxMTNjNjI2MGFiNzc3NzEyMzE3MjJkMzgxMjgzNzM5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.r9znr1y-itNz0QGUfD0I4ZjfHoK15cBOVzAwd-YXOrg" width="500" alt="File uploader" /></td>
  </tr>
  <tr>
    <th colspan="2" align="center">Full App with AI Output</th>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <img src="https://private-user-images.githubusercontent.com/43077165/469197574-a2e7cc5e-c9ab-4a49-aa94-0b15a488ad31.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTMxODg3NDgsIm5iZiI6MTc1MzE4ODQ0OCwicGF0aCI6Ii80MzA3NzE2NS80NjkxOTc1NzQtYTJlN2NjNWUtYzlhYi00YTQ5LWFhOTQtMGIxNWE0ODhhZDMxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA3MjIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNzIyVDEyNDcyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTcxNmIxNzQyZmI0YzM1ZWQyMzg2ZGM0N2ZkYzlkNzg1NmExMTEzZGYyNDY5MDUyMzRjZWM5OWNiM2ZjMjgyZWYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.OeinAVaF3f6yE6Gdb7HhRlGJqU3wjqeLGp9KflBebcs" width="500" alt="Full App with AI Output" />
    </td>
  </tr>
</table>

---

## ✨ Features

- 🔹 **Intuitive Interface:** Clean and simple UI built with Streamlit
- 🔹 **Dual Input Options:** Paste tasks manually or upload a `.txt` file
- 🔹 **AI-Powered Prioritization:** Uses Google Gemini to analyze and sort tasks
- 🔹 **Formatted Output:** Tasks are clearly categorized for quick understanding

---

## 🛠️ Tech Stack

- **Backend:** Python  
- **AI Model:** Google Gemini API (`gemini-1.5-flash`)  
- **Web Framework:** Streamlit  
- **Deployment:** Streamlit Community Cloud  

---

## 🚀 Getting Started (Run Locally)

### 1. Clone the Repository

```bash
git clone https://github.com/PranavArya37/AI-Task-Planner.git
cd AI-Task-Planner
````

### 2. Set Up a Virtual Environment

#### On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY="your_actual_api_key_here"
```

### 5. Run the App

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`.

---

## ☁️ Deployment

This app is deployed using **Streamlit Community Cloud**.
Environment variables are managed securely via Streamlit's secrets management, and dependencies are installed from `requirements.txt`.

---

## 🙋 Contributing

Contributions are welcome!
If you have suggestions or improvements, feel free to fork the repo and open a pull request.

---

## 🧑‍💻 Author

🌐 [Pranav Arya](https://pranavarya.in)

📫 Get in touch via [LinkedIn](https://www.linkedin.com/in/pranavarya37/) or [Twitter](https://twitter.com/pranavarya37)

---

## 📝 License

This project is licensed under the MIT ```License```. See the LICENSE file for details.
