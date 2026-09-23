from unittest.mock import Mock
from TicketPlus import TicketService

# Importamos los dobles desde nuestro archivo centralizado
from Dobles import InventarioSpy, RepositorioFake, UsuarioDummy

def test_flujo_completo_compra():
    # Creamos las instancias antes para poder consultarlas después de la compra
    inventario = InventarioSpy()    # SPY: Contar (registra las consultas).
    repositorio = RepositorioFake() # FAKE: Falso (guarda temporalmente).
    email = Mock()                  # MOCK: Interacción falsa (verifica llamadas).

    # Inyectamos los dobles al servicio principal
    service = TicketService(
        inventario,
        repositorio,
        email
    )

    # Ejecutamos la compra
    resultado = service.comprar(
        UsuarioDummy(), # DUMMY: Objeto (relleno).
        2
    )

    # Validamos que la compra fue exitosa
    assert resultado is True

    # Validamos que el Spy registró exactamente 1 consulta en su contador interno
    assert inventario.veces_consultado == 1

    # Validamos que el Fake guardó exactamente 1 elemento en su lista de compras
    assert len(repositorio.compras) == 1

    # Validamos que el Mock intentó enviar el correo 1 vez
    email.enviar_confirmacion.assert_called_once()