@startuml
left to right direction
skinparam packageStyle rectangle

package "Épica: Usuario y Seguridad" {
    object "US-A01: Crear Cuenta" as USA1
    USA1 : **Como:** Lector
    USA1 : **Quiero:** Registrarme en la plataforma
    USA1 : **Para:** Tener mi propio espacio de lectura

    object "US-A02: Iniciar Sesión" as USA2
    USA2 : **Como:** Usuario registrado
    USA2 : **Quiero:** Autenticarme con mis credenciales
    USA2 : **Para:** Acceder de forma segura a mi biblioteca

    object "US-A03: Configuración 2FA" as USA3
    USA3 : **Como:** Usuario
    USA3 : **Quiero:** Activar la autenticación de dos pasos
    USA3 : **Para:** Añadir una capa extra de seguridad a mi cuenta

    object "US-A04: Gestionar Perfil" as USA4
    USA4 : **Como:** Usuario
    USA4 : **Quiero:** Actualizar mis datos personales y de contacto
    USA4 : **Para:** Mantener mi información al día

    USA3 .down.> USA2 : <<extiende>>
}

@enduml