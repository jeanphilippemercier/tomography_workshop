import eikonal.data as data
import cPickle as pickle
import numpy as np
from scipy.ndimage.filters import gaussian_filter
# Defining the model parameters

origin = (0, 0, 0)
spacing = (5, 5, 5)

# creating a velocity model with a background velocity of 5000 m/s
velocity = np.ones((101, 101, 101)) * 5000

# adding a zone of low velocity at the center of the model

velocity[40:61, 40:61, 40:61] = 1000

# smoothing the velocity model using a gaussian kernel
# tomography prefers smooth model

velocity = gaussian_filter(velocity, 1)

# creating the EKImageData object

EKVelocity = data.EKImageData(velocity, origin=origin, spacing=spacing)

# saving the file in pickle format

pickle.dump(EKVelocity, open('inversion/build/originalVelocity.pickle', 'w'))
