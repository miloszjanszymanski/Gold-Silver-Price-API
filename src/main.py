import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.gold_api_client import GoldAPIClient
from src.price_formatter import PriceFormatter
from config import Config

def main():
    try:
        Config.validate_config()
        
        client = GoldAPIClient()
        
        print("Getting current gold price...")
        data = client.get_gold_price()
        

        output = PriceFormatter.format_detailed(data)
        print(output)
        
    except ValueError as e:
        print(f"Configuration error: {e}")

        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()