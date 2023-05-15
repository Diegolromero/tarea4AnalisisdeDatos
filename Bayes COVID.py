#!/usr/bin/env python
# coding: utf-8

# In[15]:


p_fatiga_given_covid = 0.90
p_tos_seca_given_covid = 0.70
p_dificultad_respirar_given_covid =0.60
p_dolor_garganta_given_covid = 0.50
p_dolor_cabeza_given_covid = 0.60
p_dolor_cuerpo_given_covid =0.50
p_escalofrios_given_covid = 0.40
p_secrecion_nasal_given_covid = 0.20
p_perdida_sentido_given_covid =0.50
p_fiebre_given_covid = 0.80
p_dolor_pecho_given_covid =0.30


p_covid = 0.05 

sintomas = ['Fatiga', 'Tos seca', 'Dificultad para respirar', 'Dolor de garganta','Dolor de cabeza',
          'Dolor en el cuerpo', 'EscalofrÍos', 'Secreción nasal', 'Pérdida del sentido del olfato o del gusto',
          'Fiebre', 'Dolor de pecho']


p_sintomas_given_covid = p_fatiga_given_covid *p_tos_seca_given_covid *p_dificultad_respirar_given_covid *                           p_dolor_garganta_given_covid * p_dolor_cabeza_given_covid * p_dolor_cuerpo_given_covid *                          p_escalofrios_given_covid *p_secrecion_nasal_given_covid * p_perdida_sentido_given_covid *                          p_fiebre_given_covid * p_dolor_pecho_given_covid
            
p_sintomas_given_no_covid = 0.05 **11

p_sintomas = p_sintomas_given_covid * p_covid + p_sintomas_given_no_covid * (1- p_covid)

p_covid_given_sintomas = p_sintomas_given_covid * p_covid / p_sintomas 


print(f"la prohabilidad deque el paciente tenga COVID 19 dados los sintoams es: {p_covid_given_sintomas}")


# In[ ]:




