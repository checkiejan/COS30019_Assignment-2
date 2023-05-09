import re
import numpy as np
import pandas as pd
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})
df.dropna(axis='columns',ignore_index = True)
from sentence import Sentence
string ="f&g"
print(re.findall("[a-zA-Z0-9]+|[&]|[~]|[|]+|\B=>", string))
sentence = Sentence(string)
#sentence.setValue({"b1": True, "e1": True,"f": False})


sentence.setValue({"f": True,"g": True, "h": False})
lst = [1,2,3,4,5,6]
print(lst.pop(0))
print(lst)
print(sentence.result())
t1 = {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': False, 'h': True, 'd': True, 'a': True}
lst =[
    {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': True, 'h': True, 'd': True, 'a': True},
    {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': False, 'h': True, 'd': True, 'a': True},
    {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': False, 'h': False, 'd': True, 'a': True}
]
print(t1 in lst)
