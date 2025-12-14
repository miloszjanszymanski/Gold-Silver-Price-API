from typing import Dict, Any
from datetime import datetime

class PriceFormatter:
    
    @staticmethod
    def format_price(data: Dict[str, Any]) -> str:
        if not data:
            return "No data"
            
        price = data.get('price', 0)
        timestamp = data.get('timestamp', 0)
        symbol = data.get('symbol', 'XAU')
        currency = data.get('currency', '')
        
        formatted_price = f"{price:,.2f}".replace(",", " ").replace(".", ",")
        
        if timestamp:
            date_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        else:
            date_str = "Unknown data"
        
        return f"Gold price ({symbol}): {formatted_price} {currency} (as of {date_str})"
    
    @staticmethod
    def format_detailed(data: Dict[str, Any]) -> str:
        lines = [
            "=" * 50,
            "CURRENT GOLD PRICE",
            "=" * 50
        ]
        
        fields = [
            ("Symbol", data.get('symbol', 'N/A')),
            ("Price", f"{data.get('price', 0):,.2f}"),
            ("Currency", data.get('currency', 'N/A')),
            ("Update date", datetime.fromtimestamp(
                data.get('timestamp', 0)
            ).strftime("%Y-%m-%d %H:%M:%S") if data.get('timestamp') else 'N/A'),
        ]
        
        for label, value in fields:
            lines.append(f"{label:20}: {value}")
        
        lines.append("=" * 50)
        
        return "\n".join(lines)