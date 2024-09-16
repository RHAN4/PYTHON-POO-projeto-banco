class Conta:
    def __init__(self, numeroDaConta: int, agencia: int) -> None:
        self.numeroDaConta = numeroDaConta
        self.agencia = agencia
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor