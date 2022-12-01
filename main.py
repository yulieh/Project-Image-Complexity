import time
import random
import os
import json
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.backend_bases import MouseButton

click_cord_x = -1
click_cord_y = -1


def on_click(event):
    if event.button is MouseButton.LEFT:
        print(f'data coords (x={event.xdata} y={event.ydata})')
        global click_cord_x, click_cord_y
        click_cord_x = event.xdata
        click_cord_y = event.ydata
        plt.close('all')

ls_files=os.listdir('pictures')
print(ls_files)

time_ls = []
correct_ls = []
for codchen in range(10):
    img_name = random.choice(ls_files)
    img = plt.imread("pictures/" + img_name)
    #x=img[:,:,0]
    #print(len(x[1]))
    # histogram=plt.hist(x)
    # print(len(histogram[2]))
    # print(len([i for i in histogram[0] if i>0.]))
    square_size = int(min(img.shape[1], img.shape[0])/10)
    x1 = random.randint(0, img.shape[1] - square_size)
    x2 = x1 + square_size
    y1 = random.randint(0, img.shape[0] - square_size)
    y2 = y1 + square_size
    img2 = img[y1:y2, x1:x2, :]

    plt.subplot(1, 2, 1)
    plt.imshow(img)

    plt.subplot(1, 2, 2)
    plt.imshow(img2)

    t0 = time.time()
    plt.connect('button_press_event', on_click)
    plt.show()
    t1 = time.time()
    spent_time = t1 - t0
    print(spent_time)
    time_ls.append(spent_time)

    if x1 < click_cord_x < x2 and y1 < click_cord_y < y2:
        print("Correct!")
        correct_ls.append(1)
    else:
        print("Naaah")
        correct_ls.append(0)

print(sum(time_ls)/len(time_ls))
print(sum(correct_ls)/len(correct_ls))

data_dict={'Resonse Time:': time_ls,
           'Average Time': sum(time_ls)/len(time_ls),
           'Responses':correct_ls,
           'Correct Rate':sum(correct_ls)/len(correct_ls)}
print("Hello Reinis, your average time is {} a"
      "nd your correct rate is {}. "
      "You should be better than this!".format(data_dict['Average Time'], data_dict['Correct Rate']))

now=datetime.now()
date_time=now.strftime("%d-%m-%Y-%H-%M")
with open('data/'+date_time+".json",'w') as f:
    json.dump(data_dict,f)