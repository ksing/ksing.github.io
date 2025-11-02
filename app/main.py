from pathlib import Path
from fastapi.applications import FastAPI
import air

app = air.Air()
templates_dir = Path(__file__).parent / "templates"
jinja = air.JinjaRenderer(directory=templates_dir)
api = FastAPI()


@app.get("/")
async def index(request: air.Request) -> None:
    return jinja(request, "index.html")


@api.get("/")
async def api_root():
    return {"message": "Awesome SaaS is powered by FastAPI"}


app.mount("/api", api)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
