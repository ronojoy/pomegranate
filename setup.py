from distutils.core import setup
from distutils.extension import Extension
import numpy as np

try:
    from Cython.Build import cythonize
except ImportError:
    use_cython = False
    ext = 'c'
else:
    use_cython = True
    ext = 'pyx'

filenames = [ "base",
              "BayesianNetwork",
              "FactorGraph",
              "distributions",
              "fsm",
              "hmm",
              "gmm"
            ]

if not use_cython:
    extensions = [
        Extension( "pomegranate.{}".format( name ), 
                   [ "pomegranate/{}.{}".format( name, ext ) ], 
                   include_dirs=[np.get_include()] ) for name in filenames
    ]
else:
    extensions = [
            Extension( "pomegranate.*", 
                       [ "pomegranate/*.pyx" ], 
                       include_dirs=[np.get_include()] )
    ]

    extensions = cythonize( extensions )

setup(
    name='pomegranate',
    version='0.2.6',
    author='Jacob Schreiber',
    author_email='jmschreiber91@gmail.com',
    packages=['pomegranate'],
    url='http://pypi.python.org/pypi/pomegranate/',
    license='LICENSE.txt',
    description='Pomegranate is a graphical models library for Python, implemented in Cython for speed.',
    ext_modules=extensions,
    install_requires=[
        "cython >= 0.20.1",
        "numpy >= 1.8.0",
        "scipy >= 0.13.3",
        "networkx >= 1.8.1",
        "matplotlib >= 1.3.1"
    ],
)
