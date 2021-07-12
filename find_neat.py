import csv
from intersect import find_intersections

long_words = []
longest_word = ""
with open("words", "r") as f:
    with open("result.csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        for line in f:
            result = find_intersections(line.strip())
            if result == 0:
                if len(line.strip()) > 6:
                    long_words.append(line.strip())
                if len(line.strip()) > len(longest_word):
                    longest_word = line.strip()
            # csvwriter.writerow([line.strip(), result])


print(sorted(long_words, key=len))
