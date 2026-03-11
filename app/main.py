import logging
import uuid
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import vertexai
from vertexai.generative_models import GenerativeModel
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Initialize Vertex AI
vertexai.init(project="ai-infra-lab-487819", location="us-central1")
model = None

@app.on_event("startup")
def startup():
    global model
    model = GenerativeModel("gemini-2.0-flash")
    logger.info("Vertex AI model initialized")

class ChatRequest(BaseModel):
    prompt: str

    @classmethod
    def validate_prompt(cls, value):
        if len(value) == 0:
            raise ValueError("Prompt cannot be empty")
        return value

        if len(value) > 5000:
            raise ValueError("Prompt exceeds maximum length of 5000 characters")
        return value


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat")
def chat(request: ChatRequest):
    request_id = str(uuid.uuid4())
    start_time = time.time()

    logger.info(f"Request ID: {request_id} - Prompt received")

    try:
        response = model.generate_content(
            request.prompt,
            generation_config={
                "max_output_tokens": 512
            }
        )
        duration = round(time.time() - start_time, 3)

        logger.info(f"Request ID: {request_id} - Response generated in {duration} seconds")

        return {
            "request_id": request_id,
            "duration_seconds": duration,
            "response": response.text
        }

    except Exception as e:
        logger.error(f"Request ID: {request_id} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Model inference failed")
