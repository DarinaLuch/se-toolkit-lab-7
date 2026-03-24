import os
from pathlib import Path

class BotConfig:
    """Bot configuration from environment variables."""
    
    def __init__(self):
        # Load from .env.bot.secret file
        env_file = Path(__file__).parent / ".env.bot.secret"
        if env_file.exists():
            with open(env_file) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        key, value = line.split('=', 1)
                        os.environ[key] = value
        
        self.bot_token = os.getenv("BOT_TOKEN", "")
        self.lms_api_base_url = os.getenv("LMS_API_BASE_URL", "http://localhost:42002")
        self.lms_api_key = os.getenv("LMS_API_KEY", "")
        self.llm_api_key = os.getenv("LLM_API_KEY", "")
        self.llm_api_base_url = os.getenv("LLM_API_BASE_URL", "http://localhost:42005/v1")
        self.llm_api_model = os.getenv("LLM_API_MODEL", "coder-model")

def load_config():
    return BotConfig()
