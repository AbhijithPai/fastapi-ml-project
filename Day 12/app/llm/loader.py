from ctransformers import AutoModelForCausalLM
from app.utils.logger import get_logging

logger = get_logging("llm-loader")

_llm = None

def load_llm():
    global _llm
    if _llm is None:
        logger.info("Loading Qwen 0.5B (public, no auth)...")

        _llm = AutoModelForCausalLM.from_pretrained(
            "Qwen/Qwen1.5-0.5B-Chat-GGUF",
            model_file="qwen1_5-0_5b-chat-q4_k_m.gguf",
            model_type="qwen"
        )

    return _llm
