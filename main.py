from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"FIO": "Клюев Александр Алексеевич"}


@app.get("/users")
async def data():
    return {"Email": "klyev.alex.02@gmail.com", "Phone number": "+79994756247"}


@app.get("/tools")
async def skills():
    return {"Skills": {"C#", "SQL", "Python", "Postgresql"}}
