import pytest
from banco.models.conta import Conta

@pytest.fixture
def contaValida():
    return Conta(333, 444)


def test_validando_atributo_numeroDaConta(contaValida):
    assert contaValida.numeroDaConta == 333

def test_validando_atributo_agencia(contaValida):
    assert contaValida.agencia == 444

def test_validando_atributo_saldo(contaValida):
    assert contaValida._saldo == 0

def test_depositar_valor_positivo(contaValida):
    contaValida.depositar(100)
    assert contaValida._saldo == 100

def test_sacar_valor_positivo_com_saldo_positivo(contaValida):
    contaValida.depositar(100)
    contaValida.sacar(100)
    assert contaValida._saldo == 0