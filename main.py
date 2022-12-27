from fastapi import FastAPI
from user import controller as user_controller
from user import model as user_model
from config.database import engine, SessionLocal

app = FastAPI()

user_model.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def index():
    return {'message': 'Hello World'}


app.include_router(user_controller.router)
