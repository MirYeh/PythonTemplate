"""docs:  http://127.0.0.1:8000/docs"""
import uvicorn
from fastapi import FastAPI

from template.ctrls import users


app = FastAPI()
app.include_router(users.router)


if __name__ == '__main__':
    uvicorn.run('main:app')
