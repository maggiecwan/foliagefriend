#Generates Trefle search string based on input, and writes JSON file
import requests
import json
import os
import parse_json
token = "X9NC_86oMIlOqctvIdZn8n_FqSSpruBNaEuzXxdiOq8"
#request_start = "https://trefle.io/api/v1/species?"
request_start = "https://trefle.io/api/v1/plants?"
request_end = "token=" + token
req_str= ""

def use(req_str, purpose):
  #What do you want plants for?
  if purpose == "eating":
    req_str += "filter_not%5Bedible_part%5D=null&"
  elif purpose == "flowers":
    req_str += "filter%5Bflower_conspicuous%5D=true&"
  elif purpose == "greenery": #greenery
    req_str += "filter%5Bleaf_retention%5D=true&"
    

  # #Eating:
  # if(eating):
  #   req_str += "filter_not%5Bedible_part%5D=null&"

  # #flowers
  # if(flowers):
  #   req_str += "filter%5Bflower_conspicuous%5D=true&"


  # #greenery
  # if(greenery):
  #   req_str += "filter%5Bleaf_retention%5D=true&"
    
  return req_str



#Where do you live?


def time(req_str, time_params):
  if time_params == []:
    return req_str
  #How long do you want them to last?
  time,mos = time_params[0],time_params[1]
  #time = “annual”,”biennial”, or “perennial”
  req_str += "filter%5Bduration%5D=" + time + "&"
  #OR 
  #mos = array of strings, each string is a growth month
  req_str += "filter%5Bgrowth_months%5D=" + mos + "&"
  return req_str

def flower(req_str, flower_params):
  if flower_params == []:
    return req_str
  color, flower_mos = flower_params[0],flower_params[1]
  #If flower:
  #What color
  req_str += "filter%5Bflower_color%5D=" + color + "&"
  #When do you want them to bloom
  #mos = array of string, each string is a bloom month
  req_str += "filter%5Bbloom_months%5D=" + flower_mos + "&"
  return req_str

def eating(req_str, eating_params):
  #get vegetables or fruits
  if eating_params == []:
    return req_str

  vegetables, fruits, fruit_months = eating_params[0],eating_params[1],eating_params[2]
  if (vegetables):
    req_str += "filter%5Bvegetable%5D=true&"
  elif (fruits):
  #mos = array string of fruiting months
    req_str += "filter%5Bedible%5D=true&filter%5Bvegetable%5D=false&filter%5Bfruit_months%5D=" + fruit_months + "&"
  return req_str

def foliage(req_str, foliage_params):
  if foliage_params == []:
    return req_str
  clr, ret =  foliage_params[0],foliage_params[1]
  #foliage
  #clr = foliage color
  #ret = boolean of if you want to retain leaves all year long
  req_str += "filter%5Bfoliage_color%5D=" + clr + "&filter%5Bleaf_retention%5D=" + ret + "&"
  return req_str


def tox(req_str, notox):
  #toxicity
  #for having pets or small children
  if notox == None:
    return req_str
  if(notox):
    req_str += "filter%5Btoxicity%5D=none&"
  return req_str

def size(req_str, size_params):
  if size_params == []:
    return req_str
  low, high = size_params[0], size_params[1]
  #size of plant
  #low = bottom of range (cm)
  #high = top of range (cm)
  #req_str = req_str + "filter_not%5Baverage_height_cm%5D=null&filter%5Baverage_height_cm%5D=" + low + "%2C" + high + "&"
  req_str = req_str + "filter%5Baverage_height_cm%5D=" + low + "%2C" + high + "&"

  return req_str

def light(req_str, light_intensity):
  #available light
  if light_intensity == "":
    return req_str
  #n = int from 0 to 10, where 0 is almost no light available, 10 is a lot
  req_str = req_str + "filter%5Blight%5D=" + light_intensity + "&"
  return req_str

def create_req_0(req_str):
  req_str = use(req_str, "greenery")
  #req_str = flower(req_str, "red", "May")
  req_str = tox(req_str, False)
  #req_str = time(req_str, )
  req_str = size(req_str, ["5", "100"])
  req_str = light(req_str, "5")
  return req_str

def create_req(req_str, purpose, time_params, flower_params, eating_params, foliage_params,notox, size_params, light_intensity):
  req_str = use(req_str,purpose)
  req_str = time(req_str,time_params)
  req_str = flower(req_str,flower_params)
  req_str = eating(req_str, eating_params)
  req_str = foliage(req_str, foliage_params)
  req_str = tox(req_str, notox)
  req_str = size(req_str, size_params)
  req_str = light(req_str,light_intensity)
  return req_str



def main(req_str):
  
  #req_str = create_req_0(req_str)
  req = request_start+ req_str + request_end
  r=requests.get(req)
  # print(r.json)
  # clear JSON file first
  if os.path.exists("json/response.json"):
    os.remove("json/response.json")
  
  with open("json/response.json", "w+") as f:
    json.dump(r.json(), f)

  parse_json.parse_response('json/response.json')
  print(req)
#filter%5Btoxicity%5D=none&filter%5Baverage_height_cm%5D=22%2C41&filter%5Blight%5D=2&
main(req_str="")