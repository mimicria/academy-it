# Необходимо написать функцию генератор nfib, которая имеет один аргумент, максимальное
# количество чисел Фибоначчи, которое она может выдать.
def nfib(n: int):
    if n in (1, 2):
        return 1
    return nfib(n - 1) + nfib(n - 2)

nnums = 20

# • Создание списка из 20 чисел Фибоначчи с помощью генератора списка
# 1'st w/o function
fib_list = [1, 1]
[fib_list.append(fib_list[-2] + fib_list[-1]) for i in range(nnums-2)]
print(fib_list)

# 2'nd with function
fib_list2 = []
[fib_list2.append(nfib(i)) for i in range(1, nnums+1)]
print(fib_list2)

# • Создание списка из 20 чисел Фибоначчи с помощью цикла for
fib_cycle = []
for iter in range(1, nnums+1):
    fib_cycle.append(nfib(iter))
print(fib_cycle)

# • Создание множества из 20 чисел Фибоначчи с помощью генератора множества
fib_set = set()
{fib_set.add(nfib(i)) for i in range(1,nnums+1)}
# where's no double 1 in set
# where's no sorted set
print(fib_set)
