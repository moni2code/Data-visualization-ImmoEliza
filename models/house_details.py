from pydantic import BaseModel

# Class with required values for the prediction
'''['postalcode', 'subtype', 'price', 'bedroom_count', 'habitable_surface',
       'kitchen_type', 'furnished', 'fireplace', 'terrace', 'garden',
       'garden_surface', 'facades', 'swimmingpool', 'condition']'''
class HouseDetails(BaseModel):
    postalcode : str
    subtype : str
    bedroom_count : float
    habitable_surface : float
    kitchen_type : str
    furnished : int
    fireplace :int
    terrace: int
    garden: int
    garden_surface : float
    facades : float
    swimmingpool : int
    condition : str
