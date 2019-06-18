from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

pyx_files = [Extension('imageProcessingCython', ['imageprocessing.pyx'])]
setup(
    ext_modules = cythonize(pyx_files)
)
