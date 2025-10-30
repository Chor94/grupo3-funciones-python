from funciones.aguiar import multiplicar_aguiar

def test_multiplicar_aguiar():
    assert multiplicar_aguiar(3, 4) == 12
    assert multiplicar_aguiar(-2, 5) == -10
    assert multiplicar_aguiar(0, 5) == 0
