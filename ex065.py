v = int(input('Digite um valor: '))
vm = v
vma = v
t = 0
nd = 1
t += v
while v != -1:
    v = int(input('Digite outro valor (Digite "-1" para sair)'))
    t += v
    nd += 1
    if v != -1:
        if v < vm:
            vm = v
        if v > vma:
            vma = v
print('''   O maior valor digitado foi {} e o menor foi {}
      A media entre os valores é de {:.1f} e a soma dos mesmos é de {}'''.format(vma, vm, (t+1) / (nd-1), t+1))