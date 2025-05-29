from fastapi import FastAPI
from app.routers import auth, user, ai, invest, history, portfolio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(ai.router)
app.include_router(invest.router)
app.include_router(history.router)
app.include_router(portfolio.router)

@app.get("/")
def root():
    return {"message": "InvestAI backend is running"}