import math
import matplotlib.pyplot as plt
import numpy as np

PHI = (1 + math.sqrt(5)) / 2

def p_positions(n):
    pts = []
    for k in range(n):
        a = int(k * PHI)
        b = a + k
        pts.append((a, b))
        # Add the symmetric equivalent, avoiding duplicating (0,0)
        if a != b: 
            pts.append((b, a))
    return pts

def p_positions_non_reflection(n):
    pts = []
    for k in range(1,n):
        a = int(k* PHI)
        b = a + k 
        pts.append((a,b))
    return pts

def plot(n=20):
    pts = p_positions(n)
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]

    # Force a square figure so the symmetry is visually accurate
    plt.figure(figsize=(8, 8)) 
    
    plt.scatter(xs, ys, color='blue', alpha=0.7, label='P-positions')
    
    # Add a diagonal dashed line (y = x) to highlight the symmetry
    max_val = max(max(xs), max(ys)) if xs else 10
    plt.plot([0, max_val], [0, max_val], 'r--', alpha=0.5, label='Pile 1 = Pile 2')

    plt.title("Wythoff's Game P-positions")
    plt.xlabel("Pile 1")
    plt.ylabel("Pile 2")
    
    # Add gridlines and a legend for clarity
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.show()

def plot_convergence(n=100):
    pts = p_positions_non_reflection(n)
    ab_dividea = [(p[1] + p[0])/p[1] for p in pts]
    a_divideb = [p[1]/p[0] for p in pts]

    plt.plot(range(n-1), ab_dividea, 'r', alpha=0.5, label='(a+b)/a')
    plt.plot(range(n-1), a_divideb, 'b', alpha=0.5, label='a/b')

    plt.xlabel(f'first {n} P-positions (Exclude (0,0))')
    plt.ylabel('Value')
    plt.title(f'P-position Convergence on Golden Ratio')

    plt.yticks(np.arange(1.5,2,0.05))

    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot(20) # Lowered the default for testing so individual dots are clearer