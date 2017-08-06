
# coding: utf-8

# In[8]:

import numpy as np
import pandas as pd
with open('duto_60_60_362_re4800_les_dyn_periodic3.txt', "r") as f:
    for line in f:
        cleanedLine = line.strip()
        if cleanedLine: # is not empty
            teste=np.loadtxt('duto_60_60_362_re4800_les_dyn_periodic3.txt',comments="#",usecols=(1,2,3,4,5,6,7,8,9,10))


# In[13]:

teste2={'coluna 1':teste[:,0],'coluna 2':teste[:,1],'coluna 3':teste[:,2],'coluna 4':teste[:,3],
        'coluna 5':teste[:,4],'coluna 6':teste[:,5],'coluna 7':teste[:,6],'coluna 8':teste[:,7],
        'coluna 9':teste[:,8],'coluna 10':teste[:,9]}


# In[17]:

teste3=pd.DataFrame(teste2, columns = ['coluna 1', 'coluna 2', 'coluna 3', 'coluna 4', 
                                'coluna 5', 'coluna 6', 'coluna 7', 'coluna 8', 
                                'coluna 9', 'coluna 10'])


# In[18]:

ax = teste3.plot()
fig = ax.get_figure()
fig.savefig('asdf.png')


# In[ ]:



