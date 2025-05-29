
from fastapi import FastAPI
from app.routers import ai, invest, auth, user, history, portfolio

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(ai.router)
app.include_router(invest.router)
app.include_router(history.router)
app.include_router(portfolio.router)

@app.get("/")
def root():
    return {"message": "InvestAI backend is running"}
