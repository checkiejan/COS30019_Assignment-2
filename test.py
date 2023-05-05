import re
from sentence import Sentence
string ="f1"
print(re.findall("[a-zA-Z0-9]+|[&]|[~]|[|]+|\B=>", string))
sentence = Sentence(string)
#sentence.setValue({"b1": True, "e1": True,"f": False})
sentence.setValue({"f1": False})
print(sentence.result())