# LORDS AI Backend (FastAPI)

A Python FastAPI backend for **LORDS AI**, providing endpoints for time, date, email, jokes, Wikipedia summaries, screenshots, CPU/battery status, remembering notes, and search links.

---

## Step 1: Clone the Repository

git clone https://github.com/yourusername/LORDS-AI.git
cd LORDS-AI

---

## Step 2: Create a Virtual Environment

python -m venv .venv
Creates an isolated environment to manage dependencies.

---

## **Step 3: Activate the Virtual Environment**

Windows (PowerShell):

. .venv\Scripts\Activate.ps1


Windows (CMD):

.venv\Scripts\activate.bat


macOS / Linux:

source .venv/bin/activate

---

## **Step 4: Install Dependencies**
```bash
pip install -r requirements.txt```

Installs FastAPI, uvicorn, PyAutoGUI, pyttsx3, pyjokes, psutil, wikipedia, python-dotenv, and other required packages.

---

## **Step 5: Set Up Environment Variables**

Create a .env file in the project root:

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
DATA_DIR=./data


### **Note: For Gmail or Outlook, you need an App Password (requires 2FA).**

---

## **Step 6: Run the FastAPI Server**
```bash
uvicorn app.main:app --reload```


Server starts on http://127.0.0.1:8000

Open http://127.0.0.1:8000/docs to see the interactive API docs (Swagger UI)

---

## **Step 7: Testing Endpoints**
Example using curl:

Get Time

```bash
curl http://127.0.0.1:8000/time```

Take Screenshot

```bash
curl -X POST http://127.0.0.1:8000/screenshot```


Send Email

```bash
curl -X POST http://127.0.0.1:8000/email \
-H "Content-Type: application/json" \
-d '{"to":"example@gmail.com","subject":"Hello","content":"This is a test"}'```

Remember a Note

```bash
curl -X POST http://127.0.0.1:8000/remember \
-H "Content-Type: application/json" \
-d '{"note":"Buy milk tomorrow"}'```

---

## **Step 8: File Storage**

Screenshots and remembered notes are stored in data/:

data/
   remember.txt
   screenshot_YYYYMMDD_HHMMSS.png

Path can be customized in .env.

---

## **Step 9: Troubleshooting**
-Screenshot Issues (PyAutoGUI / Pillow)

If you see an error like:

PyAutoGUI was unable to import pyscreeze...


PyAutoGUI depends on Pillow, which may not fully support Python 3.13.

Fix options:

```bash
pip uninstall pillow
pip install --upgrade pillow
pip install --pre --upgrade pillow  # if using Python 3.13+```


Or downgrade Python to 3.11 or 3.10 for full compatibility.

-Email Sending Issues

Ensure .env has correct email and App Password.

Gmail/Outlook requires 2FA + App Password.

General Tips

Always activate your .venv before running the server.

Use /docs to interact visually.

Check data/ folder permissions for saving files.

---

## **Step 10: Endpoint Diagram**
+----------------+           +----------------------+
|   Client / UI  |  --->     |  FastAPI Endpoints   |
+----------------+           +----------------------+
        |                            |
        | /time                      | get_time()
        | /date                      | get_date()
        | /email (POST)              | send_email(to, content, subject)
        | /joke                      | random_joke()
        | /wikipedia?query=XYZ      | wiki_summary(topic)
        | /screenshot (POST)         | take_screenshot()
        | /cpu                       | cpu_battery_status()
        | /remember (POST)           | remember(note)
        | /recall                    | recall()
        | /search?query=XYZ         | search_url(query)


The Client/UI could be a frontend, Postman, or CLI.

The FastAPI Endpoints call functions in services.py.

✅ Your LORDS AI backend is now fully ready for testing, frontend integration, or expansion.


---
