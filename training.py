import random
import trefle_search
import parse_json
import csv

use = ["eating", "flowers", "greenery"]
time_period = ["annual", "biennial", "perennial"]
toxicity = [True, False]
months = ["January", "February", "March", "April", "May", "June", "July", 
          "August", "September", "October", "November", "December"]
light = ["2", "6", "10"]


def search(u,to, l): #generates req_string
  # Eating

  #time_params = [ti, time_months]
  toxicity = [to]
  height_min = random.randint(1,70)
  height_range = random.randint(5, 20)
  height_max = height_min+height_range
  req_string = trefle_search.create_req("", u, [], [], [], [], toxicity, [str(height_min), str(height_max)], l)
  #req_string = trefle_search.create_req_0("")
  print(req_string)
  results = trefle_search.main(req_string)

  with open("results.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([u, to, l, results])
        
  return results
  # return parse_json.parse_response(req_string)
  

def random_data(n):
# n = 5 #number of random combinations to generate

  for i in range(n):
      u = random.choice(use)
      # ti = random.choice(time_period)
      #time_months = random.choice(months)
      to = random.choice(toxicity)
      l = random.choice(light)
      print(f"use: {u}, , toxic: {to}")
      search(u,to,l)

  
#testing 

random_data(1)