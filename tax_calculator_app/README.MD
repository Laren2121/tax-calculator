# Tax Calculator Application - Points

This project is a simple Flask application that calculates income tax based on a given salary and tax year. The application uses an external Dockerized API to fetch tax bracket data and then performs the tax calculation using core business logic.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your system.
- [Python 3](https://www.python.org/downloads/) installed.
- [Git](https://git-scm.com/downloads) (optional, for cloning the repository).

## Setup and Running the Application

### Step 1: Run the Dockerized API

First, pull and run the Docker image that serves as the backend API.

```bash
docker pull ptsdocker16/interview-test-server
docker run --init -p 5001:5001 -it ptsdocker16/interview-test-server
```

### Step 2: Install dependencies

```
(Optional if using virtual env)
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

```
pip install -r requirements.txt
```

### Step 3 : Run the application
python3 app.py

### Step 4 : Test the application

```
curl "http://localhost:5002/api/calculate-tax?salary=50000&tax_year=2022"
```
