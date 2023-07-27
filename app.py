from fastapi import FastAPI
import uvicorn
from models.house_details import HouseDetails
import pickle
import pandas as pd
import numpy as np
import json
from pydantic import BaseModel

# create the object app
app = FastAPI()
pickle_in = open("models/my_model.pkl", "rb")
predictor = pickle.load(pickle_in)

@app.get('/')
def get_info():
    return {"message": "You have to enter the details of a house in json format"}

@app.post('/predict')
def prediction(input_data : HouseDetails):
    input_data = json.loads(input_data.model_dump_json())
    postalcode = input_data['postalcode']
    subtype = input_data['subtype']
    region = input_data['region']
    district = input_data['district']
    province = input_data['province']
    bedroom_count = input_data['bedroom_count']
    habitable_surface = input_data['habitable_surface']
    terrace = input_data['terrace']
    facades = input_data['facades']

    predict_data = np.array[postalcode, subtype, region, district, province, bedroom_count, habitable_surface, terrace, facades]
    y_predict = predictor.predict(predict_data)
    #print(prediction)
    return {'Predicted_price': y_predict}
    

'''if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)'''