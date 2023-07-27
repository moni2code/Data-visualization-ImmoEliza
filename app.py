from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def get_info():
    return {"message": "You have to enter the details of a house in json format"}

#@app.post('/predict')
#def prediction(input_data : HouseDetail)