import datetime
import pandas as pd
# from datetime import datetime, date
import datetime
from utils import refs

class Transaction:

    def __init__(self, index: int, id_counterpart: str, country: str, rating: str, industry: str,
                 transaction_date: datetime.date, amount: float):

        self.index= index
        self.id_counterpart = id_counterpart
        self.country = self.decode_country(country)
        self.rating = self.decode_rating(rating)
        self.industry = self.decode_industry(industry)
        self.transaction_date = self.convert_date(transaction_date)
        self.amount = self.convert_amount(amount)

    def decode_country(self, country_code: str) -> str:
        decoded_country = refs.get('country', {}).get(str(country_code))
    
        return decoded_country if decoded_country is not None else str(country_code)
    
    def decode_rating(self, rating_code: str) -> str:
        decoded_rating = refs.get('rating', {}).get(str(rating_code))
    
        return decoded_rating if decoded_rating is not None else str(rating_code)
    
    def decode_industry(self, industry_code: str) -> str:
        decoded_industry = refs.get('industry', {}).get(str(industry_code))
    
        return decoded_industry if decoded_industry is not None else str(industry_code)
    
    def convert_amount(self, amount) -> float:
        try:
            # Remplacer la virgule par un point pour le formatage correct en float
            amount = str(amount).replace(',', '.')
            return float(amount)
        except (ValueError, TypeError):
            return float('nan')
            
    def convert_date(self, date_str: str) -> datetime.date:
        try:
            return datetime.datetime.strptime(str(date_str), '%d/%m/%Y').date()
        except ValueError:
            return date_str
    
    def __str__(self) -> str:
        return (f"index:{self.index} | "
                f"counterpart_id:{self.id_counterpart} | "
                f"country:{self.country} | "
                f"rating:{self.rating} | "
                f"industry:{self.industry} | "
                f"date:{self.transaction_date} | "
                f"amount:{self.amount}")
        
    def update_attr(self, attr_name, value):
        """
        Met à jour un attribut de l'objet Transaction.
        """
        try:
            setattr(self, attr_name, value)
        except AttributeError:
            return f"Erreur ! Attribut {attr_name} non trouvé"
        except Exception as ex:
            return f"Erreur inattendue : {str(ex)}"

    def access_attr(self, attr_name):
        """
        Accède à un attribut de l'objet Transaction.
        """
        try:
            return getattr(self, attr_name)
        except AttributeError:
            return f"Erreur ! Attribut {attr_name} non attendu"
        except Exception as ex:
            return f"Erreur inattendue : {str(ex)}"
        
    def get_attributes_as_list(self):
        return list(vars(self).values())