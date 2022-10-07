from fastapi import FastAPI

app = FastAPI(docs_url="/")


@app.get("/infer")
async def infer(input_text: str):

    arr = []
    for i in range(1000000):
        a = 10
        if i%100==0:
            arr.append(a)

    return {"output": input_text}