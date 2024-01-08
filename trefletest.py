import requests
import os
import random
import csv
import scipy


def calculate_score(features, plant):
    score = 0
    lighting = plant['lighting']
    is_flower = plant['is_flower']
    is_edible = plant['is_edible']
    is_toxic = plant['is_toxic']
    lifespan = plant['lifespan']
    # humidity = plant['humidity']

    return score
# def parse(response):
#     if 'data' in response:
#         plant_data = response['data']
#         scored_plants = []

#         # for plant in plant_data:
#         #     score = calculate_score(plant)
#         #     scored_plants.append((plant, score))

#         # scored_plants.sort(key=lambda x: x[1], reverse=True)
#         # top_plants = scored_plants[:10]
#         names = [item[0]['common_name'] for item in plant_data]

#         return names
#     else:
#         print("Sorry, no results found.")


def parse(response):
    if 'data' in response:
        plant = response['data']
        names = [item['common_name']for item in plant[:10]]
        return names
    else:
        print("Sorry, no results found.")


def filter_db(lighting, is_flower, is_edible, is_toxic, lifespan):
    # Constants
    token = "X9NC_86oMIlOqctvIdZn8n_FqSSpruBNaEuzXxdiOq8"
    request_url = "https://trefle.io/api/v1/species?"
    request_params = "&token=" + token
    filters = []
    if lighting:
        filters.append("filter%5Blight%5D=" + str(lighting))
    if is_flower:
        filters.append("filter%5Bflower_conspicuous%5D=true")
    if is_edible:
        filters.append("filter%5Bedible_part%5D=true")
    if is_toxic:
        filters.append("filter%5Btoxicity%5D=none")
    if lifespan:
        filters.append("filter%5Blifecycle%5D=" + lifespan)
    # if care:
    #   filters.append("filter%5Bdifficulty%5D=" + str(care))
    # if color:
    #     filters.append("filter%5Bcolor%5D=" + color)
    # if humidity:
    #     filters.append("filter%5Bhumidity%5D=" + humidity)

    filters.append("filter%5Bnative_status%5D=indoor")

    if filters:
        request_url += "&".join(filters)

    request = request_url + request_params
    response = requests.get(request)
    data = response.json()
    data = parse(data)
    print(data)

    return data


def gen_random(n):
    all_results = []
    for i in range(n):
        lighting = random.randint(0, 10)
        is_flower = random.choice([True, False])
        is_edible = random.choice([True, False])
        is_toxic = random.choice([True, False])
        lifespan = random.choice(['perennial', 'annual', 'biennial'])
        # humidity = random.choice(['low humidity', 'moderate humidity', 'high humidity'])
        results = filter_db(lighting, is_flower, is_edible, is_toxic, lifespan)

        all_results.extend(results)

    return all_results


def train_data():
    num_samples = 20
    folder_path = "data"
    file_name = "train.csv"
    # Save to csv file
    with open(os.path.join(folder_path, file_name), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["lighting", "is_flower", "is_edible",
                        "is_toxic", "lifespan", "result"])

        all_results = gen_random(num_samples)

        for result in all_results:
            if len(result) != 6:
                continue
            lighting, is_flower, is_edible, is_toxic, lifespan, humidity = result
            filtered_result = filter_db(
                lighting, is_flower, is_edible, is_toxic, lifespan)

            writer.writerow([lighting, is_flower, is_edible,
                            is_toxic, lifespan, filtered_result])

    print("Training data saved")


def clear_data():
    folder_path = "data"
    file_name = "train.csv"
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        os.remove(file_path)
        print("Data cleared successfully.")
    else:
        print("No data file found.")


clear_data()
train_data()
