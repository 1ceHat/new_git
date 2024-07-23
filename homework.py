from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main_page():
    return 'Главная страница'

@app.get('/user/admin')
async def admin_page():
    return 'Привет, администратор!'

@app.get('/user/{user_id}')
async def user_pages(user_id: int):
    return f'Привет, пользователь номер {user_id}!'

@app.get('/user')
async def user_name_page(user_name: str = 'Artem', user_age: int = 20):
    return f'Информация о пользователе\nИмя: {user_name},  возраст: {user_age}'
