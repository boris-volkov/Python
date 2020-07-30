import numpy as np
from matplotlib.colors import rgb_to_hsv
from PIL import Image
import os, cv2, sys

print_buffer = []

class Movie():
    def __init__(self):
        self.frame_buffer = []

def normalize(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(3):
                matrix[i][j][k] /= 256

blocks = [' ', '\u2591', '\u2592', '\u2593', '\u2588']
def average_brightness(nums):
    z = 0
    count = 0
    for i in nums:
        z += i
        count += 1
    avg_brightness = z/count
    return avg_brightness

def pixelate(picture, pix_across, hwr = 2): #input number of pixels across of the target image

    height = (len(picture))
    length = (len(picture[0]))
    
    height_to_width_ratio = hwr

    # these are pixels of the input image
    pix_width = length//pix_across
    pix_height = pix_width * hwr
    pix_down = height//(pix_height)

    new_picture = picture.copy()
    v_cutoff = (height - pix_height*pix_down)//2
    h_cutoff = (length - pix_width*pix_across)//2

    print(v_cutoff)
    print(h_cutoff)
    
    new_picture = new_picture[v_cutoff:v_cutoff+pix_height*pix_down, h_cutoff:h_cutoff+pix_width*pix_across]

    brightness_values = [[0]*pix_across for _ in range(pix_down)]
    
    print(np.shape(new_picture))

    pixel_count = 0
    print(height)
    print(length)
    for i in range(pix_down):
        for j in range(pix_across):
            pixels = list()
            #averages pixels in a square area
            for a in range(pix_height):
                for b in range(pix_width):
                    pixels.append(new_picture[pix_height*i + a][pix_width*j + b][2]) # grab just the brightness val 
            pixel_count += 1
            avg = average_brightness(pixels)
            #rewrites the pixels to the average
            
            
            brightness_values[i][j] = blocks[int(round(avg*4))]

    return brightness_values

if __name__ == '__main__':
    import time

    if sys.argv[2] == '-w':
        import sys
        video = sys.argv[1]
        vidcap = cv2.VideoCapture(video)
        success, image = vidcap.read()
        count = 1
        while success:
          cv2.imwrite("frames/frame%s.png" % str(count).zfill(6), image)     # save frame as png or JPEG file      
          success,image = vidcap.read()
          print('Read a new frame: ' + str(count), success)
          count += 1

        import pickle
        obj = Movie()

        for frame in sorted(os.listdir('frames')):
            img = Image.open('frames/' + frame)
            image_matrix = np.array(img, dtype = float)
            normalize(image_matrix)
            converted = rgb_to_hsv(image_matrix)
            val = pixelate(converted, 80)
            #val = pixelate(converted, os.get_terminal_size()[0])
            obj.frame_buffer.append(val)

        pickle.dump(obj, open('save.p', 'wb'))
   
    else:
        import pickle
        mov = pickle.load(open('save.p', 'rb'))
    
        for frame in mov.frame_buffer:
            print("\033c")
            for lin in frame:
                print(''.join(lin))
            time.sleep(.05)


