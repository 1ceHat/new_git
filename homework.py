from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Examples, возраст: 18'}


@app.get('/users')
async def get_all_users():
    return users


@app.post('/users/{username}/{age}')
async def create_user(username: str, age: int):
    curr_id = str(int(max(users, key=int))+1)
    users[curr_id] = f'Имя: {username}, возраст: {age}'
    return f'User {curr_id} is registered.'


@app.put('/users/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int):
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated.'


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    users.pop(str(user_id))
    return f'The user {user_id} is deleted.'
