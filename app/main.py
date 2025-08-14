from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import EmailRequest, RememberRequest, SearchRequest
from app import services

app = FastAPI(
    title="Jarvis API",
    description="HTTP endpoints for Jarvis actions (time, date, wiki, email, screenshot, cpu, jokes, notes).",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["meta"])
def health():
    return {"status": "ok"}

@app.get("/time", tags=["utility"])
def time_now():
    return {"time": services.get_time()}

@app.get("/date", tags=["utility"])
def date_now():
    return {"date": services.get_date()}

@app.get("/wikipedia", tags=["info"])
def wikipedia_summary(q: str, sentences: int = 2):
    return {"query": q, "summary": services.wiki_summary(q, sentences)}

@app.post("/send-email", tags=["comm"])
def post_email(req: EmailRequest):
    try:
        msg = services.send_email(req.to, req.content, req.subject)
        return {"status": "ok", "message": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/screenshot", tags=["system"])
def screenshot():
    try:
        path = services.take_screenshot()
        return {"status": "ok", "path": path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Screenshot failed: {e}")

@app.get("/cpu", tags=["system"])
def cpu():
    return services.cpu_battery_status()

@app.get("/joke", tags=["fun"])
def joke():
    return {"joke": services.random_joke()}

@app.post("/remember", tags=["memory"])
def post_remember(req: RememberRequest):
    return {"message": services.remember(req.note)}

@app.get("/remember", tags=["memory"])
def get_remember():
    return {"data": services.recall()}

@app.post("/search", tags=["utility"])
def search(req: SearchRequest):
    return {"url": services.search_url(req.query)}
