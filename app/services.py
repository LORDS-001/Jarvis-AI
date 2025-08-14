# app/services.py
import os
import datetime
import wikipedia
import smtplib
import psutil as ps
import pyautogui as pag
import pyjokes as pj
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
REMEMBER_FILE = DATA_DIR / "remember.txt"

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def get_time() -> str:
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date() -> str:
    # e.g., "Wednesday, 13 August 2025"
    return datetime.datetime.now().strftime("%A, %d %B %Y")

def wiki_summary(topic: str, sentences: int = 2) -> str:
    try:
        return wikipedia.summary(topic, sentences=sentences, auto_suggest=False, redirect=True)
    except wikipedia.DisambiguationError as e:
        # Give user options
        return f"Your query is ambiguous. Options: {', '.join(e.options[:5])}..."
    except wikipedia.PageError:
        return "I couldn’t find a Wikipedia page for that."
    except Exception as e:
        return f"Something went wrong: {e}"

def send_email(to: str, content: str, subject: str | None = None) -> str:
    if not (EMAIL_USER and EMAIL_PASS):
        return "Email not configured on server."
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = to
    msg["Subject"] = subject or "Jarvis Message"
    msg.attach(MIMEText(content, "plain"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.ehlo()
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)

    return "Email sent."

def take_screenshot() -> str:
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = DATA_DIR / f"screenshot_{ts}.png"
    img = pag.screenshot()
    img.save(path.as_posix())
    return str(path)

def cpu_battery_status() -> dict:
    usage = ps.cpu_percent(interval=0.5)
    info = {"cpu_percent": usage}
    try:
        battery = ps.sensors_battery()
        if battery:
            info["battery_percent"] = battery.percent
            info["power_plugged"] = battery.power_plugged
        else:
            info["battery"] = "not_available"
    except Exception:
        info["battery"] = "not_supported"
    return info

def random_joke() -> str:
    return pj.get_joke()

def remember(note: str) -> str:
    with open(REMEMBER_FILE, "a", encoding="utf-8") as f:
        ts = datetime.datetime.now().isoformat(timespec="seconds")
        f.write(f"[{ts}] {note}\n")
    return "Saved."

def recall() -> str:
    if not REMEMBER_FILE.exists():
        return "There’s nothing saved yet."
    with open(REMEMBER_FILE, "r", encoding="utf-8") as f:
        data = f.read().strip()
    return data or "There’s nothing saved yet."

def search_url(query: str) -> str:
    return f"https://www.google.com/search?q={query.replace(' ', '+')}"
