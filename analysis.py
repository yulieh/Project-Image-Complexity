import os
import json
from matplotlib import pyplot as plt

ls_files = os.listdir("data")

average_time_ls = []
correct_rate_ls = []
average_entropy_ls = []

time_ls = []
entropy_ls = []
responses_ls = []

for file in ls_files:
    with open("data/" + file, "r") as f:
        data = json.load(f)
        average_time_ls.append(data["Average Time"])
        correct_rate_ls.append(data["Correct Rate"])
        average_entropy_ls.append(data["Average Entropy"])

        time_ls += data["Resonse Time"]
        entropy_ls += data["Entropy Score"]
        responses_ls += data["Responses"]


plt.scatter([i for i in range(len(average_time_ls))], average_time_ls)
plt.scatter([i for i in range(len(correct_rate_ls))], correct_rate_ls)
plt.scatter([i for i in range(len(average_entropy_ls))], average_entropy_ls)
plt.legend(["Average Time", "Correct Rate", "Average Entropy"])
plt.xlabel("Recording #")
plt.ylabel("Result")
plt.title("Average scores of each recording")
plt.show()


plt.scatter(entropy_ls, time_ls)
plt.xlabel("Entropy")
plt.ylabel("Response time")
plt.title("Response time vs Entropy")
plt.show()

score = [0 for i in range(int(round(max(entropy_ls))) + 1)]
count = [0 for i in range(int(round(max(entropy_ls))) + 1)]

for i in range(len(responses_ls)):
    level = int(round(entropy_ls[i]))
    score[level] += responses_ls[i]
    count[level] += 1

for i in range(len(score)):
    try:
        score[i] /= count[i]
    except ZeroDivisionError:
        score[i] = 0


plt.plot([i for i in range(len(score))], score)
plt.xlabel("Correct Rate")
plt.ylabel("Entropy Level")
plt.title("Correct rate per entropy level")
plt.show()
