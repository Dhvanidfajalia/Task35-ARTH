#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


pic1 = cv2.imread('pics/black_stone.png')
pic2 = cv2.imread('pics/white-stone.png')


# In[3]:


horiPic = np.concatenate((pic1,pic2),axis=1)

cv2.imshow('Horizontal', horiPic)
cv2.waitKey()
cv2.destroyAllWindows()


# In[4]:


VertiPic = np.concatenate((pic1,pic2),axis=0)

cv2.imshow('Vertical', VertiPic)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




