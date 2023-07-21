from fastapi import FastAPI
from Posts import postList

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts/{id}")
async def rootTeste(id: int):
    p = postList[id]
    return {"id": f"{id}", "title": f"{p.title}", "body": f"{p.body}","userId":f"{p.userId}" }

@app.get("/posts")
async def rootTeste(id: int = -1):
    pId = 1
    if id == -1:
        posts = []
        for post in postList:
            posts.append({"id": f"{pId}", "title": f"{post.title}", "body": f"{post.body}", "userId": f"{post.userId}"})
            pId += 1
        return posts

    p = postList[id]
    return {"id": f"{id}", "title": f"{p.title}", "body": f"{p.body}","userId":f"{p.userId}" }
