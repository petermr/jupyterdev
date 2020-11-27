
class Tesseract:
    # https://pypi.org/project/pytesseract/
    # top
    from PIL import Image

    import pytesseract
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    %matplotlib inline

    from skimage import data, img_as_float
    from skimage import exposure
    from skimage.viewer import ImageViewer


    TEST_PNG = os.path.join(PHYSCHEM_IMAGES, 'capacitycycle.png'))

    if __name__ == '__main__':
        test

    def __init__(self, png, debug=False):
        self.png = png
        self.debug = debug
#        self.image = Image.open(self.png, 'r')


        # If you don't have tesseract executable in your PATH, include the following:
        # pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
        # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


    def get_strings(self):
        if (tesseract_strings == None and not self.png == None):
            self.tesseract_strings = pytesseract.image_to_string(Image.open(self.png))

            if self.debug:
                print(self.tesseract_strings)

    # In order to bypass the image conversions of pytesseract, just use relative or absolute image path
    # NOTE: In this case you should provide tesseract supported images or tesseract will return error
    # print(pytesseract.image_to_string('test.png'))

    # Batch processing with a single file containing the list of multiple image file paths
    # print(pytesseract.image_to_string('images.txt'))

    # Timeout/terminate the tesseract job after a period of time
    """
    try:
        print(pytesseract.image_to_string('test.jpg', timeout=2)) # Timeout after 2 seconds
        print(pytesseract.image_to_string('test.jpg', timeout=0.5)) # Timeout after half a second
    except RuntimeError as timeout_error:
        # Tesseract processing is terminated
        pass
    """
    # Get bounding box estimates
    def get_bounding_boxes(self):
        if self.bboxes == None:
            self.bboxes = pytesseract.image_to_boxes(Image.open(self.png))
            if self.debug:
                print(self.bboxes[:100], "\n...\n", self.bboxes[-100:])
        return bboxes

    def get_chunks(self):
    # Get verbose data including boxes, confidences, line and page numbers
        if self.chunks == None and not self.png == None:
            self.chunks = pytesseract.image_to_data(Image.open(self.png))
            if self.debug:
                print(type(self.chunks),"\n", self.chunks[:200], "\n...\n", self.chunks[-200:])
        return self.chunks

    def get_image_script(self):
    # Get information about orientation and script detection
        osd = pytesseract.image_to_osd(Image.open(test_png))
        if debug:
            print(osd)
        return osd

    def create_pdf(self):
        # Get a searchable PDF
        pdf = pytesseract.image_to_pdf_or_hocr(test_png, extension='pdf')
        if debug:
            print(pdf)
        return pdf

    def create_hocr(self):
    # Get HOCR output
        hocr = pytesseract.image_to_pdf_or_hocr(test_png, extension='hocr')
        if debug:
            print(hocr)
        return hocr

    @staticmethod
    def test0(test_png=TEST_PNG):
        tesseract = Tesseract()
