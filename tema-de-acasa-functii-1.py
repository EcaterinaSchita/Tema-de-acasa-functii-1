a = int(input('a='))
b = int(input('b='))


def suma(a, b):
    sum = a + b
    return sum
    
print(suma(a, b))    

def produs(a, b):
    prod = a * b
    return prod

print(produs(a, b))

def media(a, b):
    med = (a + b) / 2
    return med

print(media(a, b))

def divizori(a, b):
    comuni = []

    for i in range(1, int(max(a, b) / 2) + 1):
        if a % i == 0 and b % i == 0:
            comuni.append(i)

    return comuni


def divizormaximal():
    div = divizori(a, b)
    maxdiv = div[0]

    for i in range(1, len(div)):
        if div[i] > maxdiv:
            maxdiv = div[i]

    return maxdiv

print(divizormaximal())


def multipli(a, b):
    multiplia = []
    multiplib = []
    comuni = []

    for i in range(1, max(a, b)):
        multiplia.append(a*i)
        multiplib.append(b*i)

    for i in multiplia:
        if i in multiplib:
            comuni.append(i)

    return comuni[0:5]


def multipluminimal():
    multipli = multipli(a, b)
    minimal = multipli[0]

    for i in range(1, len(multipli)):
        if multipli[i] < minimal:
            minimal = multipli[i]

    return minimal

print(multipluminimal())

def minim(a, b):
    if (a < b):
        return a
    else:
        return b

print(minim(a, b))


def maxim(a, b):
    if (a > b):
        return a
    else:
        return b

print(maxim(a, b))

def suma2(a, b):
    return str(a) + ' + ' + str(b) + ' = ' + str(suma(a, b))

print(suma2(a, b))

def produs2(a, b):
    return str(a) + ' * ' + str(b) + ' = ' + str(produs(a, b))

print(produs2(a, b))


def cifrecomune(a, b):
    cifre = []

    for i in str(a):
        for j in str(b):
            if i == j:
                cifre.append(i)

    return cifre


print(cifrecomune(a, b))

def cifrediferite(a, b):
    cifre = []

    for i in str(a):
        if i not in str(b):
            cifre.append(i)

    return cifre

print(cifrediferite(a, b))

def cifreprietene(a, b):
    diva = []
    divb = []

    for i in range(1, int(a / 2) + 1):
        for j in range(1, int(b / 2) + 1):
            if a % i == 0:
                diva.append(i)
            if b % j == 0:
                divb.append(j)

    if len(diva) == len(divb):
        return "PRIETENE"
    else:
        return "Cifrele nu sunt prietene"

print(cifreprietene(a, b))
