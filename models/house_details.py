from pydantic import BaseModel

# Class with required values for the prediction
'''['postalcode', 'subtype', 'region', 'district', 'province', 'price',
       'bedroom_count', 'habitable_surface', 'terrace', 'facades']'''
class HouseDetails(BaseModel):
    postalcode : str
    subtype : str
    region : str
    district : str
    province : str
    bedroom_count: float
    habitable_surface:float
    terrace: bool
    facades: float
