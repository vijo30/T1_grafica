from pixel_paint_model import *
import glfw
import sys
from typing import Union


class Controller:
  grid: Union['Grid', None]
  palette: Union['Palette', None]
  
  def __init__(self):
    self.grid = None
    self.palette = None
    self.mousePos = (0.0, 0.0)
    
  def set_grid(self, g):
    self.grid = g
    
  def set_palette(self, p):
    self.palette = p
    
  def on_key(self, window, key, scancode, action, mods):
    if not (action == glfw.PRESS or action == glfw.RELEASE):
        return
    
    if key == glfw.KEY_ESCAPE:
        sys.exit()
        

    elif key == glfw.MOUSE_BUTTON_1 and action == glfw.PRESS:
      pass
      # Pick color only if you don't already have picked it
    
    elif key == glfw.KEY_S and action == glfw.PRESS:
      # Save the raster image
      pass
    
    else:
      print('Unknown key')
      
    def cursor_pos_callback(window, x, y):
      self.mousePos = (x, y)
    
    def mouse_button_callback(window, button, action, mods):
      """
      glfw.MOUSE_BUTTON_1: left click
      glfw.MOUSE_BUTTON_2: right click
      glfw.MOUSE_BUTTON_3: scroll click
      """

      if (action == glfw.PRESS) and (button == glfw.MOUSE):
        if glfw.get_cursor_pos(window)[0] < 590 and glfw.get_cursor_pos(window)[1] > 90:
          self.grid.draw_quad(1, 0, 0, mouse_pos(window)[0], mouse_pos(window)[1], 16)
    