# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>

class BaseWallet:
    _ration = 1

    def __init__(self, name, wallet):
        self._name = name
        self._wallet = wallet

    def __add__(self, other):
        if isinstance(other, BaseWallet):
            return BaseWallet(self.name, self.amount + other.amount)

        elif isinstance(other, RubbleWallet):
            return RubbleWallet(self.name, (self.amount + other.amount) / self._ration)

        elif isinstance(other, EuroWallet):
            in_dollar_wallet = RubbleWallet(self.name, other.amount * other.exchange_rate / self._ration)
            return RubbleWallet(self.name, self.amount + in_dollar_wallet.amount)

        elif isinstance(other, DollarWallet):
            in_dollar_wallet = RubbleWallet(self.name, other.amount * other.exchange_rate / self._ration)
            return RubbleWallet(self.name, self.amount + in_dollar_wallet.amount)

        else:
            return RubbleWallet(self.name, self.amount + float(other))

    def __sub__(self, other):
        if isinstance(other, BaseWallet):
            return BaseWallet(self.name, self.amount - other.amount)

        elif isinstance(other, RubbleWallet):
            return RubbleWallet(self.name, (self.amount - other.amount) / self._ration)

        elif isinstance(other, EuroWallet):
            in_dollar_wallet = RubbleWallet(self.name, other.amount * other.exchange_rate / self._ration)
            return RubbleWallet(self.name, self.amount - in_dollar_wallet.amount)

        elif isinstance(other, DollarWallet):
            in_dollar_wallet = RubbleWallet(self.name, other.amount * other.exchange_rate / self._ration)
            return RubbleWallet(self.name, self.amount - in_dollar_wallet.amount)

        else:
            return RubbleWallet(self.name, self.amount - float(other))

    def __mul__(self, other):
        if isinstance(other, BaseWallet):
            return BaseWallet(self.name, self.amount * other.amount)

        else:
            return RubbleWallet(self.name, self.amount * float(other))

    def __truediv__(self, other):
        if isinstance(other, BaseWallet):
            return BaseWallet(self.name, self.amount / other.amount)
        else:
            return RubbleWallet(self.name, self.amount / float(other))

    def __iadd__(self, other):
        if isinstance(other, BaseWallet):
            self.amount = self.amount + other.amount

        elif isinstance(other, RubbleWallet):
            self.amount = self.amount + other.amount

        elif isinstance(other, EuroWallet):
            in_dollar_wallet = RubbleWallet(self.name, other.amount * other.exchange_rate / self._ration)
            self.amount = self.amount + in_dollar_wallet.amount

        elif isinstance(other, DollarWallet):
            in_dollar_wallet = RubbleWallet(self.name, other.amount * other.exchange_rate / self._ration)
            self.amount = self.amount + in_dollar_wallet.amount

        else:
            self.amount = self.amount + float(other)

        return self

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        if isinstance(other, BaseWallet):
            return BaseWallet(self.name, other.amount / self.amount)
        else:
            return RubbleWallet(self.name, float(other) / self.amount)

    def __rsub__(self, other):
        if isinstance(other, BaseWallet):
            return BaseWallet(self.name, other.amount - self.amount)

        elif isinstance(other, RubbleWallet):
            return RubbleWallet(self.name, (other.amount - self.amount) / self._ration)

        elif isinstance(other, EuroWallet):
            in_dollar_wallet = RubbleWallet(self.name, other.amount * other.exchange_rate / self._ration)
            return RubbleWallet(self.name, in_dollar_wallet.amount - self.amount)

        elif isinstance(other, DollarWallet):
            in_dollar_wallet = RubbleWallet(self.name, other.amount * other.exchange_rate / self._ration)
            return RubbleWallet(self.name, in_dollar_wallet.amount - self.amount)

        else:
            return RubbleWallet(self.name, float(other) - self.amount)

    def __eq__(self, other):
        return type(self) == type(other) and self.amount == other.amount

    def __radd__(self, other):
        return self + other

    def __call__(self):
        return self.name, self.amount

    def to_base(self):
        return self.amount * self.exchange_rate

    def spend_all(self):
        if self.amount > 0:
            self.amount = 0

    @property
    def exchange_rate(self):
        return self._ration

    @property
    def name(self):
        return self._name

    @property
    def amount(self):
        return self._wallet

    @amount.setter
    def amount(self, new_amount):
        self._wallet = new_amount


class RubbleWallet(BaseWallet):
    _rubble_ratio = 1 / BaseWallet._ration

    def __init__(self, name, wallet):
        super(RubbleWallet, self).__init__(name, wallet)

    def __add__(self, other):
        if isinstance(other, RubbleWallet):
            return RubbleWallet(self.name, self.amount + other.amount)

        elif isinstance(other, EuroWallet):
            in_dollar_wallet = RubbleWallet(self.name, other.amount * other.exchange_rate / self._rubble_ratio)
            return RubbleWallet(self.name, self.amount + in_dollar_wallet.amount)

        elif isinstance(other, DollarWallet):
            in_dollar_wallet = RubbleWallet(self.name, other.amount * other.exchange_rate / self._rubble_ratio)
            return RubbleWallet(self.name, self.amount + in_dollar_wallet.amount)

        else:
            return RubbleWallet(self.name, self.amount + float(other))

    def __sub__(self, other):
        if isinstance(other, RubbleWallet):
            return RubbleWallet(self.name, self.amount - other.amount)

        elif isinstance(other, EuroWallet):
            in_dollar_wallet = RubbleWallet(self.name, other.amount * other.exchange_rate / self._rubble_ratio)
            return RubbleWallet(self.name, self.amount - in_dollar_wallet.amount)

        elif isinstance(other, DollarWallet):
            in_dollar_wallet = RubbleWallet(self.name, other.amount * other.exchange_rate / self._rubble_ratio)
            return RubbleWallet(self.name, self.amount - in_dollar_wallet.amount)

        else:
            return RubbleWallet(self.name, self.amount - float(other))

    def __mul__(self, other):
        if isinstance(other, RubbleWallet):
            return RubbleWallet(self.name, self.amount * other.amount)

        else:
            return RubbleWallet(self.name, self.amount * float(other))

    def __truediv__(self, other):
        if isinstance(other, RubbleWallet):
            return RubbleWallet(self.name, self.amount / other.amount)

        else:
            return RubbleWallet(self.name, self.amount / float(other))

    def __str__(self):
        return f'Rubble Wallet {self.name} {self.amount}'

    @property
    def exchange_rate(self):
        return self._rubble_ratio


class DollarWallet(BaseWallet):
    _dollar_ratio = 60 / BaseWallet._ration

    def __init__(self, name, wallet):
        super(DollarWallet, self).__init__(name, wallet)

    def __add__(self, other):
        if isinstance(other, DollarWallet):
            return DollarWallet(self.name, self.amount + other.amount)

        elif isinstance(other, EuroWallet):
            in_dollar_wallet = DollarWallet(self.name, other.amount * other.exchange_rate / self._dollar_ratio)
            return DollarWallet(self.name, self.amount + in_dollar_wallet.amount)

        elif isinstance(other, RubbleWallet):
            in_dollar_wallet = DollarWallet(self.name, other.amount * other.exchange_rate / self._dollar_ratio)
            return DollarWallet(self.name, self.amount + in_dollar_wallet.amount)

        else:
            return DollarWallet(self.name, self.amount + float(other))

    def __sub__(self, other):
        if isinstance(other, DollarWallet):
            return DollarWallet(self.name, self.amount - other.amount)

        elif isinstance(other, EuroWallet):
            in_dollar_wallet = DollarWallet(self.name, other.amount * other.exchange_rate / self._dollar_ratio)
            return DollarWallet(self.name, self.amount - in_dollar_wallet.amount)

        elif isinstance(other, RubbleWallet):
            in_dollar_wallet = DollarWallet(self.name, other.amount * other.exchange_rate / self._dollar_ratio)
            return DollarWallet(self.name, self.amount - in_dollar_wallet.amount)

        else:
            return DollarWallet(self.name, self.amount - float(other))

    def __mul__(self, other):
        if isinstance(other, DollarWallet):
            return DollarWallet(self.name, self.amount * other.amount)
        else:
            return DollarWallet(self.name, self.amount * float(other))

    def __truediv__(self, other):
        if isinstance(other, DollarWallet):
            return DollarWallet(self.name, self.amount / other.amount)
        else:
            return DollarWallet(self.name, self.amount / float(other))

    def __str__(self):
        return f'Dollar Wallet {self.name} {self.amount}'

    @property
    def exchange_rate(self):
        return self._dollar_ratio


class EuroWallet(BaseWallet):
    _euro_ratio = 70 / BaseWallet._ration

    def __init__(self, name, wallet):
        super(EuroWallet, self).__init__(name, wallet)

    def __add__(self, other):
        if isinstance(other, EuroWallet):
            return EuroWallet(self.name, self.amount + other.amount)

        elif isinstance(other, DollarWallet):
            in_euro_wallet = EuroWallet(self.name, other.amount * other.exchange_rate / self.exchange_rate)
            return EuroWallet(self.name, self.amount + in_euro_wallet.amount)

        elif isinstance(other, RubbleWallet):
            in_euro_wallet = EuroWallet(self.name, other.amount * other.exchange_rate / self.exchange_rate)
            return EuroWallet(self.name, self.amount + in_euro_wallet.amount)

        else:
            return EuroWallet(self.name, self.amount + float(other))

    def __sub__(self, other):
        if isinstance(other, EuroWallet):
            return EuroWallet(self.name, self.amount - other.amount)

        elif isinstance(other, DollarWallet):
            in_euro_wallet = EuroWallet(self.name, other.amount * other.exchange_rate / self.exchange_rate)
            return EuroWallet(self.name, self.amount - in_euro_wallet.amount)

        elif isinstance(other, RubbleWallet):
            in_euro_wallet = EuroWallet(self.name, other.amount * other.exchange_rate / self.exchange_rate)
            return EuroWallet(self.name, self.amount - in_euro_wallet.amount)

        else:
            return EuroWallet(self.name, self.amount - float(other))

    def __mul__(self, other):
        if isinstance(other, EuroWallet):
            return EuroWallet(self.name, self.amount * other.amount)
        else:
            return EuroWallet(self.name, self.amount * float(other))

    def __truediv__(self, other):
        if isinstance(other, EuroWallet):
            return EuroWallet(self.name, self.amount / other.amount)
        else:
            return EuroWallet(self.name, self.amount / float(other))

    def __str__(self):
        return f'Euro Wallet {self.name} {self.amount}'

    @property
    def exchange_rate(self):
        return self._euro_ratio


if __name__ == '__main__':
    print(EuroWallet('EUR', 200).to_base())
