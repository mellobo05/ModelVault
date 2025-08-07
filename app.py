import uvicorn
import json
import os
from datetime import datetime
from fastapi import FastAPI, Request
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(
    title="MiniVault API",
    description="A lightweight local REST API simulating ModelVault's prompt-response feature.",
    version="1.0.0"
)

# Define the request body model
class PromptRequest(BaseModel):
    prompt: str

# Define the response body model
class GenerateResponse(BaseModel):
    response: str

# --- Logging Configuration ---
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "log.json")

# Ensure the log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def log_interaction(input_data: dict, output_data: dict):
    """
    Logs input and output interactions to a JSON file.
    Each line in the file is a JSON object.
    """
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "input": input_data,
        "output": output_data
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    print(f"Logged interaction to {LOG_FILE}") # For debugging/confirmation

# --- API Endpoints ---

@app.post("/generate", response_model=GenerateResponse)
async def generate_response(request: Request, prompt_request: PromptRequest):
    """
    Receives a prompt and returns a generated response.
    Logs the input and output to 'logs/log.json'.
    """
    prompt = prompt_request.prompt
    print(f"Received prompt: '{prompt}'")

    # --- Simulate LLM Response (Stubbed) ---
    if "hello" in prompt.lower():
        generated_response = "Hello there! How can I assist you today?"
    elif "modelvault" in prompt.lower():
        generated_response = "ModelVault is a company focused on secure and efficient model deployment."
    else:
        generated_response = f"Thank you for your prompt: '{prompt}'. This is a stubbed response from MiniVault API."

    # Log the interaction
    log_interaction(
        input_data={"prompt": prompt},
        output_data={"response": generated_response}
    )

    return GenerateResponse(response=generated_response)

# --- Main entry point for running the Uvicorn server ---
if __name__ == "__main__":
    # You can run this file directly using `python app.py`
    # The host '0.0.0.0' makes it accessible externally (e.g., from Postman on your machine)
    # The port '8000' is standard for development.
    uvicorn.run(app, host="0.0.0.0", port=8000)
