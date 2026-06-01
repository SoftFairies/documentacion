@startuml
left to right direction
skinparam packageStyle rectangle

package "Épica: Dashboard Administrativo" {
    object "US-M01: Rendimiento de App" as USM1
    USM1 : **Como:** Super Administrador
    USM1 : **Quiero:** Ver el estado del servidor, latencias y consumo
    USM1 : **Para:** Asegurar la disponibilidad técnica de la plataforma

    object "US-M02: Estadísticas de Uso" as USM2
    USM2 : **Como:** Super Administrador
    USM2 : **Quiero:** Monitorear métricas de uso global (usuarios activos, lecturas)
    USM2 : **Para:** Analizar el rendimiento del negocio y adopción de la app
}

@enduml