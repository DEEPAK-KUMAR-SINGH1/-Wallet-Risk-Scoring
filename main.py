from fastapi import FastAPI, Query
from typing import List
from random import randint
from pydantic import BaseModel
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import fetch_transactions, extract_features, score_wallet

app = FastAPI(title="Wallet Scoring API")

@app.get("/")
def home():
    return {"message": "Welcome to the Wallet Scoring System"}


@app.get("/wallets", response_model=List[str])
def get_wallets():
    with open("wallets.txt", "r") as file:
        wallets = [line.strip() for line in file if line.strip()]
    return wallets


@app.get("/score")
def get_wallet_score(address: str = Query(...)):
    score = randint(0, 1000)
    return {"wallet": address, "score": score}


class WalletRequest(BaseModel):
    address: str

@app.post("/value")
def post_wallet_score(wallet: WalletRequest):
    value = randint(0, 1000)
    return {"wallet": wallet.address, "value": value}