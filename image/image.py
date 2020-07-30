import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys

img = Image.open('hailey.jpg')
img2 = Image.open('philip.jpg')
t = np.array(img)//2 + np.array(img2)//2
p = np.array(img2)
rand = np.random.randint(1,255,size=(200,200))


#plt.imshow(color_img)
#plt.show()
color_img = Image.open('tahoe.JPG')
image_matrix = np.array(color_img)

#plt.imshow(image_matrix)
#plt.show()
height = (len(image_matrix))
length = (len(image_matrix[0]))
colors = (len(image_matrix[0][0]))
print(str(height)+' x '+str(length)+' x '+str(colors))
print('total size = ' + str(image_matrix.size))
print(height * length * colors)


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

    if crop:
        v_cutoff = (height - pix_size*pix_down)//2
        h_cutoff = (length - pix_size*pix_across)//2
        print(v_cutoff)
        print(h_cutoff)
        print(pix_size)
        new_picture = new_picture[v_cutoff:v_cutoff+pix_size*pix_down, h_cutoff:h_cutoff+pix_size*pix_across]
        print(np.shape(new_picture))
    pixel_count = 0
    print(height)
    print(length)
    for i in range(pix_down):
        for j in range(pix_across):
            pixels = list()
            #averages pixels in a square area
            for a in range(pix_size):
                for b in range(pix_size):
                    pixels.append(new_picture[pix_size*i + a][pix_size*j + b]) 
            print(str(pixel_count)+' '+str(i)+':'+str(j))
            pixel_count += 1
            avg = average(pixels)
            #rewrites the pixels to the average
            for a in range(pix_size):
                for b in range(pix_size):
                    new_picture[pix_size*i + a][pix_size*j + b] = avg

    if crop:
        return new_picture


    for i in range( pix_down ):
        pixels = list()
        for a in range( pix_size ):
            for b in range( length - pix_across, length ):
                pixels.append( new_picture[pix_size*i+a][b])
        avg = average(pixels)
        for a in range( pix_size ):
            for b in range( length - pix_across, length ):
                new_picture[pix_size*i+a][b] = avg

    for j in range( pix_across ):
        pixels = list()
        for a in range( height - pix_down, height ):
            for b in range( pix_size ):
                pixels.append( new_picture[a][pix_size*j+b])
        avg = average(pixels)
        for a in range( height - pix_down, height ):
            for b in range( pix_size ):
                new_picture[a][pix_size*j+b] = avg

    pixels = list()
    for a in range( height - pix_down, height):
        for b in range( length - pix_across, length):
            pixels.append( new_picture[a][b] )
    avg = average(pixels)
    for a in range( height - pix_down, height):
        for b in range( length - pix_across, length):
            new_picture[a][b] = avg

    return new_picture

pa = 10

#plt.imshow(pixelate(image_matrix, pa))
#plt.show()
#make the function that does this
#Crop = np.vstack(border, pic, border)

#print(p.size)

def contrast(image):
    img = image.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j][0] < 255/2:
                img[i,j] = 0.9*img[i,j]
            else: 
                img[i,j] = np.minimum(img[i,j]*1.1, np.array([255,255,255])) 

    return img

#pic = contrast(p)
#plt.imshow(t, cmap=plt.cm.binary)
#plt.show()
#plt.imshow(pic, cmap=plt.cm.binary)
#plt.show()

if __name__ == '__main__':
    color_img = Image.open(sys.argv[1])
    image_matrix = np.array(color_img)
    height = (len(image_matrix))
    length = (len(image_matrix[0]))
    pixelated = pixelate(image_matrix, int(sys.argv[2]))
    plt.imshow(pixelated)
    plt.show()
    if sys.argv[3] and sys.argv[3] == 's':
        result = Image.fromarray(pixelated)
        result.save('out.jpg')
