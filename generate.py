# Generates data to use for training and validation
import csv
import trefle_search 
import requests


def main():

    # Generate training data
    parsed = ""
    training_data = []
    for data in parsed:
        # Set vars from the data
        use = data["use"]
        time = data["time"]
        flower = data["flower"]
        eating = data["eating"]
        size = data["size"]
        light = data["light"]
        name = data["name"]

        entry = [use, time, flower, eating, size, light, name]  

        training_data.append(entry)

    # Save to CSV file
    with open("training_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Use", "Time", "Flower", "Eating", "Size","Light","Name"])  
        writer.writerows(training_data)  