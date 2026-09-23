from unittest.mock import Mock
from TicketPlus import TicketService

# Importamos los dobles desde nuestro archivo centralizado
from Dobles import InventarioStub, RepositorioFake, UsuarioDummy

def test_compra_exitosa():
    # MOCK: Interacción falsa. Verifica si se llamó al método de correo.
    email_mock = Mock()

    # Inyectamos los dobles al servicio principal
    service = TicketService(
        InventarioStub(),  # STUB: Respuesta predefinida (siempre 50).
        RepositorioFake(), # FAKE: Falso (simula guardar usando una lista).
        email_mock         # MOCK: Pasa como dependencia para luego verificar.
    )

    # Ejecutamos la compra
    resultado = service.comprar(
        UsuarioDummy(),    # DUMMY: Objeto (solo rellena el parámetro requerido).
        2
    )

    # Verificamos que la compra devolvió True
    assert resultado is True

    # Verificamos mediante el Mock que la confirmación se envió exactamente 1 vez
    email_mock.enviar_confirmacion.assert_called_once()