class Wallet:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Добавлено {amount}. Текущий баланс: {self.balance}")
        else:
            print("Сумма должна быть положительной")

    def spend_money(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Потрачено {amount}. Текущий баланс: {self.balance}")
            else:
                print("Недостаточно средств")
        else:
            print("Сумма должна быть положительной")

    def check_balance(self):
        return self.balance


class CryptoWallet(Wallet):
    COIN_TO_USD = {
        'BTC': 72000,  # Пример курса биткоина к доллару
        'ETH': 3500    # Пример курса эфириума к доллару
    }

    def __init__(self, initial_balance=0):
        super().__init__(initial_balance)
        self.coins = {}

    def add_coin(self, coin, amount):
        if amount > 0:
            if coin in self.COINS:
                if coin in self.coins:
                    self.coins[coin] += amount
                else:
                    self.coins[coin] = amount
                print(f"Добавлено {amount} {coin}. Текущий баланс: {self.coins[coin]} {coin}")
            else:
                print(f"Криптовалюта {coin} не поддерживается")
        else:
            print("Количество должно быть положительным")

    def spend_coin(self, coin, amount):
        if amount > 0:
            if coin in self.coins and self.coins[coin] >= amount:
                self.coins[coin] -= amount
                print(f"Потрачено {amount} {coin}. Текущий баланс: {self.coins[coin]} {coin}")
            else:
                print(f"Недостаточно средств для {coin}")
        else:
            print("Количество должно быть положительным")

    def check_coin_balance(self, coin):
        return self.coins.get(coin, 0)

    def convert_to_usd(self, coin, amount):
        if coin in self.COINS:
            return amount * self.COINS[coin]
        else:
            print(f"Криптовалюта {coin} не поддерживается")
            return 0

    def total_balance_in_usd(self):
        total_balance = super().check_balance()
        for coin, amount in self.coins.items():
            total_balance += self.convert_to_usd(coin, amount)
        return total_balance


# Пример использования
wallet = Wallet(100)
wallet.add_money(50)
wallet.spend_money(30)
print(f"Баланс кошелька: {wallet.check_balance()}")

crypto_wallet = CryptoWallet(200)
crypto_wallet.add_coin('BTC', 0.01)
crypto_wallet.add_coin('ETH', 2)
crypto_wallet.spend_coin('ETH', 1)
print(f"Баланс биткоинов: {crypto_wallet.check_coin_balance('BTC')}")
print(f"Общий баланс в USD: {crypto_wallet.total_balance_in_usd()}")
