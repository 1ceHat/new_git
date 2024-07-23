from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/users')
async def get_all_users():
    return users


@app.post('/users/{username}/{age}')
async def create_user(user: User):
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
