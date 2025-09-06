import numpy as np
import matplotlib.pyplot as mat

def unit_step(n):
    half = n // 2
    n_vec = np.arange(-half, -half + n)
    u = (n_vec >= 0).astype(int)
    mat.figure()
    mat.stem(n_vec, u,basefmt=" ")
    mat.title(f"Unit Step (length={n})")
    mat.xlabel("n")
    mat.ylabel("u[n]")
    mat.grid(True)
    mat.show()
    return u

def unit_impulse(n):

    half = n // 2
    n_vec = np.arange(-half, -half + n)
    delta = (n_vec == 0).astype(int)
    mat.figure()
    mat.stem(n_vec, delta, basefmt=" ")
    mat.title(f"Unit Impulse (length={n})")
    mat.xlabel("n")
    mat.ylabel("delta[n]")
    mat.grid(True)
    mat.show()
    return delta

def ramp_signal(n):
    half = n // 2
    n_vec = np.arange(-half, -half + n)
    ramp = np.where(n_vec >= 0, n_vec, 0).astype(float)
    mat.figure()
    mat.stem(n_vec, ramp, basefmt=" ")
    mat.title(f"Ramp Signal (length={n})")
    mat.xlabel("n")
    mat.ylabel("r[n]")
    mat.grid(True)
    mat.show()
    return ramp