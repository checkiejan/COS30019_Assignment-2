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
    tracks = f.readline()
    tracks = tracks.strip("[\n] ")[:-1].strip().split(";")
    for i in range(len(tracks)):
        tracks[i] = tracks[i].strip()
        
    kb = KB(tracks)
    
    track = f.readline().strip("[\n]")
    track = f.readline().strip("[\n]")
    query = Sentence(track)
    
lst = [
    {'a': True, 'b': True, 'p3': True, 'p2': True, 'c': True, 'p1': True},
    {'a': True, 'b': False, 'p3': True, 'p2': True, 'c': True, 'p1': True}
]
#TT.infer(kb,query)
#print(kb.PLTrue({'a': True, 'b': True, 'p3': True, 'p2': True, 'c': True, 'p1': True}))
#print(TT.getOutput())

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

