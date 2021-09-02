import numpy as _np
import scipy.fftpack as _fft

def get_frequency_profile(time, field, pad_factor=0):
    '''

    '''

    n = int(_np.log(len(time) ) /_np.log(2.)) + 1.
    M_pad = 2. ** (n * pad_factor)
    added_pad = M_pad - len(time)
    print('Added pad = '+str(added_pad))

    if M_pad > 1:
        reduction_factor = _np.double(time)/M_pad
        added_zeros = _np.array(list(_np.zeros(_np.int(added_pad /2.))))
        field_zero_padded = added_zeros + list(field / sum(field)) + added_zeros
        print(str(added_pad) +' zeros added')

    elif M_pad == 1:  # it is actually no padded in this case.
        reduction_factor = 1.
        field_zero_padded = field /sum(field)
        print('No padding applied')

    frequency_components = _np.abs(_fft.fft(field_zero_padded))
    time_resolution = time[1] - time[0]
    frequency_resolution = 1./(time_resolution * len(field))
    frequency = reduction_factor *_np.arange(0, frequency_resolution * len(frequency_components), frequency_resolution)

    return frequency, frequency_components