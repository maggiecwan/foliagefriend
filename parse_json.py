import json
# Parses JSON Response
def parse_response(filename):
    #dict = json.loads("json/response.json")
    ##name = dict["data"][0]["common_name"]
    ## #name = dict["data": 0, "common_name"]
   # name = dict["data"][0]["common_name"]
    ##for i in range(len(dict["data"])):
    ##    name.append(dict["data"][i]["common_name"])
    
    with open(filename) as f:
        dict= json.load(f)

    data = dict["data"]
    n = []
    l = len(data)
    if l > 10:
        l = 10
    for i in range(l):
        plant = data[i]
        n.append(plant["common_name"])
    #name = data["common_name"]

    # if(len(n) > 10):
    #     n = n[:10]
    if len(n) == 0:
        print("no searches found")
    else:
        print(n)
    return n


def parse_input(size, pets, sunlight, effort, purpose, time):
    #ml stuff
    return 0
