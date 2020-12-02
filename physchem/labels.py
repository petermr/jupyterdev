from scipy.ndimage import label, generate_binary_structure

def filter_less_than(arr, k):
    return arr[np.nonzero(arr < k)]

def filter_equals(arr, k):
    print("arr", type(arr), arr.shape)
    foo = arr[np.nonzero(arr == k)]
    foo.reshape(arr.shape)
    print("foo", type(foo), foo.shape)
    return foo

def test1(image):
    s = ndimage.generate_binary_structure(2,1)
    labeled_array, numpatches = ndimage.label(image, s)
    sizes = ndimage.sum(image, labeled_array, range(1, numpatches + 1))
    max_label = np.where(sizes == sizes.max())[0] + 1
    output = np.asarray(labeled_array == max_label, np.uint8)

def label_binary(image_file, img_count=5, thresh=128):
    import os
    import numpy as np
    from PIL import Image
    from scipy.ndimage import label
    im_gray =np.array(Image.open(image_file).convert("L"))

    im_bool = im_gray > thresh
    maxval = 255

    im_bin = (im_gray > thresh) * maxval

    im_invert = (255 - im_bin)

    # https://stackoverflow.com/questions/52078231/get-a-quanity-of-pixels-with-specific-color-at-image-python-opencv

    Image.fromarray(np.uint8(im_bin)).save('numpy_binarization.png')

#    labeled, nr_objects = scipy.ndimage.label(im_bin, output=np.uint8)
#    im_bin_shaped= np.ndarray(shape=im_bin.shape, dtype=np.uint8)

#    labeled, nr_objects = scipy.ndimage.label(im_invert, output=np.uint8)
    labeled, nr_objects = label(im_invert)
    # index regions by size => index
    labels_by_size = {}
    for label in range(nr_objects):
        labels_by_size[np.count_nonzero(labeled == label)] = label;

# still learning this
#    sorted_regions_by_size = {k: v for k, v in sorted(regions_by_size.items(), key=lambda item: (item[0], item[1]), reverse=True)}
    sorted_regions_by_size = []
    labels_by_size_sorted = sorted(labels_by_size.items(), key=lambda item: item[0], reverse=True)

    count = 0 ## use enumerate later
    for labels_by_size in labels_by_size_sorted:
        if count >= img_count:
            break
        label = labels_by_size[1]

        #this reduces the size of the image - strips all zeros; can't yet make it work
        filtered_image = labeled[labeled != label]
        # take the simple route - much slower but works
        filtered_image = np.full(im_bin.shape, 255)

        for r in range(filtered_image.shape[0]):
            for c in range(filtered_image.shape[1]):
                val = labeled[r,c]
                if val == label:
                    filtered_image[r,c] = 0

        ff8 = filtered_image.astype(np.uint8)
        Image.fromarray(ff8).show()

        count += 1

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb

def segments():
    """ NOT YET USED """

    # apply threshold
    thresh = threshold_otsu(image)
    bw = closing(image > thresh, square(3))

    # remove artifacts connected to image border
    cleared = clear_border(bw)

    # label image regions
    label_image = label(cleared)
    # to make the background transparent, pass the value of `bg_label`,
    # and leave `bg_color` as `None` and `kind` as `overlay`
    image_label_overlay = label2rgb(label_image, image=image, bg_label=0)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_label_overlay)

    for region in regionprops(label_image):
        # take regions with large enough areas
        if region.area >= 100:
            # draw rectangle around segmented coins
            minr, minc, maxr, maxc = region.bbox
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                      fill=False, edgecolor='red', linewidth=2)
            ax.add_patch(rect)

    ax.set_axis_off()
    plt.tight_layout()
    plt.show()
