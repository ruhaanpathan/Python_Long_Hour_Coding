import numpy as np
import matplotlib.pyplot as plt

def sine_wave(A, f, phi, t):
    y = A * np.sin(2 * np.pi * f * t + phi)
    plt.figure()
    plt.plot(t, y)
    plt.title(f"Sine wave: A={A}, f={f} Hz, phi={phi}")
    plt.xlabel("t (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y

def cosine_wave(A, f, phi, t):
    y = A * np.cos(2 * np.pi * f * t + phi)
    plt.figure()
    plt.plot(t, y)
    plt.title(f"Cosine wave: A={A}, f={f} Hz, phi={phi}")
    plt.xlabel("t (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y

def exponential_signal(A, a, t):
    y = A * np.exp(a * t)
    plt.figure()
    plt.plot(t, y)
    plt.title(f"Exponential: A={A}, a={a}")
    plt.xlabel("t (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y
