@startuml
left to right direction
skinparam packageStyle rectangle

package "Épica: Buzón de Lectura (Social)" {
    object "US-S01: Ver Recomendaciones" as USS1
    USS1 : **Como:** Lector
    USS1 : **Quiero:** Explorar libros recomendados basados en la comunidad
    USS1 : **Para:** Descubrir nuevas obras de mi interés

    object "US-S02: Reaccionar a Recomendación" as USS2
    USS2 : **Como:** Lector
    USS2 : **Quiero:** Dar Like o Dislike a las sugerencias del buzón
    USS2 : **Para:** Ayudar al sistema a afinar lo que me muestra

    object "US-S03: Escribir Recomendación" as USS3
    USS3 : **Como:** Lector
    USS3 : **Quiero:** Redactar una reseña o recomendación de un libro
    USS3 : **Para:** Compartir mi opinión con otros usuarios

    USS2 .down.> USS1 : <<extiende>>
}

@enduml