from fastapi import FastAPI
from rps_game import play_rps
from guess_number import play_guess_number

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Games API!"}

@app.get("/rps/{choice}")
def play_rock_paper_scissors(choice: str):
    return {"result": play_rps(choice.lower())}

@app.get("/guess/{guess}")
def play_guess_the_number(guess: int):
    return {"result": play_guess_number(guess)}