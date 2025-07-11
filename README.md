# MiniVault API

A lightweight local REST API that simulates ModelVault's core feature of receiving prompts and returning generated responses. Built with FastAPI for high performance and modern Python development practices.


## Project Structure

```
minivault-api/
├── app.py                # Main API application
├── log.json             # Logs of prompt/response interactions
├── requirements.txt      # Python dependencies
└── README.md            # This documentation
```


## Features

* **POST /generate Endpoint**: Accepts a JSON payload `{"prompt": "..."}` and returns `{"response": "..."}`.
* **Local Logging**: All input prompts and generated responses are logged to `logs/log.jsonl` in JSON Lines format.
* **Stubbed Response**: For simplicity and to meet the core requirement within the time expectation, the API provides a hardcoded/dummy response. This can be easily extended to integrate a local LLM.
* **FastAPI**: Built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+.

## Setup Instructions

Follow these steps to get the MiniVault API up and running on your local machine.

### Prerequisites

* Python 3.7+ installed.

### Installation

1.  **Clone the repository (or create the files manually):**
    ```bash
    # If you're using Git
    git clone <your-repo-url>
    cd minivault-api
    ```
    If you're creating the files manually, ensure the directory structure matches the "Project Structure" above.

2.  **Create a Python Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **On Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate.bat
        ```
    * **On Windows (PowerShell):**
        ```bash
        venv\Scripts\Activate.ps1
        ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the API

1.  **Ensure your virtual environment is active.**
2.  **Run the FastAPI application:**
    ```bash
    python app.py
    ```
    You should see output indicating that Uvicorn is running, typically on `http://0.0.0.0:8000` or `http://127.0.0.1:8000`.

    ```
    INFO:     Uvicorn running on [http://0.0.0.0:8000](http://0.0.0.0:8000) (Press CTRL+C to quit)
    INFO:     Started reloader process [xxxxx]
    INFO:     Started server process [xxxxx]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```

The API is now running and ready to receive requests.

## Usage

You can interact with the API using tools like `curl`, Postman, Insomnia, or even a simple Python script.

### Example Request using `curl`

Open a new terminal window (keep the API running in the first one) and run the following `curl` command:

```bash
curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Tell me about ModelVault."}'




Expected Output
{
  "response": "ModelVault is a company focused on secure and efficient model deployment."
}

Example Request with a different prompt:
curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "What is the capital of France?"}'

Expected Output
{
  "response": "Thank you for your prompt: 'What is the capital of France?'. This is a stubbed response from MiniVault API."
}

Checking Logs
After making requests, you can view the logged interactions in logs/log.json:
cat logs/log.json

You will see output similar to this (each request will add a new line):
{"timestamp": "2025-07-10T19:08:12.345678", "input": {"prompt": "Tell me about ModelVault."}, "output": {"response": "ModelVault is a company focused on secure and efficient model deployment."}}
{"timestamp": "2025-07-10T19:08:30.987654", "input": {"prompt": "What is the capital of France?"}, "output": {"response": "Thank you for your prompt: 'What is the capital of France?'. This is a stubbed response from MiniVault API."}}

**Author:** Melanie Lobo
**Created:** July 2025
**Framework:** FastAPI + Python 3.8+