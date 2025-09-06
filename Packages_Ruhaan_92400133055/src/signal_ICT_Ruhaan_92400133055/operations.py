import numpy as np

def time_shift(signal, k):
    k = int(k)
    if k == 0:
        return signal.copy()
    if k > 0:
        return np.concatenate((np.zeros(k, dtype=signal.dtype), signal.copy()))
    # k < 0
    kpos = -k
    if kpos >= len(signal):
        return np.zeros(len(signal), dtype=signal.dtype)
    shifted = np.concatenate((signal[kpos:].copy(), np.zeros(kpos, dtype=signal.dtype)))
    return shifted

def time_scale(signal, k):
    if k <= 0:
        raise ValueError("k must be positive")
    x = np.asarray(signal)
    n = np.arange(len(x))
    new_len = int(np.floor(k * (len(x) - 1))) + 1
    new_n = np.arange(new_len)
    # sample x at positions new_n / k
    y = np.interp(new_n / k, n, x)
    return y

def _pad_to_same_len(a, b):
    la, lb = len(a), len(b)
    if la == lb:
        return a.copy(), b.copy()
    L = max(la, lb)
    a_p = np.concatenate((a, np.zeros(L - la, dtype=a.dtype)))
    b_p = np.concatenate((b, np.zeros(L - lb, dtype=b.dtype)))
    return a_p, b_p

def signal_addition(signal1, signal2):
    a, b = _pad_to_same_len(np.asarray(signal1), np.asarray(signal2))
    return a + b

def signal_multiplication(signal1, signal2):
    a, b = _pad_to_same_len(np.asarray(signal1), np.asarray(signal2))
    return a * b
