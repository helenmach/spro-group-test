import pandas as pd
from pymongo import MongoClient

#criando conexão com o MongoBD (host, port)
mongodb = MongoClient('localhost', 27017)

#criando DataFrame para os tipos de Carros
df_carros = pd.DataFrame(
    data = {
        "Carro": ["Onix", "Polo", "Sandero", "Fiesta", "City"],
        "Cor": ["Prata", "Branco", "Prata", "Vermelho", "Preto"],
        "Montadora": ["Chevrolet", "Volkswagen", "Renault", "Ford", "Honda"],
    }
)

#criando DataFrame para as Montadoras como dicionário
df_montadoras = pd.DataFrame(
    data = {
        'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'],
        'País': ['EUA', 'Alemanha', "França", 'EUA', 'Japão']
    }
)

#referenciando a base de dados a ser utilizada
db = mongodb.spro_group

#salvando os dataframes nas devidas collections dentro da base de dados referenciada
db.carros.insert_many(df_carros.to_dict('records'))
db.montadoras.insert_many(df_montadoras.to_dict('records'))