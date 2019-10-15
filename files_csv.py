import csv

elems = [
    {"first_name": "Baked", "last_name": "Beans"},
    {"first_name": "Lovely", "last_name": "Spam"},
    {"first_name": "Wonderful", "last_name": "Spam"},
]

# write
print("==Write file==")
with open("names_iter_2.csv", "w", newline="") as csvfile:
    fieldnames = ["first_name", "last_name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(elems)
    # for elem in elems:
    #     writer.writerow(elem)


# read
print("==Read file==")
with open("names.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["first_name"], row["last_name"])
