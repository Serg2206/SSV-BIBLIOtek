from fastapi import FastAPI

# Создание экземпляра приложения FastAPI с метаданными
app = FastAPI(
    title="SSV-BIBKIOtek API",
    description=(
        "API для работы с библиотекой SSV-BIBKIOtek. "
        "Позволяет добавлять, удалять и искать книги. "
        "Документация автоматически создаётся и доступна через Swagger UI."
    ),
    version="1.0.0",
    contact={
        "name": "Сергей Сушков",
        "email": "sushkov@ssvnauka.com",
        "url": "https://ssvnauka.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    }
)

# Основной маршрут
@app.get("/", summary="Проверка статуса API", tags=["Status"])
def read_root():
    """
    Проверка состояния сервера.
    
    **Ответ:** JSON с сообщением, что API запущен.
    """
    return {"message": "SSV-BIBKIOtek API is running!"}


# Дополнительный маршрут для приветствия
@app.get("/hello/{name}", summary="Приветствие пользователя", tags=["Greetings"])
def say_hello(name: str):
    """
    Приветствует пользователя по имени.

    **Параметры:**
    - `name`: Имя пользователя.

    **Ответ:** JSON с приветственным сообщением.
    """
    return {"message": f"Привет, {name}!"}


# Пример маршрута для добавления данных
@app.post("/books/", summary="Добавление книги", tags=["Books"])
def create_book(book: dict):
    """
    Добавляет книгу в библиотеку.

    **Параметры:**
    - JSON с данными книги (название, автор, год).

    **Ответ:** JSON с подтверждением добавления книги.
    """
    return {"message": "Книга успешно добавлена", "book": book}


# Пример маршрута для получения списка книг
@app.get("/books/", summary="Получение списка книг", tags=["Books"])
def get_books():
    """
    Возвращает список всех книг в библиотеке.

    **Ответ:** JSON со списком книг.
    """
    return {"books": [
        {"title": "Мастер и Маргарита", "author": "М. Булгаков", "year": 1966},
        {"title": "Преступление и наказание", "author": "Ф. Достоевский", "year": 1866},
    ]}
