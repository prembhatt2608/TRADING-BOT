import streamlit as st
from bot.orders import OrderService
from bot.validators import validate

st.title("📈 Binance Futures Testnet Bot")

# Inputs
symbol = st.text_input("Symbol", "BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
quantity = st.number_input("Quantity", min_value=0.0, value=0.001)

price = None
if order_type == "LIMIT":
    price = st.number_input("Price", min_value=0.0, value=60000.0)

# Button
if st.button("Place Order"):
    try:
        validate(symbol, side, order_type, quantity, price)

        service = OrderService()
        result = service.place_order(
            symbol, side, order_type, quantity, price
        )

        st.subheader("📊 Order Summary")
        st.write({
            "Symbol": symbol,
            "Side": side,
            "Type": order_type,
            "Quantity": quantity,
            "Price": price
        })

        if result:
            st.success("✅ Order Placed Successfully")
            st.json(result)
        else:
            st.error("❌ Order Failed")

    except Exception as e:
        st.error(f"Validation Error: {e}")