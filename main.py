from distutils.log import debug
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

dateNow = datetime.now();

dateFormatted = dateNow.strftime("%d/%m/%Y %H:%M:%S")

@app.get('/')
def home():
    return {"date": dateFormatted} 

if __name__ == "__main__": 
    app.run(debug=True)    
