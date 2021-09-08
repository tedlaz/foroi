from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from taxes import calculate_tax, ergazomenos_period_taxes, mikta_apo_kathara

description = """
api για να κάνετε υπολογίσετε φόρους

## /tax

example: /tax?year=2021&income=6000&kids=0

year: Φορολογικό Έτος

income: Καθαρό ετήσιο εισόδημα για φορολόγηση

kids: Αριθμός παιδιών

## Ειδικότητες

Μπορείτε να αναζητήσετε ειδικότητες εργαζομένων

"""

app = FastAPI(
    title="Greek Taxes calculator(By Ted Lazaros)",
    description=description,
    version="0.0.3",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/tax")
async def get_tax(year: int, income: float, kids: int = 0):
    try:
        taxes = calculate_tax(year, income, kids)
        return taxes
    except NotImplementedError:
        return {"message": f"Calculation is not valid for year {year}"}


@app.get("/taxper")
async def get_taxper(year: int, income: float, kids: int = 0, factor: int = 14):
    try:
        taxes = ergazomenos_period_taxes(year, income, kids, factor)
        return taxes
    except NotImplementedError:
        return {"message": f"Calculation is not valid for year {year}"}


@app.get("/mikta")
async def get_mikta(year: int, kathara: float, pefka: float = 14.12, kids: int = 0):
    try:
        mikta = mikta_apo_kathara(year, kathara, pefka, kids)
        return mikta
    except NotImplementedError:
        return {"message": f"Calculation is not valid for year {year}"}
