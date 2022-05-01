import numpy  as np
import cv2
import matplotlib.pyplot as plt

class convolution_2D:

    def __init__(self):
        pass

    def load_image(self,image_path,width,height):
        '''Load the images and convert them to numpy array'''
        #Convert the image to grayscale
        image = cv2.imread(image_path, 0)
        image = cv2.resize(image, (width,height))
        #image = np.asarray(image, dtype = np.uint8)
        return image

    def convolution(self,image,kernel):
        '''
        Build a 2D convolution model
        Return the convolution output
        Also we use a 3*3 kernel
        The image used is grey scale so convert the images to grey scale
        '''
        #DoubleFlip the mask
        k = np.flipud(np.fliplr(kernel))
        #create a numoy array to store the output
        output = np.zeros_like(image) 

        #create padding
        pad_image = np.zeros((image.shape[0]+2, image.shape[1]+2))
        pad_image[1:image.shape[0]+1,1:image.shape[1]+1] = image

        #Run the convolution
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                output[y,x] = (kernel * (pad_image[y:y+3,x:x+3])).sum()
        
        return output

    def display(self,image):
        cv2.imshow('Image:', image)
        while True:
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        return cv2.destroyAllWindows()


if __name__ == '__main__':

    image = '/home/mainak/Pictures/beautiful.jpg'

    conv = convolution_2D()
    im = conv.load_image(image,720,720)
    conv.display(im)
    kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])/9.0
    output = conv.convolution(im,kernel)
    conv.display(output)


