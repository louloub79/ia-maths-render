from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def repondre(question: str) -> str:
    q = question.lower()

    if "pythagore" in q:
        return "Dans un triangle rectangle : hypotenuse² = côté1² + côté2²."
    if "thalès" in q or "thales" in q:
        return "Thalès : si deux droites sont parallèles, les longueurs correspondantes sont proportionnelles."
    if "fraction" in q:
        return "Addition : même dénominateur. Multiplication : numérateur×numérateur et dénominateur×dénominateur."
    if "équation" in q or "equation" in q:
        return "Équation ax + b = c : on isole x → x = (c - b) / a."
    if "proportionnalité" in q:
        return "Proportionnalité : on multiplie ou divise par le même nombre."
    if "statistique" in q or "moyenne" in q:
        return "Moyenne = somme des valeurs / nombre de valeurs."
    if "probabilité" in q:
        return "Probabilité = cas favorables / cas possibles."
    if "fonction" in q:
        return "Une fonction associe à x un nombre f(x). Exemple : f(x)=2x+3."

    return "Je ne connais pas encore ce chapitre. Essaie de préciser ta question."

@app.get("/ask")
def ask(q: str):
    return {"reponse": repondre(q)}
