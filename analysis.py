import os
import json
from matplotlib import pyplot as plt

ls_files = os.listdir('data')
print(ls_files)

average_time_ls = []
correct_rate_ls = []
for ls in ls_files:
    with open('data/'+ls,'r') as f :
        data = json.load(f)
        average_time_ls.append(data['Average Time'])
        correct_rate_ls.append(data['Correct Rate'])
print(average_time_ls)
print(correct_rate_ls)
y=average_time_ls
x=[i for i in range(len(y))]
plt.scatter(x,y)
plt.scatter(x,correct_rate_ls )
plt.show()

#complexity vs correct rate

#complexity vs average time


