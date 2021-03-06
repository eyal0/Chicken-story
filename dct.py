#!python

from scipy.fftpack import dct, idct

# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

def viewable(orig):
    im = orig.copy()
    # make im viewable by scaling it all to the 0..1 range
    max_im = max(im[y][x]
                  for y in range(len(im))
                  for x in range(len(im[y])))
    min_im = min(im[y][x]
                  for y in range(len(im))
                  for x in range(len(im[y])))
    for y in range(len(im)):
        for x in range(len(im[y])):
            im[y][x] = (im[y][x]-min_im)/(max_im-min_im)
    return im


from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt
from skimage.transform import rescale, resize, downscale_local_mean

plt.gray()
orig = rgb2gray(imread('dog.jpg'))
orig = resize(orig, (100,100))

# plot original and reconstructed images with matplotlib.pylab
plt.subplot(3,2,1)
plt.imshow(orig)
plt.axis('off')

imF = dct2(orig)
plt.subplot(3,2,2)
plt.imshow(viewable(imF))
plt.axis('off')

fraction = 10
for y in range(len(orig)):
    for x in range(len(orig[y])):
        if x > len(orig[y])//fraction or y > len(orig)//fraction:
            # blacken pixels that aren't in the top left corner
            orig[y][x] = 0
            imF[y][x] = 0
im1 = idct2(imF)

plt.subplot(3,2,4)
plt.imshow(viewable(imF))
plt.axis('off')

plt.subplot(3,2,5)
plt.imshow(orig)
plt.axis('off')

plt.subplot(3,2,6)
plt.imshow(im1)
plt.axis('off')
plt.show()
