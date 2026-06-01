@startuml
left to right direction
skinparam packageStyle rectangle

package "Épica: Progreso y Lectura" {
    object "US-P01: Agregar Sesión" as USP1
    USP1 : **Como:** Lector
    USP1 : **Quiero:** Registrar el inicio de una sesión de lectura
    USP1 : **Para:** Medir el tiempo que dedico a un libro

    object "US-P02: Actualizar Progreso" as USP2
    USP2 : **Como:** Lector
    USP2 : **Quiero:** Registrar el avance de páginas de un libro
    USP2 : **Para:** Saber en qué parte me quedé y computar métricas

    object "US-P03: Gestionar Notas" as USP3
    USP3 : **Como:** Lector
    USP3 : **Quiero:** Crear, editar y borrar notas dentro de un libro
    USP3 : **Para:** Guardar mis pensamientos o citas favoritas

    USP2 .down.> USP1 : <<incluye>>
}

@enduml