from OpenGL.GL import * 
from OpenGL.GLU import *
 from OpenGL.GLUT import * 
 print('package Import Successful')  
#height and width of screen w, h = 500, 500  
# function to pass floating points 
def float_range(start,stop,step=0.1):   
  x=start     
  while x<=stop:      
  yield x       
  x=x+step  
# functon of horizontal line def showScreenHorizontal():   
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   
  glLoadIdentity()     
  glColor3f(1.0,0.0,0.0)    
  glPointSize(10.0)     
  glBegin(GL_POINTS)     
  rf=float_range(x1Value,x2Value)   
  for i in rf:        
  glVertex2f(i,yValue)   
  glVertex2f(x1Value, yValue)    
  glEnd()     
  glFlush() 
