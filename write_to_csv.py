import csv

data = [
    ["SN", "Name", "Country", "Contribution", "Year"],
    [1, "Linus Torvalds", "Finland", "Linux Kernel", 1991],
    [2, "Tim Berners-Lee", "England", "World Wide Web", 1990],
    [3, "Guido van Rossum", "Netherlands", "Python", 1991]
]

with open("inventors.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data has been written to inventors.csv")