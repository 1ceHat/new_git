from fastapi import FastAPI, Path, HTTPException, Request, Form, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='.\\')

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int = 20


@app.get('/users/{user_id}')
async def get_user(request: Request, user_id: int):
    try:
        # return users[user_id]
        for user in users:
            if user.id == user_id:
                return templates.TemplateResponse('users.html', {'request': request, 'user': user})
        else:
            raise IndexError
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')


@app.post('/users/{username}/{age}')
async def create_user(username: str, age: int):
    if users:
        user_id = max(users, key=lambda user: user.id).id+1
    else:
        user_id = 1
    created_user = User(id=user_id, username=username, age=age)
    users.append(created_user)
    return f'User {user_id} is registered.'


@app.put('/users/{user_id}/{username}/{age}')
async def update_user(user: User):
    try:
        for exist_user in users:
            if exist_user.id == user.id:
                exist_user.username = user.username
                exist_user.age = user.age
                return f'The user {user.id} is updated.'
        else:
            raise IndexError
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    try:
        for exist_user in users:
            if exist_user.id == user_id:
                index = users.index(exist_user)
                return f'The user {users.pop(index).id} was deleted.'
        else:
            raise IndexError
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')


@app.get('/users')
async def user_request(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, "users": users})
