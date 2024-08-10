from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_homepage():
    # Inicia el navegador
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # Abre la página
    driver.get("http://localhost/index.html")  # Reemplaza con la URL donde está alojada la página web
    
    # Verifica que el título de la página es correcto
    assert "ANTRA" in driver.title

    # Verifica que el logo se carga correctamente
    logo = driver.find_element(By.XPATH, "//img[@alt='Logo ANTRA']")
    assert logo.is_displayed()

    # Verifica que los elementos de la navegación son visibles
    navbar_items = driver.find_elements(By.CLASS_NAME, "nav-link")
    assert len(navbar_items) == 5  # Reemplaza con el número correcto de ítems en la navegación

    # Verifica que el video de fondo se está reproduciendo
    video = driver.find_element(By.TAG_NAME, "video")
    assert video.is_displayed()

    # Cierra el navegador
    driver.quit()
