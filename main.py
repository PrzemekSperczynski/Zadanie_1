import secrets
from typing import Union

from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from image_inverse import image_router
from liczby_pierwsze import prime_router

app = FastAPI()
app.include_router(image_router)
app.include_router(prime_router)

bezpieczenstwo = HTTPBasic()

def obecny_uzytkownik(credentials: HTTPBasicCredentials = Depends(bezpieczenstwo)):
    bity_obecnego_uzytkownika = credentials.username.encode("utf8")
    bity_poprawnego_uzytkownika = b"informatyka"
    poprawny_uzytkownik = secrets.compare_digest(
        bity_obecnego_uzytkownika, bity_poprawnego_uzytkownika
    )
    bity_obecnego_hasla = credentials.username.encode("utf8")
    bity_poprawnego_hasla = b"informatyka"
    poprawne_haslo = secrets.compare_digest(
        bity_obecnego_hasla, bity_poprawnego_hasla
    )

    if not (poprawny_uzytkownik and poprawne_haslo):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORISED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/")
def read_current_user(credentials: HTTPBasicCredentials = Depends(bezpieczenstwo)):
    return datetime.now().strftime('%H:%M:%S')