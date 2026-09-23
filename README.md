# Test-Double-TicketPlus

**Autor:** Hever Andre Alfonso Jimenez

Este proyecto es un ejercicio práctico sobre pruebas unitarias y el uso de dobles de prueba (Test Doubles) en Python para aislar dependencias en el código.

## Archivos del proyecto

* **TicketPlus.py**: Contiene la lógica principal del servicio `TicketService`.
* **Dobles.py**: Almacena las clases que simulan los servicios externos requeridos por el sistema.
* **test_ticket_service.py**: Archivo con la prueba unitaria aislada utilizando un Stub.
* **test_ticket_serviceI.py**: Archivo con la prueba de integración utilizando un Spy para validar todo el flujo.

## Conceptos aplicados

* **Stub (`InventarioStub`)**: Respuesta predefinida. Objeto falso configurado para devolver respuestas fijas (simula disponibilidad en el inventario).
* **Dummy (`UsuarioDummy`, `EmailDummy`)**: Objeto. Sirve como relleno inerte para ocupar espacios obligatorios en los parámetros de una función, evitando errores de ejecución pero sin aportar lógica.
* **Fake (`RepositorioFake`)**: Falso. Objeto funcional con lógica simplificada. Simula una base de datos almacenando registros temporalmente en una lista en memoria.
* **Mock (`Mock` de Python)**: Interacción falsa. Se utiliza para afirmar o verificar acciones, comprobando si un método externo fue llamado correctamente.
* **Spy (`InventarioSpy`)**: Contar. Objeto que lleva un registro interno (contador) para recordar y verificar cuántas veces fue ejecutado un método durante la prueba.

## Ejecución

El proyecto utiliza `pytest` para la ejecución de las pruebas. Para correr los tests, ejecuta los siguientes comandos en la terminal:

`pytest test_ticket_service.py`
`pytest test_ticket_serviceI.py`