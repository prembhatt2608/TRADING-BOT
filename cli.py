import argparse
from bot.orders import OrderService
from bot.validators import validate

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate(args.symbol, args.side, args.type, args.quantity, args.price)
    except Exception as e:
        print(f"❌ Validation Error: {e}")
        return

    service = OrderService()
    result = service.place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\n===== ORDER SUMMARY =====")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")
    print(f"Price: {args.price}")

    if result:
        print("\n✅ SUCCESS")
        print(f"Order ID: {result.get('orderId')}")
        print(f"Status: {result.get('status')}")
        print(f"Executed Qty: {result.get('executedQty')}")
    else:
        print("\n❌ FAILED")

if __name__ == "__main__":
    main()