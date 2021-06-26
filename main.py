import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import quotes, index

app = FastAPI()


def configure():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(quotes.router)
    app.include_router(index.router)


configure()

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
