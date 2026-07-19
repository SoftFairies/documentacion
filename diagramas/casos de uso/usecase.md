@startuml
left to right direction
skinparam packageStyle rectangle

actor "Lector" as Lector
actor "Super Administrador" as SuperAdmin

' El Super Administrador hereda de Lector
SuperAdmin --|> Lector

package "Módulo de Usuario y Seguridad" {
    usecase "Crear Cuenta" as UC_User1
    usecase "Realizar Encuesta de Preferencias" as UC_User_Pref
    usecase "Iniciar Sesión" as UC_User2
    usecase "Configuración de 2 Pasos" as UC_User3
    usecase "Gestionar Perfil" as UC_User4
    usecase "Gestionar Perfil" as UC_User4
    usecase "Ver Insignias" as UC_Gam_Insignias

    ' Relaciones
    UC_User1 ..> UC_User_Pref : <<include>>
    UC_User2 <.. UC_User3 : <<extend>>
    UC_User4 ..> UC_Gam_Insignias : <<include>>
}

package "Módulo de Biblioteca" {
    usecase "Gestionar Biblioteca (CRUD)" as UC_Lib0
    usecase "Registrar Libro" as UC_Lib1
    usecase "Buscar y Autocompletar por API" as UC_Lib_API
    usecase "Filtrar Libros" as UC_Lib2
    usecase "Agregar Sesión de Lectura" as UC_Lib3
    usecase "Actualizar Progreso" as UC_Lib4
    usecase "Sobre-escribir Libro" as UC_Lib5
    usecase "Gestionar Notas de un Libro" as UC_Lib6

    ' Relaciones
    UC_Lib1 ..> UC_Lib2 : <<include>>
    UC_Lib4 ..> UC_Lib3 : <<include>>
    UC_Lib1 <.. UC_Lib_API : <<extend>>
}

package "Buzón de Lectura (Social)" {
    usecase "Recibir Recomendaciones" as UC_Buz1
    usecase "Dar Like / Dislike" as UC_Buz2
    usecase "Escribir Recomendación" as UC_Buz3

    ' Relaciones
    UC_Buz1 <.. UC_Buz2 : <<extend>>
}

package "Home y Estadísticas (Lector)" {
    usecase "Ver Home / Inicio" as UC_Home1
    usecase "Consultar Métricas de Lectura" as UC_Home2
    usecase "Explorar Radar de Curiosidades" as UC_Home3
    usecase "Ver Recomendación Diaria" as UC_Home4
    usecase "Ver Racha de Lectura" as UC_Gam_Racha

    ' Relaciones de Inclusión
    UC_Home1 ..> UC_Home3 : <<include>>
    UC_Home1 ..> UC_Home4 : <<include>>
    UC_Home2 ..> UC_Gam_Racha : <<include>>
}

package "Dashboard Administrativo" {
    usecase "Monitorear Rendimiento de App" as UC_Admin1
    usecase "Consultar Estadísticas de Uso" as UC_Admin2
}

' Asignación de permisos (Lector)
Lector --> UC_User1
Lector --> UC_User2
Lector --> UC_User4
Lector --> UC_Lib0
Lector --> UC_Lib1
Lector --> UC_Lib4
Lector --> UC_Lib5
Lector --> UC_Lib6
Lector --> UC_Buz1
Lector --> UC_Buz3
Lector --> UC_Home1
Lector --> UC_Home2

' Asignación de permisos (Admin)
SuperAdmin --> UC_Admin1
SuperAdmin --> UC_Admin2

@enduml