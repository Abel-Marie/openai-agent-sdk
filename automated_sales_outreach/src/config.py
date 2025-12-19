import os
from dotenv import load_dotenv

# 1. Force reload environment variables
load_dotenv(override=True)

# 2. Verify Keys exist before running
if not os.getenv("BREVO_API_KEY"):
    raise ValueError("Missing BREVO_API_KEY in .env file")

# Handle GOOGLE_API_KEY / GEMINI_API_KEY mismatch fallback
if not os.getenv("GEMINI_API_KEY") and os.getenv("GOOGLE_API_KEY"):
    os.environ["GEMINI_API_KEY"] = os.environ["GOOGLE_API_KEY"]

if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("Missing GEMINI_API_KEY (or GOOGLE_API_KEY) in .env file")

# The API key will be automatically picked up by LiteLLM / Agent SDK
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
# Optional: Raise error if OpenRouter key is strictly required for the free models
# if not OPENROUTER_API_KEY:
#     raise ValueError("OPENROUTER_API_KEY not found in environment variables")

# --- Configuration ---
# UPDATE THIS to your verified Brevo sender
SENDER_EMAIL = {"email": "abelmarie49@gmail.com", "name": "Abel Marie"} 
RECIPIENT_EMAIL = [{"email": "birukabere4@gmail.com", "name": "Dick Head"}]

# FREE MODELS (AUTO FALLBACK)
# -------------------------------------------------
FREE_MODELS = [
    "litellm/openrouter/meta-llama/llama-3.2-3b-instruct:free",
    "litellm/openrouter/mistralai/mistral-7b-instruct:free",
    "litellm/openrouter/tngtech/deepseek-r1t2-chimera:free",
    "litellm/openrouter/meta-llama/llama-3.3-70b-instruct:free",
    "litellm/openrouter/nousresearch/hermes-3-llama-3.1-405b:free",
]
