from fastapi import FastAPI

# Создание экземпляра приложения FastAPI
app = FastAPI()

# Маршрут для проверки статуса API
@app.get("/")
def read_root():
    return {"message": "SSV-BIBKIOtek API is running!"}

# Маршрут для приветствия пользователя
@app.get("/hello/{name}")
def say_hello(name: str):
    """
    Возвращает приветствие пользователю.
    
    Параметры:
    - name: Имя пользователя.

    Возвращает:
    - JSON с приветствием.
    """
    return {"message": f"Привет, {name}!"}
