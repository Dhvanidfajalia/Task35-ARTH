#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import numpy as np


# In[5]:


frame = np.zeros([650,650,3], np.uint8)

pt1 = (200,100)
pt2 = (100,200)
pt3 = (300,200)
pt4 = (400,100)
pt5 = (500,200)
sq1 = (250, 400)
sq2 = (250, 400)
rec1 = (150, 200)
rec2 = (450, 400)

clr = (0, 255, 0)

def drawline(point1,point2):
    return cv2.line(frame, point1, point2, clr,2)

drawimg = drawline(pt1,pt2)
drawimg = drawline(pt1,pt3)
drawimg = drawline(pt2,pt3)
drawimg = drawline(pt1,pt4)
drawimg = drawline(pt3,pt5)
drawimg = drawline(pt4,pt5)
drawimg = drawline(pt3,pt5)
drawimg = drawline(sq1,sq2)
drawimg = cv2.rectangle(frame, rec1, rec2, clr, 2)

cv2.imshow('image', drawimg)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




