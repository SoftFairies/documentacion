@startuml
left to right direction
skinparam packageStyle rectangle

package "Épica: Gestión de Biblioteca (CRUD)" {
    object "US-B01: Registrar Libro" as USB1
    USB1 : **Como:** Lector
    USB1 : **Quiero:** Agregar un nuevo libro a mi catálogo
    USB1 : **Para:** Empezar a trackear su lectura

    object "US-B02: Visualizar Biblioteca" as USB2
    USB2 : **Como:** Lector
    USB2 : **Quiero:** Ver la lista completa de mis libros guardados
    USB2 : **Para:** Seleccionar qué quiero leer hoy

    object "US-B03: Modificar Libro" as USB3
    USB3 : **Como:** Lector
    USB3 : **Quiero:** Editar los metadatos o sobreescribir un libro
    USB3 : **Para:** Corregir información errónea

    object "US-B04: Eliminar Libro" as USB4
    USB4 : **Para:** Limpiar mi catálogo de títulos que ya no quiero

    object "US-B05: Filtrar Libros" as USB5
    USB5 : **Como:** Lector
    USB5 : **Quiero:** Buscar libros por estado (Pendiente, )
    USB5 : **Para:** Encontrar lecturas específicas rápidamente

    USB5 .down.> USB2 : <<incluye>>
}

@enduml