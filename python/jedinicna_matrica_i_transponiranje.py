def jedinicnaMatrica(N):
    """
    Funkcija prima cijeli broj N i vraća jediničnu matricu dimenzija (NxN)
    """
    #matrica = [[1 if j==i else 0 for j in range(N)] for i in range(N)] Rješenje s list comprehension
    matrica = []
    for i in range(N):
        redak = [0] * N
        redak[i] = 1
        matrica.append(redak)
    return matrica

N = 5
matrica = jedinicnaMatrica(N)
print(matrica); print()

def lijepaMatrica(matrica):
    """
    Funkcija prima jediničnu matrixu u plošnom obliku (rezultat funkcije jedinicnaMatrica()) 
    te ju ispisuje na vizualno uobičajen način
    """
    r = s = len(matrica)
    print(f"({r}x{s}):")
    print(*matrica, sep="\n")

lijepaMatrica(matrica); print()

def transponiraj(matrica):
    """
    Funkcija prima 2-d matricu te ju transponira (vraća njenu transponiranu verziju)
    """
    n_stupaca = len(matrica[0])
    transponirana = [[j[i] for j in matrica] for i in range(n_stupaca)]
    return transponirana

def main():
    """
    Početna (glavna) funkcija. Središnji dio iz kojeg se dalje pozivaju potrebne funkcije
    """
    matrica = [[4, 2, 5], [6, 9, 5], [0, 0, 5], [5, 5, 5]]
    r_mat, s_mat = len(matrica), len(matrica[0])
    print(f"Prije transponiranja ({r_mat}x{s_mat}): {matrica}")
    transponirana_matrica = transponiraj(matrica)
    r_tran, s_tran = len(transponirana_matrica), len(transponirana_matrica[0])
    print(f"Nakon transponiranja ({r_tran}x{s_tran}): {transponirana_matrica}")
    return

if __name__ == "__main__":
    main()