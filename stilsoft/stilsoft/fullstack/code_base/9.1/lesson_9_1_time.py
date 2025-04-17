import timeit


def speed_test_1():
	numbers = list(range(1, 10000))
	odd, even = [], []

	for num in numbers:
		if num % 2 == 0:
			even.append(num)

	for num in numbers:
		if num % 2 != 0:
			odd.append(num)


def speed_test_2():
	numbers = list(range(1, 10000))
	odd, even = [], []

	for num in numbers:
		if num % 2 == 0:
			even.append(num)
		else:
			odd.append(num)


result_1 = sum(timeit.repeat("speed_test_1()", number=10000, globals=globals()))
result_2 = sum(timeit.repeat("speed_test_2()", number=10000, globals=globals()))

diff = round(max([result_1, result_2]) / min([result_1, result_2]), 2)

print(f" {result_1} {result_2} разница в {diff} раз")