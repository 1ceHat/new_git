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
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        # return users[user_id]
        for user in users:
            print(users)
            if user.id == user_id:
                return templates.TemplateResponse('users.html', {'request': request, 'user': user})
        else:
            raise IndexError
    except IndexError:
        return HTTPException(status_code=404, detail='User was not found')


@app.post('/users/{username}/{age}')
async def create_user(user: User):
    if users:
        user_id = max(users, key=lambda us: us.id).id+1
    else:
        user_id = 1
    user.id = user_id
    users.append(user)
    return f'User {user.id} is registered.'


@app.put('/users/{user_id}/{username}/{age}')
async def update_user(user: User):
    try:
        edit_user = users[user.id - 1]
        if edit_user.id == user.id:
            users[user.id-1].username = user.username
            users[user.id - 1].age = user.age
            return f'The user {user.id} is updated.'
        else:
            raise IndexError
    except IndexError:
        return HTTPException(status_code=404, detail='User was not found')


@app.delete('/users/{user_id}')
async def delete_user(user: User):
    try:
        edit_user = users[user.id - 1]
        if edit_user.id == user.id:
            users.pop(user.id - 1)
            return f'The user {user.id} is deleted.'
        else:
            raise IndexError
    except IndexError:
        return HTTPException(status_code=404, detail='User was not found')

@app.get('/')
async def user_request(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, "users": users})
