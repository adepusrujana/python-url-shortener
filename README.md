# URL Shortener API

A simple url shortener application built using FASTAPI,SQLALchemy,SQLite.

# Features
- Creates short URLs
- Generates unique short codes
- Store URLs in database
- REST APIs using FastAPI
- Interactive Sqagger documentation

# TechStack
- FastAPI
- SQL ALchemy
- SQLite
- Pydantic
- Uvicorn

# Project Structure

URL_SHORTNER/
--main.py
--database.py
--schemas.py
--models.py
--database.py
--routes.py
--urls.db
--requirements.txt

# Installation
### Clone the repository
'''bash
git clone  https://github.com/adepusrujana/python-url-shortener.git
cd python-url-shortener
'''

### Create vitual environment
'''bash
python -m venv venv
'''
### Activate virtual environment
'''bash
venv/Scripts/activate
'''

### Install Dependencies
'''bash
pip install -r requirements.txt
'''

# Run the application
'''bash
uvicorn main:app --reload --port 8001
'''
# API Documentation
http://127.0.0.1:8001/docs

# Author
Srujana

