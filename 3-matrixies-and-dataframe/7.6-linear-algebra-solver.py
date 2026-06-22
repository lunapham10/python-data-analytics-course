import numpy as np

def main():
    number_coefficients = int(input("Number of coefficients: "))

    A = []
    B = []
    for i in range (number_coefficients):
        line = input("Coefficients of equation {eq}: ")
        parts = [float(x) for x in line.split()]

        A.append(parts[:-1])
        B.append(parts[-1])
    
    A = np.array(A)
    B = np.array(B)

    solution = np.linalg.solve(A, B)
    print(f"List of coefficit is: {solution}")

if __name__ == "__main__":
    main()