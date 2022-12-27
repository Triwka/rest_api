from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

data_base = {'22.12.2022': {'Расходы на еду': 12,
                            'Расходы на бензин': 13,
                            'Расходы на жкх': 15.6}}


class Stats(BaseModel):
    date: str
    food: float
    gas: float
    service: float


@app.post('/')
def add_new_stats(
        stats: Stats
):
    date = stats.date
    data_base[date] = {'Расходы на еду': stats.food,
                       'Расходы на бензин': stats.gas,
                       'Расходы на жкх': stats.service}
    return data_base[date]


@app.get('/')
def get_stats():
    return data_base


@app.get("/{date}")
def get_stat_by_date(
        date: str
):
    return data_base[date]


@app.put('/{date}')
def update_stats(date: str, stats: Stats):
    data_base[date]['Расходы на еду'] = data_base[date]['Расходы на еду'] + stats.food
    data_base[date]['Расходы на бензин'] = data_base[date]['Расходы на бензин'] + stats.gas
    data_base[date]['Расходы на жкх'] = data_base[date]['Расходы на жкх'] + stats.service
    return data_base[date]


@app.delete('/{date}')
def delete_stats(date: str):
    del data_base[date]
    return data_base
