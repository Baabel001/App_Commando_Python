import json
from math import isnan


with open('referential.json', 'r') as file:
    refs = json.load(file)
    
def is_valid_country(country_code) -> bool:
    return str(country_code) in refs.get('country', {})

def is_valid_rating(rating_code) -> bool:
    return str(rating_code) in refs.get('rating', {})

def is_valid_industry(industry_code) -> bool:
    return str(industry_code) in refs.get('industry', {})

def is_invalid_amount(number) -> bool:
    if number == "" or number is None:
        return True
    
    try:
        if isinstance(number, str):
            number = number.replace(',', '.')
            
        value = float(number)
        if isnan(value):
            return True
        
    except (ValueError, TypeError):
        return True
    
    return False