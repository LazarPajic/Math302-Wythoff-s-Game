from wythoff.core import optimal_move
from wythoff.visualize import plot


def run_demo():
    print("=== Wythoff Demo ===")

    test_cases = [(2, 3), (5, 8), (10, 16), (7, 11)]

    for x, y in test_cases:
        print(f"State ({x}, {y}) -> {optimal_move(x, y)}")

    print("\nShowing visualization...")
    plot(35)


if __name__ == "__main__":
    run_demo()