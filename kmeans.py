# Code references: https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097 with adaptation 
# for video stream
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

cap = cv2.VideoCapture(0)

clt = KMeans(n_clusters=3) #cluster number

while (True):
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()

    h, w = frame.shape[:2]
    x_start = int(w * 0.3)
    x_end = int(w * 0.7)
    y_start = int(h * 0.3)
    y_end = int(h * 0.7)

    rect = frame[y_start:y_end, x_start:x_end]

    rect_rgb = cv2.cvtColor(rect, cv2.COLOR_BGR2RGB)
    img = rect_rgb.reshape((rect.shape[0] * rect.shape[1],3))
    clt.fit(img)

    hist = find_histogram(clt)
    bar = plot_colors2(hist, clt.cluster_centers_)

    cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
    cv2.imshow('frame',frame)

    plt.axis("off")
    plt.imshow(bar)
    plt.show()