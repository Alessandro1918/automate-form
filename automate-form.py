import pyautogui as pag
import time

def writeField(fieldvalue):
  pag.press("tab")
  pag.write(fieldvalue, interval=0.1)
  time.sleep(1)

#reads the form answers from a txt file
with open('form-aswers.txt') as f:
  lines = f.readlines()

#find position of the first form field in the screen
coords = pag.locateCenterOnScreen("first-field.png")
print("First field:", coords)

#brings page to front plan, sending python terminal to the back
pag.moveTo(coords[0], coords[1], 1)
pag.click()

#field: "Email"
pag.click()
pag.write(lines[0], interval=0.1)
time.sleep(1)

#field: "Senha"
writeField(lines[1])

#field: "Confirmar senha"
writeField(lines[2])

#field: "Nome"
writeField(lines[3])
  
#field: "Sobrenome"
writeField(lines[4])

#field: "Celular"
writeField(lines[5])

#field: "Empresa"
writeField(lines[6])

#button: "Enviar"
coords = pag.locateCenterOnScreen("submit-button.png")
print("Submit button:", coords)
pag.moveTo(coords[0], coords[1], 1)
pag.click()
