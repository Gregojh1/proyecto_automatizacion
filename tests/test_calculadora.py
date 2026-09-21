from calculadora import Calculadora
import pytest
#PUNTO 1 -----------------------
calculadora1 = Calculadora()


def test_sumarenteros_positivo(numeros_enteros):

    a, b = numeros_enteros
    resultado = calculadora1.sumar(a, b)

    assert resultado == 12


def test_sumarenteros_fallo(numeros_enteros):
    with pytest.raises(TypeError):
        calculadora1.sumar("hola", 7)


def test_mult_pass(numeros_flotantes):
    a, b = numeros_flotantes
    resultado = calculadora1.multiplicar(a, b)
    assert resultado == pytest.approx(0.02)


def test_mult_fail(numeros_flotantes):
    with pytest.raises(TypeError):
        calculadora1.multiplicar("j", 5.0)


def test_rest_pass(numeros_enteros):
    a, b = numeros_enteros
    resultado = calculadora1.restar(a, b)
    assert resultado == 4


def test_rest_fail(numeros_enteros):
    a, b = numeros_enteros
    with pytest.raises(TypeError):
        calculadora1.restar("y", 8)


def test_div_pass(numeros_enteros):
    a, b = numeros_enteros
    resultado = calculadora1.dividir(a, b)
    assert resultado == 2


@pytest.mark.exception
def test_div_fail(numeros_enteros):
    a, b = numeros_enteros
    with pytest.raises(ValueError):
        calculadora1.dividir(2, 0)


# PUNTO 2 -----------------------


@pytest.mark.smoke
@pytest.mark.parametrize(
    "a,b , esperado", [(2, 5, 7), (9, 1, 10), (8, 7, 15)]
)  # estructura es a b y el tercer numero es el esperado el resultado
def test_sumar_param(a, b, esperado):
    resultado = calculadora1.sumar(a, b)

    assert resultado == esperado


@pytest.mark.parametrize("a,b, esperado", [(10, 4, 6), (8, 2, 6), (19, 13, 6)])
def test_rest_param(a, b, esperado):
    resultado = calculadora1.restar(a, b)
    assert resultado == esperado


@pytest.mark.parametrize("a,b, esperado", [(2, 8, 16), (5, 3, 15), (12, 1, 12)])
def test_mult_param(a, b, esperado):
    resultado = calculadora1.multiplicar(a, b)
    assert resultado == esperado


@pytest.mark.exception
@pytest.mark.parametrize("a,b, esperado", [(4, 2, 2), (16, 4, 4), (8, 2, 4)])
def test_div_param(a, b, esperado):
    resultado = calculadora1.dividir(a, b)
    assert resultado == esperado

@pytest.mark.exception
@pytest.mark.parametrize("a,b, esperado", [(4, 0, 1), (16, 0, 1), (8, 0, 1)])
def test_div_param_fail(a,b, esperado):
    with pytest.raises(ValueError):
        calculadora1.dividir(a, b)