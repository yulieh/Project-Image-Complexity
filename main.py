import time
import random
import os
import json
from datetime import datetime

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backend_bases import MouseButton
from skimage.filters.rank import entropy
from skimage.color import rgb2gray
from skimage.morphology import disk

click_cord_x = -1
click_cord_y = -1


def on_click(event):
    if event.button is MouseButton.LEFT:
        global click_cord_x, click_cord_y
        click_cord_x = event.xdata
        click_cord_y = event.ydata
        plt.close("all")


ls_files = os.listdir("pictures")
if not len(ls_files):
    raise Exception("No images found in pictures folder")

time_ls = []
correct_ls = []
entropy_ls = []

print("Please click on location of the picture on the right in the picture on the left")

for _ in range(10):
    img_name = random.choice(ls_files)
    img = plt.imread("pictures/" + img_name)
    square_size = int(min(img.shape[1], img.shape[0]) / 5)
    x1 = random.randint(0, img.shape[1] - square_size)
    x2 = x1 + square_size
    y1 = random.randint(0, img.shape[0] - square_size)
    y2 = y1 + square_size
    img2 = img[y1:y2, x1:x2, :]

    plt.subplots(1, 2, gridspec_kw={"width_ratios": [3, 1]}, figsize=(12, 8))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(img)

    plt.subplot(1, 2, 2)
    plt.title("Piece to Find")
    plt.imshow(img2)

    t0 = time.time()
    plt.connect("button_press_event", on_click)
    plt.suptitle("Images")

    plt.show()

    t1 = time.time()
    spent_time = t1 - t0
    time_ls.append(spent_time)

    if x1 < click_cord_x < x2 and y1 < click_cord_y < y2:
        correct_ls.append(1)
    else:
        correct_ls.append(0)

    img2_gray = rgb2gray(img2)
    entropy_image = entropy(img2_gray, disk(round(square_size / 50)))
    entropy_ls.append(np.mean(entropy_image))

data_dict = {
    "Resonse Time": time_ls,
    "Average Time": sum(time_ls) / len(time_ls),
    "Responses": correct_ls,
    "Correct Rate": sum(correct_ls) / len(correct_ls),
    "Entropy Score": entropy_ls,
    "Average Entropy": sum(entropy_ls) / len(entropy_ls),
}
print(
    "Hello, your average time is {} a"
    "nd your correct rate is {}. Average entropy is {}".format(
        data_dict["Average Time"],
        data_dict["Correct Rate"],
        data_dict["Average Entropy"],
    )
)

now = datetime.now()
date_time = now.strftime("%d-%m-%Y-%H-%M")
with open("data/" + date_time + ".json", "w") as f:
    json.dump(data_dict, f)

print("Results saved to {} file".format(date_time + ".json"))
