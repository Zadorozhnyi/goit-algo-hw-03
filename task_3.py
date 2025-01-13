def hanoi(n, source, target, auxiliary, state):

    # Recursive solution to the Towers of Hanoi problem.
    
    # :param n: number of disks
    # :param source: initial rod
    # :param target: destination rod
    # :param auxiliary: auxiliary rod
    # :param state: current state of the rods

    if n > 0:
        # Move n-1 disks from the initial core to the auxiliary core
        hanoi(n - 1, source, auxiliary, target, state)

        # Movement logging
        disk = state[source].pop()  # Take the top disk from the source
        state[target].append(disk)  # Put it on the destination rod
        print(f"Move the disk from {source} on {target}: {disk}")
        print(f"Intermediate state: {state}")

        # Move n-1 disks from the auxiliary rod to the destination rod
        hanoi(n - 1, auxiliary, target, source, state)

# Initial data
n = int(input("Enter the number of disks: "))
state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}

print(f"Initial state: {state}")
hanoi(n, 'A', 'C', 'B', state)
print(f"Final state: {state}")
