class Wallet:
    payment_system: str = 'Visa/MasterCard'

    def __init__(self, name: str, currency: str):
        if currency not in ["USD", "EUR", "RUB"]:
            raise ValueError("Неподдерживаемая валюта.")

        self.name = name
        self.currency = currency
        self._balance = 0.0

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self._balance += amount

    def pay(self, amount: float):
        if amount > self._balance:
            raise ValueError("Недостаточно средств на балансе.")
        self._balance -= amount

    def get_balance(self) -> float:
        return self._balance

    def delete_account(self):
        self._balance = 0.0


# Пример использования
wallet = Wallet("MyWallet", "USD")
wallet.deposit(100.0)
print(wallet.get_balance())  # 100.0
wallet.pay(50.0)
print(wallet.get_balance())  # 50.0
wallet.delete_account()
print(wallet.get_balance())  # 0.0