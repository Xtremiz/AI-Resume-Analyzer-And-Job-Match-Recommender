from fastapi import FastAPI
import API.pclass as p1
import requests
app = FastAPI()
@app.get("/")
def view():
  return {"message":"hello"}

@app.post("/post-to-webhook")
def put(text :p1.Text_Input):
   url = "https://fozanahmed.app.n8n.cloud/webhook/e3f2d2aa-33c5-4913-8da6-6a53050df43b"
   try:
    responce = requests.post(url,json={
      "text":text.text,"email":text.email
    })
    return {
      "status":"success"
    }
   except Exception as e:
     return {
       "status":"error",
       "message":str(e)
     }