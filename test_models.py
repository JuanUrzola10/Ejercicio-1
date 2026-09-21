from models import Registro

def test_registro_valido():
    r=Registro(nombre="Ana Pérez",identificacion="12345",
               correo="ana@example.com",programa="Ingeniería de Sistemas",
               semestre=5,telefono="3001234567")
    assert r.semestre==5
