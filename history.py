
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps.auth import get_current_user, get_db
from app.models.inversion import Inversion

router = APIRouter(prefix="/history", tags=["Historial"])

@router.get("/")
def historial(db: Session = Depends(get_db), user = Depends(get_current_user)):
    inversiones = db.query(Inversion).filter(Inversion.user_id == user.id).order_by(Inversion.fecha.desc()).all()
    return [
        {
            "ticker": inv.ticker,
            "monto": inv.monto,
            "fecha": inv.fecha.isoformat()
        }
        for inv in inversiones
    ]
