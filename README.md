# Budge

## Quick Budgeting for Impulse Spenders

**API currently:**

creates user
authenticates user
authorizes user
retrieves all users

creates budget
connects budget to user.public_id
retrieves all budgets by user

### Init project

    Start pip virtual env: virtualenv venv

    Install pip requirememts: pip install -r requirements.txt (*note: make python-packages below also works)

    Source virtual env: source venv/bin/activate

### Terminal commands

    To clean excess files: make clean

    To install packages: make python-packages

    To run test: make tests

    To run application: make run

### Viewing the app

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/
