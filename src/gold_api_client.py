import requests
from typing import Dict, Optional, Any
from config import Config

class GoldAPIClient:
    """Klient do komunikacji z Gold API"""
    
    def __init__(self, api_key: str = None, currency: str = None):
        self.api_key = api_key or Config.API_KEY
        self.currency = currency or Config.CURRENCY
        self.base_url = Config.API_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "x-access-token": self.api_key,
            "User-Agent": "GoldPriceTracker/1.0"
        })
        
    def get_gold_price(self, symbol: str = None) -> Dict[str, Any]:
        symbol = symbol or Config.GOLD_SYMBOL
        
        try:
            url = f"{self.base_url}/price/{symbol}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if "error" in data:
                raise ValueError(f"Błąd API: {data.get('error')}")
                
            return data
            
        except requests.exceptions.Timeout:
            raise requests.exceptions.RequestException("Przekroczono czas oczekiwania")
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.RequestException("Błąd połączenia z API")
    
    def test_connection(self) -> bool:
        try:
            self.get_gold_price()
            return True
        except:
            return False