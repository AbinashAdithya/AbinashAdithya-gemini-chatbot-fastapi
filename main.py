from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import google.generativeai as genai
import osCC

# Replace with your Gemini API Key
genai.configure(api_key="AIzaSyAAP0lrg1QFSMsYCE6TQPaW6t0maX-2-Oc")

# Initialize the chatbot model
model = genai.GenerativeModel("gemini-2.5-flash")
chat_session = model.start_chat()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat_with_bot(message: str = Form(...)):
    response = chat_session.send_message(message)
    return JSONResponse(content={"response": response.text})
