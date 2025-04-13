import random
import math

def random_noise():
    random_characters = ['$', '!', 'p', '-_-', ':D', '~', '@', '#']
    random_index = [random_characters[random.randint(0, len(random_characters) - 1)] for _ in range(4)]
    return ''.join(random_index)

def hypotenuse(x, y):  # Fixed parameter name (was 'b')
    return math.sqrt(x**2 + y**2)

if __name__ == "__main__":  # This prevents execution when imported
    print("TRY TO STOP THIS FROM BEING PRINTED IN FILE a.py WITHOUT DELETING THIS PRINT STATEMENT")
