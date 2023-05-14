#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[29]:



pd.read_csv('covid.csv')
df = pd.read_csv('covid.csv')
df.head()


# In[30]:


columnas= [ 'id', 'patient_type', 'entry_date', 'date_symptoms', 'date_died', 'other_disease', 'icu' ]
df.drop(columnas, axis=1, inplace= True)
df.head()


# In[31]:


#filtrarlasfilas

df = df[df['covid_res'] != 3]
df.head()


# In[32]:


#filtrar las filas y eliminar aquellas que tengan el valor de  99 en contact_other_covid
df = df[df['contact_other_covid'] != 98]
df.head()


# In[33]:


df = df[df['intubed'] != 97]
df.head()


# In[34]:


df = df[df['asthma'] != 97]
df.head()


# In[35]:


df = df[df['hypertension'] != 97]
df.head()


# In[36]:


df = df[df['diabetes'] != 98]
df.head()


# In[37]:


df = df[df['obesity'] != 98]
df.head()


# In[38]:


df = df[df['pneumonia'] != 98]
df.head()


# In[39]:


df = df[df['renal_chronic'] != 98]


# In[40]:


df = df[df['tobacco'] != 97]


# In[41]:


nfilas = df.shape[0]
print("n",nfilas)


# In[42]:


#separar caracteristicas de la variable objetivo
x = df.drop('covid_res', axis= 1)
y = df['covid_res']


# In[43]:


#dividir entrenamiento de prueba



x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)


# In[44]:


#crear instancia del modelo

arbol_decision = DecisionTreeClassifier(random_state=1)


# In[45]:


#entrner modelo con el conjunto


arbol_decision.fit(x_train, y_train)


# In[46]:


#UTILIZAR EL MODELO PARA HACER CONJUNTO DE PRUEBAS

y_pred = arbol_decision.predict(x_test)


# In[47]:


#EVALUAR DESEMPEÑO DEL MODELO 
accuracy = accuracy_score(y_test, y_pred)
print("la precision del modelo es: ", accuracy)


# In[48]:


pip install graphviz


# In[49]:


entre=accuracy*100
print("porcentaje",entre)


# In[ ]:





# In[ ]:





# In[53]:


from sklearn.tree import DecisionTreeClassifier

arbol_decision = DecisionTreeClassifier(max_depth=3, min_samples_split=10)

arbol_decision.fit(x_train, y_train)


# In[54]:


from sklearn.tree import export_graphviz
import graphviz

# Exportar el árbol de decisiones
export_graphviz(arbol_decision, out_file='arbol_decision.dot', feature_names=x.columns.values, filled=True, rounded=True, special_characters=True)


# Convertir el archivo .dot a un objeto gráfico
with open('arbol_decision.dot') as f:
    dot_graph = f.read()

graph = graphviz.Source(dot_graph)

# Mostrar y guardar el gráfico
graph


# In[55]:


from IPython.display import Image
from graphviz import render

#render
render('dot', 'png', 'arbol_decision.dot')


# In[ ]:




