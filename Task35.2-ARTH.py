#!/usr/bin/env python
# coding: utf-8

# In[54]:


import cv2
minion1=cv2.imread('Pictures/minion1.jfif')
minion2=cv2.imread('Pictures/minion2.jfif')
minion11=cv2.imread('Pictures/minion1.jfif')
cv2.imshow("Minion Image1", minion1)
cv2.imshow("Minion Image2", minion2)
cv2.waitKey()
cv2.destroyAllWindows()


# In[58]:


minion2_face=minion2[30:210,30:210]
cv2.imshow("Minion2 face image", minion2_face)
cv2.waitKey()
cv2.destroyAllWindows()
print(minion2_face.shape)


# In[59]:


minion1_face=minion11[30:210,30:210]
cv2.imshow("Minion1 face image", minion1_face)
cv2.waitKey()
cv2.destroyAllWindows()
print(minion1_face.shape)


# In[60]:


minion2_face=minion2[210:30,210:30]
minion11[210:30,210:30]=minion2_face
cv2.imshow("Minion1 face image", minion1)
cv2.waitKey()
cv2.destroyAllWindows()


# In[61]:


minion1_face=minion11[210:30,210:30]
minion2[210:30,210:30]=minion1_face
cv2.imshow("Minion2 face image", minion1)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




