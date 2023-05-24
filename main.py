import sys
from TT import TT
from FC import FC
from KB import KB
from BC import BC
from WSAT import WSAT
from sentence import Sentence
kb = None
query = None
TT = TT()
FC = FC()
BC = BC()
WSAT = WSAT()
with open(sys.argv[2],"r") as f: 
    track = f.readline().strip("[\n]")
    tracks = f.readline()
    tracks = tracks.strip("[\n] ")[:-1].strip().split(";")
    for i in range(len(tracks)):
        tracks[i] = tracks[i].replace(" ", "")
    kb = KB(tracks)
    track = f.readline().strip("[\n]")
    track = f.readline().strip("[\n]")
    query = Sentence(track)


methods = {"tt":TT,"fc": FC,"bc":BC, "wsat":WSAT}
if len(sys.argv) == 3:
    method = sys.argv[1].lower()
    
    if method in methods.keys():
        t = methods[method]

        t.infer(kb,query)
        print(t.output)
        pass
       
    else:
        print("Unknown method")
elif len(sys.argv) > 2:
    print("wrong number of argument")
else:
    pass

