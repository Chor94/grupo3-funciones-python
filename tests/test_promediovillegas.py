#tests/test_promedio.py
from funciones.promediovillegas import promedio
def test_promedio():
 assert promedio([2, 4, 6]) == 4
 assert promedio([]) is None
