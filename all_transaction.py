# from datetime import datetime, date
import datetime
import sys
from math import isnan
from transaction import Transaction
from utils import *
    
class TransactionBook:

    def __init__(self):

        self.transaction_list: list[Transaction] = list()
        self.invalid_transactions_list: list[Transaction] = list()

    def load_transactions(self, transaction_list):
        for transac in transaction_list:
            if self.is_valid_transaction(transac):
                self.transaction_list.append(Transaction(*transac))
            else:
                self.invalid_transactions_list.append(Transaction(*transac))

    def netting(self):
        netting_dict = {}
        for transac in self.transaction_list:
            key = (transac.id_counterpart, transac.country, transac.rating, transac.industry, transac.transaction_date)
            if key not in netting_dict:
                netting_dict[key] = 0
            try:
                netting_dict[key] += float(transac.amount)
            except (ValueError, TypeError):
                continue
        return netting_dict

    def is_valid_transaction(self, transaction):
        """
            Cette fonction vérifie la validité des attributs pour la création d'un objet TransactionBook
        """
        try:
            idx, id_counterpart, country, rating, industry, transaction_date, amount = tuple(transaction)

            if not isinstance(idx, int) or idx <= len(self.transaction_list):
                return False
            if id_counterpart is None:
                return False
            if not is_valid_country(country):
                return False
            if not is_valid_rating(rating):
                return False
            if not is_valid_industry(industry):
                return False
            if is_invalid_amount(amount):
                return False
            
            # Convertir transaction_date pour validation
            datetime.datetime.strptime(transaction_date, '%d/%m/%Y')  # Vérifie le format de la date
            return True
        
        except (ValueError, TypeError) as e:
            return False
          
    def add_transaction(self, *args):

        for elt in args:
            if self.is_valid_transaction(elt):
                self.transaction_list.append(Transaction(*elt))
            else:
                print(f"Transaction invalide !")
                self.invalid_transactions_list.append(Transaction(*elt))

    def delete_transaction(self, *args, **kwargs):
        """
        Supprimer des transactions du book à l'aide d'une de ses caractéristiques (index, country, rating, industry ...)
        """
        
        def matches_criteria(transaction, criterion):
            return all(transaction.access_attr(k) == v for k, v in criterion.items())

        self.transaction_list = [transac for transac in self.transaction_list
                                 if not any(matches_criteria(transac, crit) for crit in args)]
        
    def update_transaction(self, actuel, nouveau, **kwargs):
        """
        Mise à jour des transactions du book à l'aide d'une de ses caractéristiques (index, country, rating, industry ...)
        """
        if kwargs:
            if actuel is None:
                actuel = kwargs
            else:
                actuel.update(kwargs)
                
        for transac in self.transaction_list:
            if actuel and all(transac.access_attr(cle) == value for cle, value in actuel.items()):
                if nouveau:
                    for cle, value in nouveau.items():
                        transac.update_attr(cle, value)
                    
    def get_transactions_between_dates(self, date_1, date_2):
        
        transacs = TransactionBook()
        transacs.transaction_list = [transac for transac in self.transaction_list
                              if date_1 <= transac.transaction_date <= date_2]
        
        return transacs

    def get_invalid_transactions(self):
        return '\n'.join(str(transac) for transac in self.invalid_transactions_list)

    def get_sorted_transactions(self, *args, **kwargs):
        sort_keys = args
        sorted_list = TransactionBook()
        if not sort_keys:
            return self.transaction_list

        sorted_list.transaction_list = sorted(self.transaction_list, key=lambda x: tuple(getattr(x, key) for key in sort_keys))
        return sorted_list
    
    def limit_transaction(func):
        def wrapper(self, limit=None, *args, **kwargs):
            transactions = TransactionBook()
            if limit is None:
                limit = len(self.transaction_list)
            count = 0
            for transaction in self.transaction_list:
                if count >= limit:
                    break
                transactions.transaction_list.append(transaction)
                count += 1
            return transactions
        return wrapper
         
    @limit_transaction
    def get_transactions(self, limit=None):
        return self.transaction_list

    def __str__(self) -> str:
        return '\n'.join(str(transac) for transac in self.transaction_list)
        
    def run(self):
        while True:
            print("\nGestionnaire de transactions")
            print("1. Ajouter une transaction")
            print("2. Afficher les transactions")
            print("3. Supprimer une transaction")
            print("4. Quitter")

            choice = input("Choisissez une option : ").strip()

            if choice == '1':
                transac = {}
                transac['index'] = int(input("Donnez l'index ").strip())
                transac['counterpart_id'] = input("Donnez le counterpart_id ").strip()
                transac['country'] = input("Donnez la country ").strip()
                transac['rating'] = input("Donnez le rating ").strip()
                transac['industry'] = input("Donnez l'industry ").strip()
                transac['date'] = input("Donnez la date ").strip()
                transac['solde'] = float(input("Donnez le solde ").strip())
                self.add_transaction(list(transac.values()))
            elif choice == '2':
                print("1. Afficher un nombre de transaction")
                print("2. Afficher les transactions entre deux dates")
                
                choix = input("Choissiez une option : ").strip()
                
                if choix=="1":
                    nombre_transac = input("Entrez le nombre de transactions à afficher ou appuyer sur entrée pour toutes les transactions: ").strip()
                    print(" "*20)
                    if not nombre_transac:
                        print(self.get_transactions())
                    else:
                        print(self.get_transactions(int(nombre_transac)))
                elif choix=="2":
                    date1 = input("Donnez une date de départ sous la forme dd/mm/yyyy : ").strip()
                    date2 = input("Donnez une date d'arrivée sous la forme dd/mm/yyyy : ").strip()
                    
                    print(f"Les transactions entre {date1} et {date2} sont")
                    print(self.get_transactions_between_dates(datetime.datetime.strptime(str(date1), '%d/%m/%Y').date(),
                                                              datetime.datetime.strptime(str(date2), '%d/%m/%Y').date()))
                    
            elif choice == '3':
                dicts = {"1":"index", "2": "country", "3":"rating", "4":"industry", "5":"date"}
                
                choix = input("Choisir une caractérisque : \n" + ", ".join(f"{cle}:{valeur}" for cle, valeur in dicts.items()) + " ")
                while choix not in ["1", "2", "3", "4", "5"]:
                    choix = input("Choisir une caractérisque : \n" + ", ".join(f"{cle}:{valeur}" for cle, valeur in dicts.items()) + " ")
                    
                valeur_transac = input("Entrez la valeur de la transaction à supprimer : ").strip()
                self.delete_transaction({dicts[choix]:valeur_transac})
                
            elif choice == '4':
                print("Au revoir !")
                sys.exit()
            else:
                print("Choix invalide, veuillez réessayer.")