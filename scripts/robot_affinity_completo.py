import pyautogui
import time
import pandas as pd
from groq import Groq
from dotenv import load_dotenv
import os

# --- 1. CONFIGURACIÓN ---
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

pyautogui.FAILSAFE = True

# --- 2. FUNCIONES DE ACCIÓN ---
def escribir(imagen, texto):
    try:
        pos = pyautogui.locateOnScreen(imagen, confidence=0.7)
        if pos:
            pyautogui.click(pyautogui.center(pos))
            time.sleep(0.5)
            pyautogui.click(clicks=3)
            pyautogui.press('backspace')
            pyautogui.write(str(texto), interval=0.1)
            return True
    except:
        return False

def buscar_municipio_con_scroll():
    print("Buscando San Cristóbal de La Laguna...")
    try:
        campo = pyautogui.locateOnScreen('campo_municipio.png', confidence=0.7)
        if campo:
            pyautogui.click(pyautogui.center(campo))
            time.sleep(1)

            zona = pyautogui.locateOnScreen('zona_lista_municipios.png', confidence=0.7)
            if zona:
                pyautogui.click(pyautogui.center(zona))
                time.sleep(0.5)

                for i in range(50):
                    encontrado = pyautogui.locateOnScreen('opcion_laguna.png', confidence=0.8)
                    if encontrado:
                        pyautogui.click(pyautogui.center(encontrado))
                        print("¡Municipio seleccionado!")
                        return True
                    pyautogui.scroll(-300)
                    time.sleep(0.2)
        return False
    except Exception as e:
        print(f"Error en el scroll: {e}")
        return False

# --- 3. CARGA DE DATOS ---
df = pd.read_excel("sample_members.xlsx")
elena = df.iloc[0]

# --- 4. EJECUCIÓN ---
print("Robot listo. Tienes 5 segundos...")
time.sleep(5)

# FASE 1: INICIO Y DATOS PERSONALES
if pyautogui.locateOnScreen('boton_anadir.png', confidence=0.7):
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('boton_anadir.png')))
    time.sleep(2)

    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('selector_empresa.png', confidence=0.7)))
    time.sleep(0.5)
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('opcion_fisica.png', confidence=0.7)))
    time.sleep(1)

    escribir('casilla_nif.png', elena['NIF / CIF'])
    escribir('casilla_nombre.png', elena['Nombre'])
    escribir('casilla_apellido.png', elena['Apellidos'])

    # FASE 2: DOMICILIO FISCAL
    pestana = pyautogui.locateOnScreen('pestana_domicilio.png', confidence=0.7)
    if pestana:
        pyautogui.click(pyautogui.center(pestana))
        time.sleep(1)

        escribir('casilla_calle.png', elena['Dirección Completa'])
        escribir('casilla_cp.png', elena['CP'])

        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('campo_provincia.png', confidence=0.7)))
        time.sleep(0.8)
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('opcion_tenerife.png', confidence=0.7)))
        time.sleep(1)

        buscar_municipio_con_scroll()

    # FASE 3: FINALIZACIÓN
    otros = pyautogui.locateOnScreen('pestana_otros_datos.png', confidence=0.7)
    if otros:
        pyautogui.click(pyautogui.center(otros))
        print(">>> TRABAJO TERMINADO.")
