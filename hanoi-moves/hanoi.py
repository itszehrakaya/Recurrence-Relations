def hanoi(n, src, ax, tgt):
    """
    Recursive function to solve Tower of Hanoi puzzle and list all the moves.
        n (int): Number of disks.
        src (str): Source peg.
        ax (str): Auxiliary peg.
        tgt (str): Target peg.
    """
    if n > 0:
        # Move n-1 disks from 'source' peg to auxiliary peg
        hanoi(n-1, src, tgt, ax)
        
        print(f"Move disk {n} from {src} to {tgt}")
        
        # Move n-1 disks from auxiliary peg to target peg
        hanoi(n-1, ax, src, tgt)


if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))
    print(f"Moves to solve Tower of Hanoi with {n} disks:")
    hanoi(n, "A", "B", "C")
