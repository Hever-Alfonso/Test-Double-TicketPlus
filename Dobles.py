# STUB: Respuesta predefinida.
class InventarioStub:
    def consultar_disponibilidad(self):
        return 50

# DUMMY: Objeto (Relleno).
class UsuarioDummy:
    pass

# FAKE: Falso (simula la base de datos).
class RepositorioFake:
    def __init__(self):
        self.compras = []

    def guardar(self, usuario, cantidad):
        self.compras.append({
            "usuario": usuario,
            "cantidad": cantidad
        })

# DUMMY (Email): Objeto de relleno.
class EmailDummy:
    def enviar_confirmacion(self, usuario):
        pass

# SPY: Contar. 
class InventarioSpy:
    def __init__(self):
        self.veces_consultado = 0

    def consultar_disponibilidad(self):
        self.veces_consultado += 1
        return 50

# ==========================================
# PRUEBAS AISLADAS (COMENTADAS)
# ==========================================
# -- Prueba del Dummy --
# usuario = UsuarioDummy()
# print(usuario)
#
# -- Prueba del Fake --
# repo = RepositorioFake()
# repo.guardar('Ana', 2)
# print(repo.compras)
#
# -- Prueba del Spy --
# inventario = InventarioSpy()
# inventario.consultar_disponibilidad()
# print(inventario.veces_consultado)