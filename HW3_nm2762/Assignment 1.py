
# coding: utf-8

# In[222]:

import numpy as np
import matplotlib.pyplot as pt
import pylab as pl
get_ipython().magic('matplotlib inline')
np.random.seed(299)

df = 100
mysize = (2000 / (np.array(range(1, 101)))).astype(int)





    


# In[ ]:




# In[ ]:




# In[223]:

def create_chisq_size(df,n):
    return np.random.chisquare(df, size = n).mean()

chisquare_mean = []
for n in mysize:
    chisquare_mean.append (create_chisq_size(df,n))
    

pl.plot(mysize, chisquare_mean, 'o')
pl.xlabel('sample size', fontsize=18)
pl.ylabel('sample mean', fontsize=18) 

pl.figure(figsize=(10, 10))
pl.hist(chisq_mean,bins=30)
pl.xlabel('sample mean', fontsize = 18)
pl.ylabel('N', fontsize = 18)


# In[224]:

def create_normal(center, standardev, number):
    return np.random.normal (center, standardev, number ).mean()



norma_mean = []
for n in mysize: 
    norma_mean.append (create_normal(df,20,n))
    
pl.plot(mysize, norma_mean, 'o')
pl.xlabel('sample size', fontsize=18)
pl.ylabel('sample mean', fontsize=18) 


pl.figure(figsize=(10, 10))
pl.hist(norma_mean,bins=30)
pl.xlabel('sample mean', fontsize = 18)
pl.ylabel('N', fontsize = 18)


# In[225]:


def create_poisson(lam, size):
    return np.random.poisson(lam, size = n).mean()
    
    
    
poisson_mean = []
for n in mysize:
    poisson_mean.append (create_poisson(df,n))
    

pl.plot(mysize, poisson_mean, 'o')
pl.xlabel('sample size', fontsize=18)
pl.ylabel('sample mean', fontsize=18) 

pl.figure(figsize=(10, 10))
pl.hist(poisson_mean,bins=30)
pl.xlabel('sample mean', fontsize = 18)
pl.ylabel('N', fontsize = 18)


# In[226]:

def create_binomial(number, prob, size):
    return np.random.binomial(number, prob, size = n).mean()


binomial_mean = []
for n in mysize:
    binomial_mean.append (create_binomial(df,0.5,n))
    
pl.plot(mysize, binomial_mean, 'o')
pl.xlabel('sample size', fontsize=18)
pl.ylabel('sample mean', fontsize=18) 

pl.figure(figsize=(10, 10))
pl.hist(binomial_mean,bins=30)
pl.xlabel('sample mean', fontsize = 18)
pl.ylabel('N', fontsize = 18)



# In[227]:

def create_pareto(number, size):
    return np.random.pareto(number, size = n).mean()


pareto_mean = []
for n in mysize:
    pareto_mean.append (create_pareto (df, n))
    
pl.plot(mysize, pareto_mean, 'o')
pl.xlabel('sample size', fontsize=18)
pl.ylabel('sample mean', fontsize=18) 



pl.figure(figsize=(10, 10))
pl.hist(pareto_mean,bins=30)
pl.xlabel('sample mean', fontsize = 18)
pl.ylabel('N', fontsize = 18)




# In[ ]:




# In[ ]:




# In[ ]:



