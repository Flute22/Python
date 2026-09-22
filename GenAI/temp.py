# agent.py
from PIL.Image import logger
import os
import datetime
import logging
# from dotenv import load_dotenv
import google.generativeai as genai

# load_dotenv()
# logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
# logger = logging.getLogger(__name__)

api_key = ''
# if not api_key:
#     raise EnvironmentError("GEMINI_API_KEY not set in .env")

genai.configure(api_key=api_key)

# --- Tools ---
def get_current_time() -> str:
    """Returns current date and time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate(expression: str) -> str:
    """Safely evaluates basic math expressions."""
    allowed = set("0123456789+-*/(). ")
    if not all(c in allowed for c in expression):
        return "Error: invalid characters in expression"
    try:
        return str(round(eval(expression), 4))
    except Exception as e:
        logger.warning(f"Calculate failed: {e}")
        return "Error: could not evaluate expression"

def web_search(query: str) -> str:
    """Placeholder — replace with real search API."""
    if not query or len(query) > 500:
        return "Error: invalid query"
    return f"[Search result for '{query}']"

# --- Model ---
model = genai.GenerativeModel(
    model_name=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
    tools=[get_current_time, calculate, web_search],
    system_instruction="You are a helpful daily life assistant. Use tools when needed."
)

def run_agent():
    chat = model.start_chat(enable_automatic_function_calling=True)
    logger.info("Agent started")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["quit", "exit"]:
                break
            if len(user_input) > 2000:
                print("Input too long. Keep it under 2000 characters.")
                continue

            response = chat.send_message(user_input)
            print(f"\nAgent: {response.text}\n")

        except KeyboardInterrupt:
            break
        except Exception as e:
            logger.error(f"Agent error: {e}")
            print("Something went wrong. Try again.")

if __name__ == "__main__":
    run_agent()