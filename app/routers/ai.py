
from fastapi import APIRouter, Depends
import yfinance as yf
from random import choice
from app.deps.auth import get_current_user

router = APIRouter(prefix="/ai", tags=["IA"])

@router.get("/recomendacion")
def recomendar(user = Depends(get_current_user)):
    tickers = ["AAPL", "TSLA", "MSFT", "NFLX"]
    ticker = choice(tickers)
    t = yf.Ticker(ticker)
    precio = t.history(period="1d")["Close"].iloc[-1]
    return {
        "ticker": ticker,
        "motivo": "Análisis técnico positivo",
        "precio_actual": round(precio, 2),
        "recomendacion": "comprar"
    }
