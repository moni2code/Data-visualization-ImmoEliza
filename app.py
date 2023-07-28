# Importing the necessary library
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

# Opening and loading the saved model
pickle_in = open("models/my_model.pkl", "rb")
predictor = pickle.load(pickle_in)

# Route to get the information about what the post expects
@app.get('/')
def get_info():
    '''Function to give information about what kind of data should be entered and in which format.'''
    return {"message": "To get the prediction of a house price, You have to enter the details of a house in json format with the following conditions",
           "postal code": "It should be of 4 digits zipcode inside of Belgium  "
           "subtype" : "Expected values : APARTMENT,HOUSE,VILLA,PENTHOUSE,DUPLEX,FLAT_STUDIO,GROUND_FLOOR,APARTMENT_BLOCK,MIXED_USE_BUILDING,EXCEPTIONAL_PROPERTY,MANSION,LOFT,TOWN_HOUSE,SERVICE_FLAT,BUNGALOW,COUNTRY_COTTAGE,TRIPLEX,CHALET,FARMHOUSE,MANOR_HOUSE,KOT,CASTLE",
           "bedroom_count" : "It should be an integer, number of bedrooms ",
           "habitable_surface" : "It should be in sq.m(area of livable space)",
           "kitchen_type" : "Expected values : INSTALLED,HYPER_EQUIPPED,SEMI_EQUIPPED,USA_HYPER_EQUIPPED,NOT_INSTALLED,USA_INSTALLED,USA_SEMI_EQUIPPED,USA_UNINSTALLED",
           "furnished" : "Expected values 1 for furnished and 0 for not_furnished",
           "fireplace" : "Expected values 1 for Yes and 0 for No",
           "terrace" : "Expected values 1 for Yes and 0 for No",
           "garden" : "Expected values 1 for Yes and 0 for No",
           "garden_surface" : "It should be in sq.m (area of garden surface)",
           "facades" : "It should be an integer, number of facades",
           "swimmingpool" : "Expected values 1 for Yes and 0 for No",
           "condition" : "Expected values : GOOD,AS_NEW,NOT_KNOWN,TO_BE_DONE_UP,TO_RENOVATE,JUST_RENOVATED,TO_RESTORE"
           }

# Route that receives the data
@app.post('/predict')

def prediction(input_data : HouseDetails):
    '''Function to get the data as parameter and converts it into a array for the prediction and returns the prediction. '''
    postalcode = input_data.postalcode
    subtype = input_data.subtype
    bedroom_count = input_data.bedroom_count
    habitable_surface = input_data.habitable_surface
    kitchen_type = input_data.kitchen_type
    furnished = input_data.furnished
    fireplace = input_data.fireplace
    terrace = input_data.terrace
    garden = input_data.garden
    garden_surface = input_data.garden_surface
    facades = input_data.facades
    swimmingpool = input_data.swimmingpool
    condition = input_data.condition

    predict_data = np.array([postalcode, subtype, bedroom_count, habitable_surface,
       kitchen_type, furnished, fireplace, terrace, garden,
       garden_surface, facades, swimmingpool, condition])
    y_predict = predictor.predict([predict_data])
    
    return {'Predicted_price': y_predict.tolist()}
    

