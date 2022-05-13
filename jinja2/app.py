from fastapi import templating
from starlette.responses import Response
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import  Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/')
def hello_world():
    return { 'message' : 'hello'}

    @app.get("/items/{id}", response_class=HTMLResponse)
    async def read_item(request: Response, id: str):
        return templates.TemplateResponse("item.html", {"request": request, "id": id})

    if __name__ == '__main__':
        uvicorn.run(app)

