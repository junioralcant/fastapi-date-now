from distutils.log import debug
from fastapi import FastAPI
from datetime import date, datetime
from pytz import timezone

app = FastAPI()


def now():

    dateNow = datetime.now()

    dateBrasil = timezone("America/Sao_Paulo")

    date = dateNow.astimezone(dateBrasil)

    dateFormatted = date.strftime("%d/%m/%Y %H:%M:%S")

    return dateFormatted


@app.get('/')
def home():
    return {"date": now()}


if __name__ == "__main__":
    app.run(debug=True)
