import math
import matplotlib.pyplot as plt

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

if __name__ == "__main__":
    plot(20) # Lowered the default for testing so individual dots are clearer