import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from app.routes import users, results
from app.database import db
from app.routes.internal import add_data, setup, text
from app.routes.test import question
from app.routes.question_answer import question_answer

load_dotenv()

app = FastAPI()
app.include_router(users.router)
app.include_router(results.router)
app.include_router(text.router)
app.include_router(add_data.router)
app.include_router(setup.router)
app.include_router(question.router)
app.include_router(question_answer.router)


@app.on_event("startup")
def on_startup():
    db.create_db_and_tables()


if __name__ == "__main__":
    uvicorn.run("app.main:app", port=8080, reload=False, debug=True, access_log=False)