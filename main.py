import pandas as pd
import datetime

from all_transaction import TransactionBook

if __name__ == "__main__":
    

    transactions_list = pd.read_csv(r"data.csv", sep=";", decimal=",").values.tolist()
    transaction_to_add = [2001, "1", "10", "11", "58", "01/02/2023", 48919]
    
    transaction_book = TransactionBook()
    
    # Pour naviguer facilement sur les fonctions, on peut utiliser la ligne de code "transaction_book.run()" et mettre en commentaire toutes les lignes après
    # transaction_book.load_transactions(transactions_list)
    # transaction_book.run()
    
    # 1. implémenter load_transaction pour charger la liste de transaction dans le TransactionBook
    transaction_book.load_transactions(transactions_list)
    # 2. implémenter add_transaction pour ajouter "transaction_to_add" dans le TransactionBook
    transaction_book.add_transaction(transaction_to_add)
    # 3. implémenter get_transactions qui affiche l'ensemble des transactions du TransactionBook et le décorateur limit_transaction(n)
    # qui limite à "n" le nombre de transactions affichées
    print(transaction_book.get_transactions())
    # 4. implémenter delete_transaction et update_transaction
    transaction_book.update_transaction({"country": "FR"}, {"country": "FRA"}) # -> update les transactions FR en FRA
    transaction_book.delete_transaction({"rating": "F"}) # -> supprime les transactions de rating F
    # 5. implémenter get_transactions_between_dates pour avoir toutes les transactions entre 2 dates
    print(transaction_book.get_transactions_between_dates(datetime.date(2023, 1, 1), datetime.date(2023, 12, 1)))
    # 6. implémenter get_invalid_transaction pour avoir les transactions invalides (mauvais type, valeur vide etc...)
    print(transaction_book.get_invalid_transactions())
    # 7. implémenter netting qui permet d'avoir le solde des transactions par contreparties (= à un group_by sur toutes les caractéristiques des transactions sauf sur l'index)
    print(transaction_book.netting())
    # 8. faire en sorte que print(transaction_book) retourne la liste des transactions
    print(transaction_book)
    # 9. implémenter get_sorted_transactions qui permet de retourner les transactions triées selon les caractéristiques passées en argument
    print(transaction_book.get_sorted_transactions("country", "rating"))