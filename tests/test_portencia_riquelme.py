from funciones.potencia_riquelme import potencia

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1
    assert potencia(-2, 3) == -8
    assert potencia(0, 5) == 0