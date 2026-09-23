class TicketService:
    def __init__(self, inventario, repositorio, email_service):
        self.inventario = inventario
        self.repositorio = repositorio
        self.email_service = email_service

    def comprar(self, usuario, cantidad):
        disponibles = self.inventario.consultar_disponibilidad()
        
        if disponibles < cantidad:
            return False
            
        self.repositorio.guardar(usuario, cantidad)
        self.email_service.enviar_confirmacion(usuario)
        
        return True

# ==========================================
# ZONA DE EJECUCIÓN ANTIGUA (COMENTADA)
# ==========================================
# from Dobles import InventarioStub, UsuarioDummy, RepositorioFake, EmailDummy, InventarioSpy
# from unittest.mock import Mock
#
# inventario_spy = InventarioSpy()
# 
# service = TicketService(
#     inventario_spy,
#     RepositorioFake(),
#     EmailDummy()
# )
# 
# resultado = service.comprar(UsuarioDummy(), 2)
# print("Resultado compra 1:", resultado)
# print("Consultas al inventario:", inventario_spy.veces_consultado)