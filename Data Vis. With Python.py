#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# In[2]:


file =  'https://cocl.us/datascience_survey_data'
df = pd.read_csv(file)
df


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.sort_values(by=['Very interested'], inplace=True, ascending=False)
df.rename(columns={'Unnamed: 0':'Topic'},inplace=True)
df_perc = df[['Topic']]
df_perc = df_perc.join((df[['Very interested','Somewhat interested','Not interested']]/2233)*100)
df_perc.set_index('Topic', inplace=True)
df_perc.round(2)


# In[4]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# In[5]:


labels =['Data Analysis / Statistics','Machine Learning','Data Visualization','Big Data (Spark / Hadoop)','Deep Learning','Data Journalism']
very_int = df_perc['Very interested']
some_int = df_perc['Somewhat interested']
not_int = df_perc['Not interested']

ind = np.arange(len(very_int))  
width = 0.3

fig, ax = plt.subplots(figsize=(20,8))
rects1 = ax.bar(ind - width, very_int, width, label='Very interested', color='#5cb85c')
rects2 = ax.bar(ind, some_int, width, label='Somewhat interested', color='#5bc0de')
rects3 = ax.bar(ind + width, not_int, width, label='Notr interested', color='#d9534f')

ax.set_title("Percentage of Respondents' Interest In Data Science Areas", fontsize=16)
ax.set_xticks(ind)
ax.set_xticklabels((labels))
ax.get_yaxis().set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=14)

def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height().round(2)
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  
                    textcoords="offset points", 
                    ha=ha[xpos], va='bottom', fontsize=14)


autolabel(rects1, "center")
autolabel(rects2, "center")
autolabel(rects3, "center")


fig.tight_layout()

plt.show()


# In[6]:


file =  'https://cocl.us/sanfran_crime_dataset'
df_sf = pd.read_csv(file)
df_sf.head()


# In[7]:


df_sf_neigh = df_sf.groupby(["PdDistrict"]).count().reset_index()
df_sf_neigh.drop(df_sf_neigh.columns.difference(['PdDistrict','IncidntNum']), 1, inplace=True)
df_sf_neigh.rename(columns={'PdDistrict':'Neighborhood','IncidntNum':'Count'}, inplace=True)
df_sf_neigh


# In[8]:


get_ipython().system('wget --quiet https://cocl.us/sanfran_geojson')
get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium

print('Folium installed and imported!')
print('GeoJSON file downloaded!')


# In[10]:


sf_geo = 'https://cocl.us/sanfran_geojson'

sf_latitude = 37.77
sf_longitude = -122.42
sf_map = folium.Map(location=[sf_latitude,sf_longitude], zoom_start=12)


# In[11]:


sf_map.choropleth(
    geo_data=sf_geo,
    data=df_sf_neigh,
    columns=['Neighborhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Crime Rate per District in San Francisco')

sf_map


# In[ ]:




