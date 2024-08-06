### In progress
# Write2Me
Portfolio project app

## Stack
- Backend: FastAPI
- Frontend: React
- Mobile: Flutter
- Database: Sqlite

## Description
Write2Me is application dedicated to single personal websites for e.g. contact forms. Admin can add few lines of code and connect to my api. When user send message or contact request, Admin see notification on our platforms, and can see all requests/messages.

## Running
To run:
1. `pip install poetry`
2. `poetry install`
3. `poetry run uvicorn source.main:app`
4. Type in browser: `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/docs`

## PS
to clear used port:
1. `lsof -i :8000`
2. `kill <PID>` or `kill -9 <PID>`