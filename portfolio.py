
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps.auth import get_current_user, get_db
from app.models.inversion import Inversion
import yfinance as yf

router = APIRouter(prefix="/portfolio", tags=["Portafolio"])

@router.get("/")
def portafolio(db: Session = Depends(get_db), user = Depends(get_current_user)):
    inversiones = db.query(Inversion).filter(Inversion.user_id == user.id).all()

    portafolio = {}
    for inv in inversiones:
        if inv.ticker not in portafolio:
            portafolio[inv.ticker] = 0
        portafolio[inv.ticker] += inv.monto

    acciones = []
    total_invertido = 0
    total_valor_actual = 0

    for ticker, monto in portafolio.items():
        t = yf.Ticker(ticker)
        precio_actual = t.history(period="1d")["Close"]
        simulador = precio_actual.iloc[-1] if not precio_actual.empty else monto * 1.05
        valor_actual = simulador
        acciones.append({
            "ticker": ticker,
            "monto": round(monto, 2),
            "valor_actual": round(valor_actual, 2)
        })
        total_invertido += monto
        total_valor_actual += valor_actual

    rentabilidad = ((total_valor_actual - total_invertido) / total_invertido * 100) if total_invertido else 0

    return {
        "total_invertido": round(total_invertido, 2),
        "valor_actual": round(total_valor_actual, 2),
        "rentabilidad": round(rentabilidad, 2),
        "acciones": acciones
    }
