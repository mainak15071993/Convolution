from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = '2D_Convolution'
LONG_DESCRIPTION = 'Convolution for 2D images(grayscale)'

# Setting up
setup(
       # the name must match the folder name 'innner folder inside the main folder'
        name = "convolution", 
        version = VERSION,
        author = "Mainak Sen",
        author_email = "<93mainak@gmail.com>",
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        #packages = find_packages(),
        packages = ['convolution'],
        install_requires = ['numpy','matplotlib','opencv-python'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords = ['python', 'convolution'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            'Operating System :: POSIX :: Linux'
        ]
)
