import sys
from TT import TT
from FC import FC
from KB import KB
from BC import BC
from sentence import Sentence
kb = None
query = None
TT = TT()
FC = FC()
BC = BC()
with open(sys.argv[2],"r") as f: 
    track = f.readline().strip("[\n]")
    tracks = f.readline().strip("[\n] ")[:-1].strip().split(";")
    for i in range(len(tracks)):
        tracks[i] = tracks[i].strip()
    kb = KB(tracks)
    
    track = f.readline().strip("[\n]")
    track = f.readline().strip("[\n]")
    query = Sentence(track)
    
    
# TT.TTEntail(kb,query)
# #print(kb.PLTrue({'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': False, 'h': False, 'd': True, 'a': True}))
# print(TT.getOutput())
# lst =[
#     {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': True, 'h': True, 'd': True, 'a': True},
#     {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': False, 'h': True, 'd': True, 'a': True},
#     {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': False, 'h': False, 'd': True, 'a': True}
# ]

# kb.setValue( {'p2': True, 'p3': False, 'p1': False, 'c': False, 'e': False, 'b': True, 
#               'f': False, 'g': False, 'h': False, 'd': False, 'a': True})

# FC.infer(kb, query)
# TT.TTEntail(kb,query)

FC.infer(kb, query)
print(FC.getOutput())






# for x in lst:
#     print(kb.PLTrue(x))

# methods = {"tt":TT,"fc": FC,"bc":BC}
# if len(sys.argv) == 3:
#     method = sys.argv[1].lower()
    
#     if method in methods.keys():
#         t = methods[method]
#         t.infer(kb,query)
#         print(t.output)
#         pass
       
#     else:
#         print("Unknown method")
# elif len(sys.argv) > 2:
#     print("wrong number of argument")
# else:
#     pass

