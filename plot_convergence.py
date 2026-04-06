"""
plot_convergence.py
-------------------
This program shows how the P-positions in Wythoff's game converge towards the Golden ratio
(1 + sqrt(5)) / 2

Usage:
    python plot_convergence.py
"""

from wythoff.visualize import plot_convergence


def run_plot():
    plot_convergence(200)


if __name__ == "__main__":
    run_plot()
