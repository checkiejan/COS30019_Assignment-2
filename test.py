import re
string = "b&e => f"
string = string.strip(" ")
print(re.split("[&] =>",string))