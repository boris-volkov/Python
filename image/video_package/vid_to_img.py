import cv2
import sys

if __name__ == '__main__':
    video = sys.argv[1]
    vidcap = cv2.VideoCapture(video)
    success,image = vidcap.read()
    count = 1
    while success:
      cv2.imwrite("frames/frame%s.png" % str(count).zfill(6), image)     # save frame as png or JPEG file      
      success,image = vidcap.read()
      print('Read a new frame: ' + str(count), success)
      count += 1
