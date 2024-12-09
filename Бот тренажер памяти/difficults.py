import random
def easy():
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	random.shuffle(numbers)
	listeasy = []
	index = 0
	while len(listeasy) != 4:
		listeasy.append(str(numbers[index]))
		index += 1
	result = ' '.join(listeasy)
	return result


def medium():
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	random.shuffle(numbers)
	listeasy = []
	index = 0
	while len(listeasy) != 5:
		listeasy.append(str(numbers[index]))
		index += 1
	result = ' '.join(listeasy)
	return result


def hard():
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	random.shuffle(numbers)
	listeasy = []
	index = 0
	while len(listeasy) != 6:
		listeasy.append(str(numbers[index]))
		index += 1
	result = ' '.join(listeasy)
	return result


def extreme():
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	random.shuffle(numbers)
	listeasy = []
	index = 0
	while len(listeasy) != 7:
		listeasy.append(str(numbers[index]))
		index += 1
	result = ' '.join(listeasy)
	return result
