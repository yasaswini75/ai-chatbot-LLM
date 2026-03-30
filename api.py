from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_response
from prompts import zero_shot, few_shot

app = FastAPI()

class RequestBody(BaseModel):
    message: str
    mode: str = "zero"

@app.post("/chat")
def chat(req: RequestBody):

    if req.mode == "compare":
        zero_prompt = zero_shot(req.message)
        few_prompt = few_shot(req.message)

        zero_reply = get_response(zero_prompt)
        few_reply = get_response(few_prompt)

        return {
            "input": req.message,
            "mode": "compare",
            "zero_shot": zero_reply,
            "few_shot": few_reply
        }

    elif req.mode == "few":
        prompt = few_shot(req.message)
    else:
        prompt = zero_shot(req.message)

    reply = get_response(prompt)

    return {
        "input": req.message,
        "mode": req.mode,
        "response": reply
    }