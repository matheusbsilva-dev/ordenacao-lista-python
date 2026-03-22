lista = []
for n in range(1,6):
    v = int(input('digite um numero: '))
    lista.append(v)
c = sorted(lista)
print(f'a ordem de numero que voce digitou foi: {lista}')
print(f'a lista emm forma crescente: {c}')