
from fastapi import APIRouter, Depends
from app.deps.auth import get_current_user
import yfinance as yf
from random import choice

router = APIRouter(prefix="/ai", tags=["IA"])

@router.get("/recomendacion")
def recomendar(user = Depends(get_current_user)):
    tickers = ["AAPL", "TSLA", "NFLX", "MSFT", "GOOGL"]
    ticker = choice(tickers)
    t = yf.Ticker(ticker)
    hist = t.history(period="1d")
    precio = round(hist["Close"].iloc[-1], 2) if not hist.empty else 0.0
    return {
        "ticker": ticker,
        "motivo": "Selección basada en análisis del mercado y tendencia.",
        "precio_actual": precio,
        "recomendacion": "comprar" if precio > 0 else "esperar"
    }
