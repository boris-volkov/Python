import cv2
import sys

if __name__ == '__main__':
    video = sys.argv[1]
    vidcap = cv2.VideoCapture(video)
    success,image = vidcap.read()
    count = 0
    while success:
      cv2.imwrite("frame%d.png" % count, image)     # save frame as JPEG file      
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1
