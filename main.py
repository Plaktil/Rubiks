import numpy as np

def main():
    x = np.array([[-1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1]])

    y = np.array([-1, 1, 1])

    z = np.matmul(y, x)
    print(z)

main()