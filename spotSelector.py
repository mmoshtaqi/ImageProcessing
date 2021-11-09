# importing everything we need
import cv2
import csv

VIDEO_SOURCE = 0
cap = cv2.VideoCapture(VIDEO_SOURCE)
while True:
  suc, image = cap.read()
  cv2.imshow('frame', image)
  if cv2.waitKey(1) & 0xFF == ord('c'):
    break

cv2.imwrite("frame0.jpg", image)
img = cv2.imread("frame0.jpg")
r = cv2.selectROIs('ROI Selector', img, showCrosshair=False, fromCenter=False)

rlist = r.tolist()
print(rlist)
with open('data/rois.csv', 'w', newline='') as outf:
  csvw = csv.writer(outf)
  csvw.writerows(rlist)

cap.release()
cv2.destroyAllWindows()
