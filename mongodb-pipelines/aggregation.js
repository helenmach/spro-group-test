[
  {
    '$lookup': {
      'from': 'montadoras', 
      'localField': 'Montadora', 
      'foreignField': 'Montadora', 
      'as': 'Montadoras'
    }
  }, {
    '$addFields': {
      'Pais': {
        '$getField': {
          'field': 'País', 
          'input': {
            '$arrayElemAt': [
              '$Montadoras', 0
            ]
          }
        }
      }
    }
  }, {
    '$group': {
      '_id': '$Pais', 
      'Carros': {
        '$push': '$Carro'
      }
    }
  }
]