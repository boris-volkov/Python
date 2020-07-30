import cv2
import os
import sys
from natsort import ns, natsorted

if __name__ == '__main__':
    image_folder = sys.argv[1]
    video_name = 'video.avi'
    fps = int(sys.argv[2])
    imgs = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images = list(natsorted(imgs, alg=ns.IGNORECASE))
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    #video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 30, (width,height))
    video = cv2.VideoWriter(video_name, 0, fps, (width,height))
    

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

    print('video written: ' +str(len(imgs))+ ' frames')
