import csv

def save_file(data):
    with open('Notes.csv', encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
