from fastapi import File, APIRouter
from fastapi.responses import StreamingResponse

prime_router = APIRouter()

@prime_router.post("/prime")

def prime():
    num = int(input("Jaka liczbe chcesz przetestowac by sprawdzic czy jest liczba pierwsza? "))

    if num > 9223372036854775807:

        return("Twoja cyfra jest zbyt wysoka do sprawdzenia")


    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return ("Twoja cyfra nie jest liczbą pierwszą")

        else:
            return (num, " jest cyfrą pierwszą")

    else:
        return ("Twoja cyfra nie jest liczbą pierwszą")
