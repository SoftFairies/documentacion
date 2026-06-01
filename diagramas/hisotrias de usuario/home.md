@startuml
left to right direction
skinparam packageStyle rectangle

package "Épica: Home y Estadísticas" {
    object "US-H01: Ver Dashboard Home" as USH1
    USH1 : **Como:** Lector
    USH1 : **Quiero:** Acceder al inicio de la aplicación
    USH1 : **Para:** Tener un vistazo rápido de mi actividad reciente

    object "US-H02: Consultar Métricas" as USH2
    USH2 : **Como:** Lector
    USH2 : **Quiero:** Visualizar gráficos de mis estadísticas de lectura
    USH2 : **Para:** Evaluar mis hábitos y metas mensuales

    object "US-H03: Radar de Curiosidades" as USH3
    USH3 : **Como:** Lector
    USH3 : **Quiero:** Interactuar con el radar de datos curiosos
    USH3 : **Para:** Conocer estadísticas aleatorias e interesantes de la app
}

@enduml