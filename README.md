# TODO List Project

This project is a simple TODO List application implemented in Python using the Flask web framework, with data persistence managed by PostgreSQL. It also utilizes Flask-Migrate for database migrations. The project emphasizes good architectural practices for maintainability and scalability.

## Tools Used

- Python
- Flask
- PostgreSQL
- Flask-Migrate

## Features

- Create, Read, Update, and Delete tasks in a TODO list.
- Data persistence using a PostgreSQL database.
- Efficient database migrations with Flask-Migrate.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/todo-list-project.git
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Setup the .env you can use the .env.example

4. Initialize the migrations setup
```
flask db init 
```
5. First migration
```
flask db migrate -m "First migration"
```
6. Only update the database, to start the project you only need this one
```
flask db upgrade
```
7. Run the application
```
python main.py
```

## Swagger
Open the default link and will take you to swagger, Also you can use Postman.
