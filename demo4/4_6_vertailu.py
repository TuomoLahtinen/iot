import matplotlib
matplotlib.use('Agg')
import numpy as np
import cv2
from matplotlib import pyplot as plt

kuva1 = cv2.imread('kuva.png',0)
kuva2 = cv2.imread('kuva2.png',0)

# Initiate SIFT detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(kuva1,None)
kp2, des2 = orb.detectAndCompute(kuva2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
kuva3 = cv2.drawMatches(kuva1, kp1, kuva2, kp2, matches, None, flags=2)

plt.imshow(cv2.cvtColor(kuva3, cv2.COLOR_BGR2RGB)), plt.imsave('foo.png', kuva3)
