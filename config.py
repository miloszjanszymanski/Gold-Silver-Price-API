import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_BASE_URL = "https://api.gold-api.com"
    API_KEY = os.getenv("GOLD_API_KEY", "")
    GOLD_SYMBOL = "XAU"  
    CURRENCY = "PLN"  
    
    @classmethod
    def validate_config(cls):
 
        if not cls.API_KEY:
            raise ValueError("No API key found. Please set the GOLD_API_KEY environment variable.")