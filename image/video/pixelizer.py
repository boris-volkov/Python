import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys

def bit_8(triple_set):
    x = 0
    y = 0
    z = 0
    count = 0
    for i in triple_set:
        x += i[0]
        y += i[1]
        z += i[2]
        count += 1
    def simplify(n):
        return (n*6/256)*36
    bit_pixel = np.array([simplify(x//count), simplify(y//count), simplify(z//count)])
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
            #averages pixels in a square area
            for a in range(pix_size):
                for b in range(pix_size):
                    pixels.append(new_picture[pix_size*i + a][pix_size*j + b]) 
            pixel_count += 1
            percent_done = ((pixel_count/(pix_down*pix_across))*100)//1
            print('     processing image: ' + str(percent_done) + '%', end = '\r')
            #print('processing pixel ' + str(pixel_count)+' '+str(i)+':'+str(j))
            avg = bit_8(pixels)
            #rewrites the pixels to the average
            for a in range(pix_size):
                for b in range(pix_size):
                    new_picture[pix_size*i + a][pix_size*j + b] = avg

    print('\n')
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
    color_img = Image.open(sys.argv[1])
    image_matrix = np.array(color_img)
    height = (len(image_matrix))
    length = (len(image_matrix[0]))
    pixelated = pixelate(image_matrix, int(sys.argv[2]))
    picture_count = 1
    if sys.argv[3] and sys.argv[3] == 's':
        result = Image.fromarray(pixelated)
        result.save('pixel_' + picture_count)
        picture_count += 1
        print('image written')
    else:
        plt.imshow(pixelated)
        plt.show()
