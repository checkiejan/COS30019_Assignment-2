import sys
from KB import KB
kb = None
with open("test.txt","r") as f: 
    track = f.readline().strip("[\n]")
    tracks = f.readline().strip("[\n] ")[:-1].strip().split(";")
    for i in range(len(tracks)):
        tracks[i] = tracks[i].strip()
    kb = KB(tracks)
    print(tracks)
    
for s in kb.sentences:
    print(s.lst)

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

