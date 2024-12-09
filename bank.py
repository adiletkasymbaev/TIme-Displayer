class BankAccount:
	owner = None
	__balance = 0
	__currency = "$"
	__operations_history = []
	has_credit = False

	def __init__(self, owner, balance, currency, operations_history, has_credit):
		self.owner = owner
		self.__balance = balance
		self.__currency = currency
		self.__operations_history = operations_history
		self.has_credit = has_credit

	def __add_to_history(self, type, sum):
		self.__operations_history.append(
			{
				'type': type,
				'sum': sum
			}
		)

	def add_to_balance(self, new_sum):
		if type(new_sum) is int:
			if 0 < new_sum < 25000:
				self.__balance += new_sum
				self.__add_to_history("Пополнение", new_sum)

	def withdraw_from_balance(self, new_sum):
		if type(new_sum) is int:
			if 0 < new_sum < 25000:
				self.__balance -= new_sum
				self.__add_to_history("Снятие", new_sum)

	def display_balance(self):
		print(f"Баланс: {self.__balance} {self.__currency}")

	def display_history(self):
		for op in self.__operations_history:
			print(f"Тип: {op['type']}, Сумма: {op['sum']}")


ba_adilet = BankAccount("Bayastan Kadyraliev", 15000, "$", [], False)

ba_adilet.display_balance()
ba_adilet.add_to_balance(5000)
ba_adilet.withdraw_from_balance(10000)
ba_adilet.display_history()
ba_adilet.display_balance()
