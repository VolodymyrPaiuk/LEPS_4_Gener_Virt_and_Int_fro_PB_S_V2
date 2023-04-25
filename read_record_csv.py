import csv
def read (way_PB_S):
    with open(way_PB_S, "r") as f:
        reader = csv.reader(f)
        people = []
        for row in reader:
            for roww in row:
                people.append(roww.split(";"))
        # print(people)
        # print(people[1][0])
    return people

def record (mas_for_w, way_for_w):
    with open(way_for_w, "w", newline="") as k:
        writer = csv.writer(k, delimiter=';')
        writer.writerows(mas_for_w)
