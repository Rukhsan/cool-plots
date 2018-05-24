
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import numpy as np
import seaborn
get_ipython().magic(u'matplotlib inline')


# In[10]:


plt.imshow(np.random.rand(10,10),interpolation="none")


# In[12]:


y=np.random.rand(1000)
plt.plot(y)


# In[13]:


x=np.linspace(-10.,10.,1000)
y=np.sin(3.*x)*np.exp(-1.*x**2)
plt.plot(x,y)


# In[15]:


x=np.random.rand(100)
y=x+np.random.rand(100)
plt.scatter(x,y)


# In[16]:


from matplotlib.colors import LogNorm
x=np.random.randn(100000)
y=np.random.randn(100000)+5.0
plt.hist2d(x,y,bins=40,norm=LogNorm())


# In[18]:


df=seaborn.load_dataset("iris")
df.head(5)
seaborn.pairplot(df,hue="species",size=2.5)

