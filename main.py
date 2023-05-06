import sys
from TT import TT
from KB import KB
from sentence import Sentence
kb = None
query = None
TT = TT()
with open("test.txt","r") as f: 
    track = f.readline().strip("[\n]")
    tracks = f.readline().strip("[\n] ")[:-1].strip().split(";")
    for i in range(len(tracks)):
        tracks[i] = tracks[i].strip()
    kb = KB(tracks)
    
    track = f.readline().strip("[\n]")
    track = f.readline().strip("[\n]")
    query = Sentence(track)
    print(track)
    
TT.TTEntail(kb,query)
#print(kb.PLTrue({'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': False, 'h': False, 'd': True, 'a': True}))
print(TT.getOutput())
lst =[
    {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': True, 'h': True, 'd': True, 'a': True},
    {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': False, 'h': True, 'd': True, 'a': True},
    {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': False, 'h': False, 'd': True, 'a': True}
]
# for x in lst:
#     print(kb.PLTrue(x))

# methods = ["tt","fc","bc"]
# if len(sys.argv) == 3:
#     method = sys.argv[1].lower()
    
#     if method in methods:
#         pass
       
#     else:
#         print("Unknown method")
# elif len(sys.argv) > 2:
#     print("wrong number of argument")
# else:
#     pass

