import pygame

class Cubo:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.ancho = 50
    self.alto  = 50
    self.velocidad = 1
    self.color = "red"
    self.rec = pygame.Rect(self.x,self.ancho, self.alto)
    

  
  def  dibujar(self, ventana):
    pygame.draw.rect(ventana, self.color, self.rect)
