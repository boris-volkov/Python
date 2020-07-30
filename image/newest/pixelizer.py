import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys

def make_pallate():
    pallate = []
    nums = [0,51,102,204,255]
    for i in nums:
        for j in nums:
            for k in nums:
                pallate.append(np.array([i,j,k]))
    return pallate

def lim_pal(triple_set):
    x = 0
    y = 0
    z = 0
    count = 0
    for i in triple_set:
        x += i[0]
        y += i[1]
        z += i[2]
        count += 1
    avg_pix = np.array([x//count, y//count, z//count])
    min_distance = (float('inf'))
    index = 0
    for i,v in enumerate(pallate):
        norm = np.linalg.norm(triple_set - v, ord=1)
        if  norm < min_distance:
            min_distance = norm
            index = i
    return pallate[index]

def myround(x, base=5):
    return base * round(x/base)

def round_triple(triple_set):
    x = 0
    y = 0
    z = 0
    count = 0
    for i in triple_set:
        x += i[0]
        y += i[1]
        z += i[2]
        count += 1
    x /= count
    y /= count
    z /= count
    bit_pixel = np.array([myround(x,10),myround(y,10),myround(z,10)])
    return bit_pixel

def average(triple_set):
    x = 0
    y = 0
    z = 0
    count = 0
    for i in triple_set:
        x += i[0]
        y += i[1]
        z += i[2]
        count += 1
    avg_pix = np.array([x//count, y//count, z//count])
    return avg_pix  

def pixelate(picture,pix_across, crop = True):
    pix_size = length//pix_across
    pix_down = height//pix_size
    new_picture = picture.copy()

    v_cutoff = (height - pix_size*pix_down)//2
    h_cutoff = (length - pix_size*pix_across)//2
    new_picture = new_picture[v_cutoff:v_cutoff+pix_size*pix_down, h_cutoff:h_cutoff+pix_size*pix_across]
    pixel_count = 0
    for i in range(pix_down):
        for j in range(pix_across):
            pixels = list()
            #averages pixels in a square block
            for a in range(pix_size//4,3*pix_size//4,2):
                for b in range(pix_size//4,3*pix_size//4,2):
                    pixels.append(new_picture[pix_size*i + a][pix_size*j + b]) 
            pixel_count += 1
            percent_done = ((pixel_count/(pix_down*pix_across))*100)//1
            print('     processing image: ' + str(percent_done) + '%', end = '\r')
            avg = round_triple(pixels)
            #rewrites the pixels to the average
            for a in range(pix_size):
                for b in range(pix_size):
                    new_picture[pix_size*i + a][pix_size*j + b] = avg

    print('\t'*4)
    return new_picture


def shrink(picture,pix_across):
    picture_copy = picture.copy()
    pix_size = length//pix_across
    pix_down = height//pix_size
    v_cutoff = (height - pix_size*pix_down)//2
    h_cutoff = (length - pix_size*pix_across)//2
    picture_copy = picture_copy[v_cutoff:v_cutoff+pix_size*pix_down, h_cutoff:h_cutoff+pix_size*pix_across]
    pixel_count = 0
    avg = list() 
    for i in range(pix_down):
        for j in range(pix_across):
            pixels = list()
            #averages pixels in a square area
            for a in range(pix_size//4,3*pix_size//4,2):
                for b in range(pix_size//4,3*pix_size//4,2):
                    pixels.append(picture_copy[pix_size*i + a][pix_size*j + b]) 
            #print('processing pixel ' + str(pixel_count)+' '+str(i)+':'+str(j))
            avg.append(round_triple(pixels))
            #rewrites the pixels to the average
            pixel_count += 1
            percent_done = ((pixel_count/(pix_down*pix_across))*100)//1
            print('     processing image: ' + str(percent_done) + '%', end = '\r')
    
    
    
    
    new_picture = np.zeros(shape=(pix_down, pix_across, 3)) 
    pixel_count = 0
    for i in range(pix_down):
        for j in range(pix_across):
            new_picture[i][j] = avg[pixel_count]
            pixel_count += 1
    return new_picture

def contrast(image):
    img = image.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j][0] < 255/2:
                img[i,j] = 0.9*img[i,j]
            else: 
                img[i,j] = np.minimum(img[i,j]*1.1, np.array([255,255,255])) 

    return img

if __name__ == '__main__':
    color_img = Image.open('frames/' + sys.argv[1])
    image_matrix = np.array(color_img)
    height = (len(image_matrix))
    length = (len(image_matrix[0]))
    pixelated = pixelate(image_matrix, int(sys.argv[2]))
    #print('pixelated type : ' + str(type(pixelated)))
    down_cast = pixelated.astype(dtype=np.uint8) 
    #print('downcast type : ' + str(type(down_cast)))
    #print(type(down_cast[1][1][1]))
    if sys.argv[3] and sys.argv[3] == 's':
        result = Image.fromarray(down_cast)
        result.save('pixelated/pixel_' + sys.argv[1])
        print('image written : ' + sys.argv[1])
    else:
        plt.imshow(pixelated)
        plt.show()
