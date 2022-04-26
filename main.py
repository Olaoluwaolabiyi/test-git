import pandas as pd
import numpy as np

people = {
    'name': ['Ola', 'Solo', 'Ugo'],
    'sex': ['Male', 'Male','Male'],
    'age': [1,2,3]
}

peopledf = pd.DataFrame(data=people)

print('Hello_world')
print(peopledf)