import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

vertex_src = """
# version 330
in vec3 a_position;
in vec3 a_color;
out vec3 v_color;
void main()
{
    gl_Position = vec4(a_position, 1.0);
    v_color = a_color;
}
"""

fragment_src = """
# version 330
in vec3 v_color;
out vec4 out_color;
void main()
{
    out_color = vec4(v_color, 1.0);
}
"""

# initialize glfw
if not glfw.init():
  raise Exception("glfw can not be initialized!")

# create window
window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

# check if window was created
if not window:
  glfw.terminate()
  raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 400, 200)

# make the context current
glfw.make_context_current(window)



# vertices and color of the triangle

vertices = [-0.5,-0.5, 0.0, 1.0, 0.0, 0.0,
             0.5,-0.5, 0.0, 0.0, 1.0, 0.0,
             0.0, 0.5, 0.0, 0.0, 0.0, 1.0]
             
            
            

# convert list to array

vertices = np.array(vertices, dtype=np.float32)

# pipeline
shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

position = glGetAttribLocation(shader, "a_position")
glEnableVertexAttribArray(position)
glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

color = glGetAttribLocation(shader, "a_color")
glEnableVertexAttribArray(color)
glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

glUseProgram(shader)
glClearColor(0, 0.1, 0.1, 1) # window colors

# the main loop
while not glfw.window_should_close(window):
  glfw.poll_events()
  
  glClear(GL_COLOR_BUFFER_BIT) # change window color
   
  glDrawArrays(GL_TRIANGLES, 0, 3) # draw
  
  glfw.swap_buffers(window)
  
# terminate glfw
glfw.terminate()