# Airline Data Query Platform (ADQP)

## Airline Project - Database Management

The Airline Data Query Platform (ADQP) aims to build an advanced query system that enables analysts to easily retrieve and analyze U.S. domestic airline ticket data from the DB1B dataset.

### Features:
- A web-based front-end (ReactJS),
- A back-end powered by Hive and Spark for efficient data processing,
- Integration with Large Language Models (LLMs) for natural language queries,
- Robust data visualization tools.

### Target Users:
- Data analysts
- Airline companies
- Research institutions focusing on transportation data

ADQP is a Django-based web application with Spark (distributed data processing engine), designed to provide a user-friendly interface for querying and analyzing U.S. domestic airline ticket data from the DB1B dataset. It features a powerful query engine and a visualization engine that enables users to create interactive charts and graphs. The app is containerized using Docker, making it easy to deploy and scale. The app will be deployed on K8s with CI/CD for scalability and reliability.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Git installed.
- Docker installed.

## Installing ADQP

1. **Dev container**
    - Clone the repository
    - Open the project in VSCode
    - Install Dev Container extension from the marketplace
    - Shift-command-p, and click on the "Reopen and rebuild in Container" button to open the project in a dev container
    - The dev container will install all the required dependencies and set up the environment for you

2. **Inside the environment we created, create a virtual environment**:
    ```bash
    python3.11 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the Spark**:
    - Run the ingest_data.py script to ingest the data, the program will download and extract the data from the source and ingest it into the Spark cluster.
   ```bash
    python3.11 ingest_data.py
    ```
   
5. **Run the application**:
    ```bash
    python3.11 manage.py runserver
    ```
   
6. **Test the api (this is an example, you can modify the query to whatever you want)**:
    ```bash
    curl -X POST http://127.0.0.1:8000/adqp/api/query/      -H "Content-Type: application/json"      -d '{"query": "SELECT * FROM db1b.market WHERE ItinGeoType=2 LIMIT 100"}'
    ```



## API Endpoints

- **/adqp/api/query/**
    - **POST**: Send a SQL query to the server to retrieve data from the Spark.
    - **Request Body**: 
        ```json
        {
            "query": "SELECT * FROM db1b.market WHERE ItinGeoType=2 LIMIT 100"
        }
        ```




## TODO
- [X] Spark integration instead of PostgreSQL
- [] CSV file download feature
- [] User input validation
- [] LLMs integration



