ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode([ALTO,ANCHO])

jugando=True

while jugando:
  eventos=pygame.event.get()

  for evento in eventos:
    if evento.type ==pygame.QUIT:
      jugando = False
  
  pygame.display.update()
  quit()
