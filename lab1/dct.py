#import scipy.fftpack.dct
from scipy.fftpack import dct
import numpy as np

#using dct from scipy.fftpack to transform input array using dct
print(dct(np.array([4.,3.,5.,10.]),1))