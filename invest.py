
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps.auth import get_current_user, get_db
from app.models.inversion import Inversion
from app.schemas.inversion import InversionIn

router = APIRouter(prefix="/invest", tags=["Inversiones"])

@router.post("/")
def invertir(data: InversionIn, db: Session = Depends(get_db), user = Depends(get_current_user)):
    nueva = Inversion(
        ticker=data.ticker.upper(),
        monto=data.monto,
        user_id=user.id
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return {"msg": f"Inversión en {nueva.ticker} registrada por ${nueva.monto:.2f}"}
