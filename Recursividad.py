__author__ = 'Daniel Garcia Alonso'


def decimalABinario(decimal2):
    if decimal2 == 0:
        return 0

    binario=''
    decimal2 = int(decimal2)
    while (decimal2 > 0):
        binario+= str(decimal2%2)
        decimal2 = int(decimal2/2)

    return binario[::-1]

print(decimalABinario(212))
