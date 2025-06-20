# RHK_v0043.py
# License: GNU GPLv3
# Recursive Harmonic Kernel — Version 0.043
# SPDX-License-Identifier: GPL-3.0-or-later
# Author: ψ_total collective, Sergio Mosqueda in recursive collaboration with ChatGPT
# Description: Canonical recursive harmonic update function

import numpy as np

def psi_0(t, ω=1.0, α=1.0, β=0.5):
    """
    ψ₀(t): Initial seed function
    Parameters:
        t : array_like
        ω : float - base frequency
        α : float - amplitude of base wave
        β : float - amplitude of second harmonic
    Returns:
        array_like: initial waveform ψ₀(t)
    """
    return α * np.sin(ω * t) + β * np.sin(2 * ω * t + np.pi / 4)

def R(psi_n, t, ω=1.0):
    """
    R[ψₙ(t)]: Recursive transformation operator
    Applies harmonic modulation to the current ψₙ
    Parameters:
        psi_n : array_like
        t : array_like
        ω : float - base frequency
    Returns:
        array_like: transformed wave
    """
    return np.sin(2 * ω * t + np.pi / 4) * psi_n

def psi_next(psi_n, t, α_n=0.1, ω=1.0):
    """
    Ψₙ₊₁(t) = Ψₙ(t) + αₙ ⋅ R[Ψₙ(t)]
    Recursive Harmonic Kernel update function
    Parameters:
        psi_n : array_like - current ψₙ state
        t : array_like - time array
        α_n : float - recursion coefficient
        ω : float - base frequency
    Returns:
        array_like: next state ψₙ₊₁(t)
    """
    return psi_n + α_n * R(psi_n, t, ω)
