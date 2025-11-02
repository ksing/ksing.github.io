import air

app = air.Air()

@app.get("/")
async def index():
    return air.Html(air.H1("Hello, world!", style="color: blue;"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
