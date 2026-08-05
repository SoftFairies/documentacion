import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

print("--- Datos de acceso para la prueba ---")
usuario_real = input("Correo de Admin: ")
password_real = getpass.getpass("Contraseña (no se verá al escribir): ")

print("Iniciando el navegador...")
driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

try:
    # -------------------------------------------------------------
    # Ingresar al Login de la Administración
    # -------------------------------------------------------------
    url_login = "http://localhost:3001/login"
    print(f"📍 Navegando a: {url_login}")
    driver.get(url_login)

    assert (
        "login" in driver.current_url.lower()
    ), "No se pudo cargar la página de login."

    # -------------------------------------------------------------
    # Autenticación (Usando los datos de la terminal)
    # -------------------------------------------------------------
    print("Ingresando credenciales de administrador...")

    wait_largo = WebDriverWait(driver, 20)

    selector_email = "input[name='email'], input[name='correo'], input[type='email'], input[id='email'], input[id='correo']"
    email_input = wait_largo.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, selector_email))
    )
    email_input.clear()
    email_input.send_keys(usuario_real)

    selector_pass = "input[name='password'], input[name='contrasena'], input[type='password'], input[id='password'], input[id='contrasena']"
    password_input = driver.find_element(By.CSS_SELECTOR, selector_pass)
    password_input.clear()
    password_input.send_keys(password_real)

    print("Enviando formulario...")
    password_input.send_keys(Keys.RETURN)

    # -------------------------------------------------------------
    # Validación del Dashboard (Resumen)
    # -------------------------------------------------------------
    print("Verificando redirección al Dashboard...")
    wait.until(EC.url_contains("/dashboard"))

    assert (
        "/dashboard" in driver.current_url
    ), "El inicio de sesión falló o no redirigió al dashboard."
    print("¡Inicio de sesión exitoso!")

    time.sleep(5)

    # -------------------------------------------------------------
    # Navegación entre las diferentes vistas del módulo
    # -------------------------------------------------------------
    url_usuarios = "http://localhost:3001/dashboard/usuarios"
    print(f"Navegando a la gestión de usuarios: {url_usuarios}")
    driver.get(url_usuarios)
    
    wait.until(EC.url_contains("/usuarios"))
    print("Vista de Usuarios cargada correctamente.")
    time.sleep(3)

    url_actividad = "http://localhost:3001/dashboard/actividad"
    print(f"Navegando al registro de actividad: {url_actividad}")
    driver.get(url_actividad)
    
    wait.until(EC.url_contains("/actividad"))
    print("Vista de Actividad cargada correctamente.")
    time.sleep(3)

    url_resumen = "http://localhost:3001/dashboard/resumen"
    print(f"Navegando a la gestión de usuarios: {url_resumen}")
    driver.get(url_resumen)
        
    wait.until(EC.url_contains("/resumen"))
    print("Vista de Resumen cargada correctamente.")
    time.sleep(3)

    assert "Error" not in driver.title, "Ocurrió un error al cargar alguna de las vistas."
    print("¡Todas las pruebas y navegaciones en Lectura Métrica concluyeron con éxito!")

except Exception as e:
    print(f"Ocurrió un error en la ejecución del test: {e}")
    driver.save_screenshot("error_lecturametrica.png")
    print(
        "📸 Se ha guardado una captura de pantalla del error como 'error_lecturametrica.png'"
    )

finally:
    print("ByeBye! Cerrando el navegador...")
    time.sleep(1)
    driver.quit()