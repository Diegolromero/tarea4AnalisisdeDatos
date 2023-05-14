#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score



pd.read_csv('covid.csv')
df = pd.read_csv('covid.csv')

columnas= [ 'id', 'patient_type', 'entry_date', 'date_symptoms', 'date_died', 'other_disease', 'icu' ]
df.drop(columnas, axis=1, inplace= True)

#filtrarlasfilas

df = df[df['covid_res'] != 3]
df = df[df['contact_other_covid'] != 98]
df = df[df['intubed'] != 97]
df = df[df['asthma'] != 97]
df = df[df['hypertension'] != 97]
df = df[df['diabetes'] != 98]
df = df[df['obesity'] != 98]
df = df[df['pneumonia'] != 98]
df = df[df['renal_chronic'] != 98]
df = df[df['tobacco'] != 97]


#separar caracteristicas de la variable objetivo
x = df.drop('covid_res', axis= 1)
y = df['covid_res']

#dividir entrenamiento de prueba

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print('precision del modelo: ',accuracy)

print("el porcentaje de precision del modelo es de: ",(accuracy*100),"%")

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

features = ['sex', 'intubed', 'pneumonia', 'age', 'diabetes', 'copd', 'inmsupr', 'hypertension', 'cardiovascular', 'pregnancy', 'obesity', 'tobacco', 'contact_other_covid', 'renal_chronic']
target = 'covid_res'

x = df[features]
y = df[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)

con_mat = confusion_matrix(y_test, y_pred)

print(con_mat)


import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(6, 4))

sns.heatmap(con_mat, annot=True, cmap="Blues", fmt="d", xticklabels=["negativo", "positivo"], yticklabels=["negativo", "positivo"])

ax.set_xlabel('predicción')
ax.set_ylabel('valor real')
ax.set_title('Matriz de Confusión')

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




