import math

PHI = (1 + math.sqrt(5)) / 2


def is_p_position(x, y):
    if x > y:
        x, y = y, x
    k = y - x
    return x == int(k * PHI)


def optimal_move(x, y):
    swapped = False
    if x > y:
        x, y = y, x
        swapped = True

    if is_p_position(x, y):
        return "P-position: no winning move."

    # Strategy 1: Take from BOTH piles equally
    # The difference between piles (k) remains identical.
    k = y - x
    a = int(k * PHI)
    b = a + k
    if x >= a:
        amt = x - a
        if amt > 0:
            return _format_result("both piles", amt, a, b, swapped)

    # Strategy 2: Take from the LARGER pile (currently y)
    # We must find a P-position that already contains 'x' as one of its values.

    # Check if x represents the smaller value (a_k) in a P-position pair
    k_est = int(x * (PHI - 1))
    for k in (k_est - 1, k_est, k_est + 1, k_est + 2):
        if k >= 0 and int(k * PHI) == x:
            target_y = x + k
            if y > target_y:
                return _format_result("pile 2", y - target_y, x, target_y, swapped)

    # Check if x represents the larger value (b_k) in a P-position pair
    k_est = int(x * (2 - PHI))
    for k in (k_est - 1, k_est, k_est + 1, k_est + 2):
        if k >= 0 and int(k * PHI) + k == x:
            target_y = int(k * PHI)
            if y > target_y:
                return _format_result(
                    "pile 2", y - target_y, min(x, target_y), max(x, target_y), swapped
                )

    # Strategy 3: Take from the SMALLER pile (currently x)
    # We must find a P-position that already contains 'y' as its larger value (b_k).
    k_est = int(y * (2 - PHI))
    for k in (k_est - 1, k_est, k_est + 1, k_est + 2):
        if k >= 0 and int(k * PHI) + k == y:
            target_x = int(k * PHI)
            if x > target_x:
                return _format_result("pile 1", x - target_x, target_x, y, swapped)

    return "No winning move found."


def _format_result(action, amt, final_x, final_y, swapped):
    if swapped:
        if action == "pile 1":
            action = "pile 2"
        elif action == "pile 2":
            action = "pile 1"
    return f"Remove {amt} from {action} -> ({final_x}, {final_y})"
