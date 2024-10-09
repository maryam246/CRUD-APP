# FastAPI MongoDB CRUD App

## Overview

This project provides a simple FastAPI CRUD (Create, Read, Update, Delete) API for task management, using MongoDB as the backend database. It supports creating new tasks, retrieving all tasks, updating existing tasks, and performing soft deletes (marking tasks as deleted without actually removing them).

## Features

- **Create Tasks:** Add a new task to the database.
- **Read Tasks:** Fetch all tasks that are not deleted.
- **Update Tasks:** Modify an existing task using its ID.
- **Delete Tasks:** Soft delete tasks by marking them as deleted.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/maryam246/CRUD-APP.git
cd fastapi-mongodb-crud
```

2. Create and Activate Virtual Environment (Optional)
```bash
python -m venv venv
```
```bash
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. Install Dependencies
Install all the required packages from requirements.txt using the following command:
```bash
pip install -r requirements.txt
```
4. Set Up MongoDB
Ensure you have MongoDB running locally or remotely (e.g., using MongoDB Atlas). You will need to set up the connection URI in the configuration.py file to connect the app with your MongoDB instance.

Running the Application
Start the FastAPI application by running:

```bash
uvicorn main:app --reload
```
Start the FastAPI server at 
```bash 
http://127.0.0.1:8000
```
