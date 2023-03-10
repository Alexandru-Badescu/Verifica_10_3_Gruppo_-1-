import Verifica_10_3_Gruppo_1(Saluto_Carli_Gruppo1)
import Verifica_10_3_Gruppo_1(saluto_Rolfini_Gruppo_1)
import Verifica_10_3_Gruppo_1(saluto_Mantovani_Gruppo1)
import Verifica_10_3_Gruppo_1(simonevecchiattini)
def Verifica_10_3_Gruppo_1(nome, cognome):
    """Restituisce una stringa di saluto con nome e cognome"""
    return f"Ciao {nome} {cognome}, piacere di conoscerti!"

# Esempio di utilizzo della funzione saluto_cognome()
nome_utente = input("Inserisci il tuo nome: ")
cognome_utente = input("Inserisci il tuo cognome: ")
saluto = Verifica_10_3_Gruppo_1(cognome_utente,nome_utente)
print(saluto)

Verifica_10_3_Gruppo_1()
