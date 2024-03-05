from fastapi import FastAPI
from g4f.client import Client

app = FastAPI()


@app.get("/")
def root():
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Привет, расскажи анекдот."}]
    )
    return {"message": "Hello, Denis"}
    # return {"message": response.choices[0].message.content}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
