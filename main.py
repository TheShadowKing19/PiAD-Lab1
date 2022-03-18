import numpy as np

#  Tablice
a = np.array([1, 2, 3, 4, 5, 6, 7])
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Tablica jednowymiarowa:")
print(a)
print("\nTablica dwuwymiarowa:")
print(b)

print("\nTranspozycja tablicy b:")
b = np.transpose(b)
print(b)

print("\nTablica składająca sie ze 100 elementów:")
c = np.arange(0, 101)
print(c)

print("\nTablica 10 liczb z zakresu od 0 do 2:")
d = np.linspace(0, 2, 10)
print(d)

print("\nTablica wartości od 0 do 100 ze skokiem 5:")
e = np.arange(0, 105, 5)
print(e)


# Liczby Losowe
print("\nTablica 20 liczb losowych rozkładu normalnego, zaokrąglonych do dwóch miejsc po przecinku:")
f = np.random.rand(20)
f = np.around(f, 2)
print(f)

print("\nTablica 100 liczb całkowitych od 1 do 1000:")
g = np.random.randint(1, 1000+1, 100)
print(g)


zero_a = np.zeros((3, 2))
one_a = np.ones((3, 2))
print("\nMacierz 3x2 zer:")
print(zero_a)
print("\nMacierz 3x2 jedynek:")
print(one_a)

print("\nMacierz losowa 5x5 liczb całkowitych od 0 do 100 z typem danych 32bit:")
h = np.random.randint(0, 101, size=(5, 5), dtype=np.int32)
print(h)

# Zadania
print("\nTablica złożona z losowych liczb dziesiętnych od 0 do 10;")
a = np.random.default_rng().uniform(low=0.0, high=10.0, size=10)
print(a)

print("\nZmieniam typ danych na int i wstawiam do tablicy b:")
b = a.astype('int32')
print(b)

print("Zaokrąglam tablicę a do liczb całkowitych i zmieniam typ na int32:")
a = np.around(a, 0)
a = a.astype('int32')
print(a)
print("\nWnioski: Zdaje się, że niektóre wartości w tablicy 'a' zostały zaokrąglone, gdzie tablica 'b' została "
      "nieruszona (pomijąc zaokrąglenie")


# Selekcja danych

print("\n\nTworze tablice b:")
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], dtype=np.int32)
print(b)

print("\nSprawdzam ile wymiarów ma tablica b:")
print(b.ndim)

print("\nSprawdzam z ilu elementów składa się tablica b:")
print(b.size)

print("\nWybieram i wyświetlam '2' i '4' z tablicy b:")
print(b[0][1], b[0][3])

print("\nWybieram i wyświetlam pierwszy wiersz tablicy b:")
print(b[0])

print("\nWybieram i wyświetlam wszystkie wiersze z pierwszej kolumnny tablicy b:")
print(b[:, 0])

print("\nGeneruje macierz losową 20x7 z liczbami całkowitymi w przedziale od 0 do 100:")
rand_array = np.random.randint(0, 101, (20, 7))
print(rand_array)
print("\nNastępnie wyświetlam wszystkie wiersze pierwszych czterech kolumn:")
print(rand_array[:, 0:4])

# Działania matematyczne i logiczne

print("\n\nTworze dwa macierze liczb całkowitych z przedziału od 1 do 10 o rozmiarze 3x3:")
a = np.random.randint(1, 11, (3, 3))
b = np.random.randint(1, 11, (3, 3))
print(a)
print(b)
print("\nDodaje za pomocą znaku '+':")
print(a + b)
print("Dodaje za pomocą funkcji 'add()':")
print(np.add(a, b))
print("Odejmuje za pomocą znaku '-':")
print(a - b)
print("Odejmuje za pomocą funkcji 'subtract()':")
print(np.subtract(a, b))
print("Monoże za pomocą znaku '*':")
print(a * b)
print("Mnoże za pomocą funkcji 'multiply()':")
print(np.multiply(a, b))
print("Mnoże za pomocą funkcji 'dot()':")
print(np.dot(a, b))
print("Mnoże za pomocą funkcji 'matmul()':")
print(np.matmul(a, b))
print("Dziele za pomocą znaku '/':")
print(a / b)
print("Dziele za pomocą funkcji 'divide()':")
print(np.divide(a, b))
print("Potęguje za pomocą znaku '**':")
print(a ** b)
print("Potęguje za pomocą funkcji 'power()':")
print(np.power(a, b))

print("\nSprawdzam czy wartości macierzy 'a' są większe lub równe 4:")
print(np.where((a >= 4), True, False))

print("\nSprawdzam czy wartości macierzy 'a' są większe lub równe 1 i mniejsze lub równe 4:")
print(np.where((a >= 1) & (a <= 4), True, False))

print("\nObliczam sume elementów na przekątnej macierzy 'b':")
print(np.trace(b))

# Dane statystyczne

print("\n\nObliczam sume elementów macierzy 'b':")
print(np.sum(b))
print("Znajduję minimum macierzy 'b':")
print(np.amin(b))
print("Znajduję maksimum macierzy 'b':")
print(np.amax(b))
print("Obliczam odchylenie standardowe macierzy 'b':")
print(np.std(b))

print("\nObliczam średnią dla wierszy macierzy 'b':")
print(a.mean(axis=1))

print("\nObliczam średnią dla kolumn macierzy 'b':")
print(a.mean(axis=0))


# Rzutowanie wymiarów za pomocą reshape lub resize

print("\n\nTworzę tablicę składającą się z 50 liczb:")
a = np.arange(50)
print(a)

print("\nTworze macierz 10x5 z utworzonej tablicy za pomocą funkcji 'reshape()':")
b = a.reshape((10, 5))
print(b)

print("\nTworze macierz 10x5 z utworzonej tablicy za pomocą funkcji 'resize()':")
c = np.resize(a, (10, 5))
print(c)

print("\nFunkcja ravel() 'spłaszcza' macierz, czyli zamienią ją w tablice 1D:")
c = np.ravel(c)
print(c)

print("\nTworzę dwie tablice:")
a = np.arange(5)
b = np.arange(4)
print(a)
print(b)
print("Używam 'numpy.newaxis' by zwiększyć wymiary tablicy 'a'")
a = a[:, np.newaxis]
print(a)
print(b)
print("Dodaje je do siebie:")
print(a + b)
print("By dodać dwie tablice o różnych rozmiarach, należy zwiększyć wymiar jednej z jej. Wtedy numpy pozwoli nam je"
      "dodać do siebie, łącząc je i uzupełniając sam nową utworzoną macierz")


# Sortowanie danych

print("\n\nWprowadzam macierz 'a':")
a = np.random.randint(0, 100, size=(5, 5))
print(a)
print("Sortuje wiersze rosnąco")
print(np.sort(a))
print("Sortuję kolumny malejąco:")
print(np.sort(a, axis=0)[::-1])


print("\nWprowadzam macierz 'b':")
b = np.array([(1, 'MZ', 'mazowieckie'), (2, 'ZP', 'zachodniopomorskie'), (3, 'ML', 'małopolskie')])
print(b)
print("\nSortuje po drugiej kolumnie:")
b = b[b[:, 1].argsort()]
print(b)
print("\nNazwa województwa:")
print(b[2][2])


# Zadania podsumujące

# Zad 1
print("\n\nTworzę macierz 10x5 zawierająca liczby całkowite z przedziału od 0 do 100:")
a = np.random.randint(0, 101, (10, 5))
print(a)
print("Liczę sumę elementów głównej przekątnej tej macierzy za pomocą funkcji trace():")
print(np.trace(a))
print("Pobieram przekątną za pomocą funkcji diag():")
print(np.diag(a))

# Zad 2
print("\nTworze dwie macierze 5x5 z losowymi liczbami z przedziału normalnego:")
a = np.random.rand(5, 5)
b = np.random.rand(5, 5)
print(a, "\n")
print(b)
print("Mnożę...")
print(a * b)

# Zad 3
print("\nTworzę dwie tablice zawierające losowe liczby całkowite w zakresie od 1 do 100:")
a = np.random.randint(1, 100, 5)
b = np.random.randint(1, 100, 5)
print(a)
print(b)
print("Tworze z tablic macierze z 5 kolumnami:")
a = a[np.newaxis, :]
b = b[np.newaxis, :]
print(a)
print(b)
print("Dodaję je do siebie:")
print(a + b)

# Zad 4
print("\n\nTworzę macierze 4x5 i 5x4:")
a = np.random.randint(0, 101, size=(4, 5))
b = np.random.randint(0, 101, size=(5, 4))
print(a)
print(b)
print("Zmieniam rozmiar macierzy 5x4 na rozmiar kompatybilny z drugą macierzą, czyli 4x5")
b = np.resize(b, (4, 5))
print(b)
print("Następnie dodaję macierzę ze sobą:")
print(a + b)

# Zad 5
print("\n\nMnożę kolumne 3 i 4 pierwszej macierzy 'a':")
print(a[:, 2] * a[:, 3])
print("Mnoże kolumne 3 i 4 drugiej macierzy 'b':")
print(b[:, 2] * b[:, 3])

# Zad 6
print("\n\nGeneruję macierz o rozkładzie normalnym:")
a = np.random.normal(size=(5, 5))
print(a)
print("Średnia:")
print(np.mean(a))
print("Odchylenie standardowe:")
print(np.std(a))
print("Wariancja:")
print(np.var(a))
print("Suma elementów:")
print(np.sum(a))
print("Minimum macierzy:")
print(np.amin(a))
print("Maksimum macierzy:")
print(np.amax(a))
print("\nGeneruje macierz o rozkładzie jednostajnym:")
b = np.random.uniform(size=(5, 5))
print(b)
print("Średnia:")
print(np.mean(b))
print("Odchylenie standardowe:")
print(np.std(b))
print("Wariancja:")
print(np.var(b))
print("Suma elementów:")
print(np.sum(b))
print("Minimum macierzy:")
print(np.amin(b))
print("Maksimum macierzy:")
print(np.amax(b))

# Zad 7
print("\n\nTworzę dwie macierze:")
a = np.random.randint(0, 101, size=(3, 3))
b = np.random.randint(0, 101, size=(3, 3))
print(a, "\n")
print(b)
print("Mnożę macierzę za pomocą znaku '*':")
print(a * b)
print("Mnoże macierze za pomocą funkcji dot():")
print(np.dot(a, b))

# Zad 8
print("\n\nTworzę macierz:")
a = np.random.randint(0, 21, size=(5, 5))
print(a)
print("Jedno pole w macierzy zajmuję:")
print(a.itemsize, "bity")
print("Wyświetlam 5 kolumn z trzech pierwszych wierszy:")
print(np.lib.stride_tricks.as_strided(a, shape=(3, 5), strides=(20, 4)))

# Zad 9
print("\n\nTworze tablice:")
a = np.arange(5)
b = np.arange(5, 10)
print(a)
print(b)
print("Łączę je za pomocą funkcji stack():")
print(np.stack((a, b), axis=-1))
print("Łącze je za pomocą funkcji vstack():")
print(np.vstack((a, b)))

# Zad 10
print("\n\nTworzę macierz:")
a = np.arange(24).reshape((4, 6))
print(a)
print("Sumuję pierwszy blok (kremowy):")
print(np.sum(np.lib.stride_tricks.as_strided(a, shape=(2, 3), strides=(24, 4))))
print("Sumuję drugi blok (zielony):")
print(np.sum(np.lib.stride_tricks.as_strided(a+3, shape=(2, 3), strides=(24, 4))))
print("Sumuję trzeci blok (niebieski):")
print(np.sum(np.lib.stride_tricks.as_strided(a+12, shape=(2, 3), strides=(24, 4))))
print("Sumuję czwarty blok (czerwony):")
print(np.sum(np.lib.stride_tricks.as_strided(a+15, shape=(2, 3), strides=(24, 4))))

