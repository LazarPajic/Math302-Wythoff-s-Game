from wythoff.core import optimal_move 

def play():
    print("=== Wythoff's Game ===")
    
    # Validate initial setup
    while True:
        try:
            x = int(input("Initial Pile 1: "))
            y = int(input("Initial Pile 2: "))
            if x >= 0 and y >= 0:
                break
            print("Pile sizes must be non-negative.")
        except ValueError:
            print("Please enter valid integers.")

    player = 1

    while x > 0 or y > 0:
        print(f"\n--- Player {player}'s Turn ---")
        print(f"State: ({x}, {y})")
        print("Optimal:", optimal_move(x, y))

        valid_move = False
        while not valid_move:
            try:
                move_input = input("Move (e.g., '1 5' for 5 from pile 1, or 'both 3'): ").lower().split()

                if len(move_input) != 2:
                    print("Warning: Invalid format. Use '[pile] [amount]' or 'both [amount]'.")
                    continue

                action = move_input[0]
                amt = int(move_input[1])

                if amt <= 0:
                    print("Warning: Amount must be greater than 0.")
                    continue

                if action == "both":
                    if amt <= x and amt <= y:
                        x -= amt
                        y -= amt
                        valid_move = True
                    else:
                        print(f"Warning: Cannot take {amt} from both. Piles are ({x}, {y}).")
                elif action == "1":
                    if amt <= x:
                        x -= amt
                        valid_move = True
                    else:
                        print(f"Warning: Pile 1 only has {x} items.")
                elif action == "2":
                    if amt <= y:
                        y -= amt
                        valid_move = True
                    else:
                        print(f"Warning: Pile 2 only has {y} items.")
                else:
                    print("Warning: Invalid pile selection. Choose '1', '2', or 'both'.")
            except ValueError:
                print("Warning: Amount must be an integer.")

        # Check win condition
        if x == 0 and y == 0:
            print(f"\nState: (0, 0)")
            print(f"Player {player} wins!")
            break

        player = 2 if player == 1 else 1

if __name__ == "__main__":
    play()