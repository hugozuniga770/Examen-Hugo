"""Escriba aquí sus pruebas. No borre ni modifique tests/test_base.py.

Cada función de prueba comienza con test_ y usa assert.
Agregue al menos los cuatro casos descritos en el README.
Los imports ya están preparados; deepcopy crea una copia independiente
de la lista y de los diccionarios para comprobar que no se modificaron.
"""
from copy import deepcopy

import reservas
from reservas import modificar_reserva, se_superponen


# Ejemplo de estructura, sin solución del caso:
# def test_nombre_del_comportamiento():
#     datos = [...]
#     antes = deepcopy(datos)
#     resultado = modificar_reserva(datos, ...)
#     assert resultado == "..."
#     assert datos == antes  # Cuando la operación debe conservar TODO.

def test_aprueba_por_conflicto_modificacion_con_otras_reservas():
    datos = [dict(id="R1", sala="A", inicio=540, fin=600, estado="confirmada"),
             dict(id="R2", sala="B", inicio=600, fin=660, estado="confirmada")]
    assert modificar_reserva(datos, "R1", 560, 620) == "CONFLICTO"


def test_aprueba_por_cancelada_modificacion_con_otras_reservas():
    datos = [dict(id="R3", sala="C", inicio=540, fin=600, estado="cancelada"),
             dict(id="R4", sala="D", inicio=600, fin=660, estado="confirmada")]
    assert modificar_reserva(datos, "R3", 540, 600) == "CANCELADA"


def test_aprueba_por_horario_invalido_con_otras_reservas():
    datos = [dict(id="R5", sala="E", inicio=540, fin=600, estado="confirmada"),
             dict(id="R6", sala="F", inicio=600, fin=660, estado="confirmada")]
    assert modificar_reserva(datos, "R5", -60, 60) == "HORARIO_INVALIDO"
