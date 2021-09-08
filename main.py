from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from taxes import calculate_tax, ergazomenos_period_taxes, mikta_apo_kathara
from fastapi.responses import RedirectResponse


INFO = "Greek Tax Calculator"

description = """
## /tax

example: [https://tpcvju.deta.dev/tax?year=2020&income=870&kids=0](https://tpcvju.deta.dev/tax?year=2020&income=870&kids=0)

year: fiscal year

income: net income before taxes

kids: number of kids

## /taxper

example: [https://tpcvju.deta.dev/taxper?year=2021&income=600&kids=0&factor=28](https://tpcvju.deta.dev/taxper?year=2021&income=600&kids=0&factor=28)

year: fiscal year

income: monthly income

kids: number of kids

factor: normally 14 for monthly income otherwise 28


## /mikta

example: [https://tpcvju.deta.dev/mikta?year=2021&kathara=958.12](https://tpcvju.deta.dev/mikta?year=2021&kathara=958.12)

year: fiscal year

kathara: Amount payable

pefka: EFKA percentage for employee

kids: number of kids

"""

app = FastAPI(
    title="Greek Tax calculator(By Ted Lazaros)",
    description=description,
    version="0.0.4",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=RedirectResponse, include_in_schema=False)
async def main():
    return "https://tpcvju.deta.dev/docs"


@app.get("/tax")
async def get_tax(year: int, income: float, kids: int = 0):
    try:
        tax = calculate_tax(year, income, kids)
        return {"info": INFO, "data": tax, "message": "ok"}
    except NotImplementedError:
        return {
            "info": INFO,
            "data": {},
            "message": f"Calculation is not valid for year {year}",
        }


@app.get("/taxper")
async def get_taxper(year: int, income: float, kids: int = 0, factor: int = 14):
    try:
        tax = ergazomenos_period_taxes(year, income, kids, factor)
        return {"info": INFO, "data": tax, "message": "ok"}
    except NotImplementedError:
        return {
            "info": INFO,
            "data": {},
            "message": f"Calculation is not valid for year {year}",
        }


@app.get("/mikta")
async def get_mikta(year: int, kathara: float, pefka: float = 14.12, kids: int = 0):
    try:
        mikta = mikta_apo_kathara(year, kathara, pefka, kids)
        return {"info": INFO, "data": mikta, "message": "ok"}
    except NotImplementedError:
        return {
            "info": INFO,
            "data": {},
            "message": f"Calculation is not valid for year {year}",
        }
