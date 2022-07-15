from distutils.log import debug
from fastapi import FastAPI
from datetime import datetime
from pytz import timezone

app = FastAPI()

dateNow = datetime.now()

dateBrasil = timezone("America/Sao_Paulo")

date = dateNow.astimezone(dateBrasil)

dateFormatted = date.strftime("%d/%m/%Y %H:%M:%S")


@app.get('/')
def home():
    return {"date": dateFormatted}


if __name__ == "__main__":
    app.run(debug=True)
