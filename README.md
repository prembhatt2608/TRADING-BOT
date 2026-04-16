# 🚀 Binance Futures Testnet Trading Bot

A lightweight Python trading bot that places orders on Binance Futures Testnet (USDT-M).
Built with clean architecture, CLI support, logging, and optional UI.

---

## ✨ Features

* ✅ Place MARKET and LIMIT orders
* ✅ Supports BUY and SELL
* ✅ CLI-based input using argparse
* ✅ Input validation with clear error messages
* ✅ Structured code (client, orders, validators)
* ✅ Logging of API requests, responses, and errors
* ✅ Optional Streamlit UI for easy interaction

---

## 🛠 Tech Stack

* Python 3.x
* requests
* python-dotenv
* argparse
* Streamlit (optional)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add API Keys

Create a `.env` file:

```
API_KEY=your_api_key
API_SECRET=your_secret_key
BASE_URL=https://testnet.binancefuture.com
```

---

## ▶️ Usage

### 🔹 Market Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### 🔹 Limit Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## 🖥 Optional UI

Run Streamlit UI:

```
streamlit run ui.py
```

---

## 📊 Output

* Displays order summary
* Shows order response:

  * orderId
  * status
  * executedQty
* Prints success/failure message

---

## 🧾 Logging

All logs are stored in:

```
bot.log
```

Includes:

* API request data
* API responses
* Errors and exceptions

---

## ⚠️ Assumptions

* Binance Futures Testnet account is active
* API keys are valid
* Testnet wallet has sufficient USDT balance

---

## 📁 Project Structure

```
trading_bot/
│── bot/
│   │── client.py
│   │── orders.py
│   │── validators.py
│   │── logging_config.py
│
│── cli.py
│── ui.py (optional)
│── .env
│── requirements.txt
│── README.md
```

---

## 🚀 Future Improvements

* Stop-Limit / Advanced order types
* Real-time price fetching
* Order history tracking
* Deployment on cloud

---

## 👨‍💻 Author

Prem Bhatt

---
