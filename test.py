import re
from sentence import Sentence
string ="f&g"
print(re.findall("[a-zA-Z0-9]+|[&]|[~]|[|]+|\B=>", string))
sentence = Sentence(string)
#sentence.setValue({"b1": True, "e1": True,"f": False})
sentence.setValue({"f": False,"g": False, "h": False})
print(sentence.result())