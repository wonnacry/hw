N = int(input())
Msr = int(input())
while N != 0 and Msr != 0:
    N -= 1
    Msr -= 0.5
if Msr == 0 and N != 0:
    print('Моющее средство закончилось. Осталось '+ str(N) +' тарелок')
elif N == 0 and Msr != 0:
    print('Все тарелки вымыты. Осталось ' + str(Msr) + ' ед. моющего средства')
else:
    print('Все тарелки вымыты, моющее средство закончилось')