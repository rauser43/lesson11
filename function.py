

def new_list (first_list,second_list):
    first_list = ['1', '2', '3', '4', '5', '6', '7']
    second_list =['7', '6', '5', '4', '3', '2', '1']
    new_list == first_list*second_list
print (new_list)

def test_new_list ():



def name_мак():
    names = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
print (name_мак)
import random
def get_country(country, capital):
    full_country = f"{country}-{capital}"
    return full_country.title()

def test_get_country (country, capital):
    assert get_country (Russia)== (Russia, Moscow)