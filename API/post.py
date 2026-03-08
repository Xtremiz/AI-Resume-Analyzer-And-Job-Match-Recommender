from fastapi import FastAPI
import API.pclass as p1
import requests

app = FastAPI()

@app.get("/")
def view():
    return {"message":"hello"}

@app.post("/post-to-webhook")
async def put(text: p1.Text_Input):

    url = "https://fozanahmed.app.n8n.cloud/webhook/frist_project"

    try:
        responce = requests.post(url, json={
            "text": text.text,
            "email": text.email})


        return responce.json()[0]['text']


    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }