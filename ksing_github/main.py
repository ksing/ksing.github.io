import air

app = air.Air()


@app.get("/")
async def index() -> None:
    return air.Html(air.H1("This is Kush's personal page!"))
