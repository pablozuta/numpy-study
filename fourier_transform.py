import numpy as np 

# define a time domain signal
time_domain_signal = np.array([1, 2, 1, -1, 3])

# perform fourier transform
frequency_domain_signal = np.fft.fft(time_domain_signal)

# print the result
print("Fourier Transform Result: ", frequency_domain_signal)