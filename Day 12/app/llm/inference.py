import time
from app.llm.loader import load_llm
from app.llm.prompts import SENTIMENT_PROMPT_V1
from app.utils.logger import get_logging

logger = get_logging("llm-inference")

def run_inference(text: str):
    llm =  load_llm()

    prompt = SENTIMENT_PROMPT_V1.format(text=text)

    start = time.time()
    response = llm(
        prompt,
        max_new_tokens = 30,
        temperature = 0.0   
    )
    latency = time.time() - start

    logger.info({
        "prompt version": "v1",
        "latency": latency,
        "response": response
    })

    return response
