import io
import csv
from operator import itemgetter

data = []
with io.open("input.csv", "r", encoding="utf8") as fp:
    for line in fp:
        url, clicks = line.split(";")
        clicks = int(clicks[:-1])
        data.append((url, clicks))

data = sorted(data, key=itemgetter(1), reverse=True)

set_a = []
sum_a = 0
set_b = []
sum_b = 0
for i in range(0, len(data), 2):
    j = i+1
    val_a = data[i]
    val_b = data[j]

    if sum_a > sum_b:
        set_a.append(val_a)
        sum_a += val_a[1]
        set_b.append(val_b)
        sum_b += val_b[1]
    else:
        set_a.append(val_b)
        sum_a += val_b[1]
        set_b.append(val_a)
        sum_b += val_a[1]


with io.open("output.csv", "w") as fp:
    writer = csv.writer(fp, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in range(len(set_a)):
        writer.writerow((set_a[i][0], set_a[i][1], set_b[i][0], set_b[i][1]))

print("SUM", sum_a, sum_b)
