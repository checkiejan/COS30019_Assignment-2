import sys
with open(sys.argv[2],"r") as f: 
    track = f.readline().strip("[\n]")
    tracks = f.readline().strip("[\n] ")[:-1].split(";")
    print(track)
    

methods = ["tt","fc","bc"]
if len(sys.argv) == 3:
    method = sys.argv[1].lower()
    
    if method in methods:
        pass
       
    else:
        print("Unknown method")
elif len(sys.argv) > 2:
    print("wrong number of argument")
else:
    pass