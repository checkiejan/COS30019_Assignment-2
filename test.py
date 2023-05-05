import re
from sentence import Sentence
string ="f&g => h"
print(re.findall("[a-zA-Z0-9]+|[&]|[~]|[|]+|\B=>", string))
sentence = Sentence(string)
#sentence.setValue({"b1": True, "e1": True,"f": False})
sentence.setValue({"f": True,"g": True, "h": False})
print(sentence.result())