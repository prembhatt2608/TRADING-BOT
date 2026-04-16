from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger()

class OrderService:
    def __init__(self):
        self.client = BinanceClient()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        try:
            logger.info(f"Request: {params}")
            res = self.client.send_request(
                "POST",
                "/fapi/v1/order",
                params
            )
            logger.info(f"Response: {res}")
            return res

        except Exception as e:
            logger.error(f"Error: {e}")
            return None