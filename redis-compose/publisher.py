from fastapi import FastAPI
from pydantic import BaseModel
import redis

app = FastAPI()

# Connect to Redis container
r = redis.Redis(host="redis", port=6379, decode_responses=True)

CHANNEL = "messages"

class Message(BaseModel):
    message: str

@app.post("/publish")
def publish_message(msg: Message):
    r.publish(CHANNEL, msg.message)
    return {"status": "Message published", "message": msg.message}