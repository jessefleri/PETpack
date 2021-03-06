# -*- coding: utf-8 -*-
"""
Author: Jesse Fleri
Project: Climate projection comparison
Last revised: 2017-12-5
"""
import os
path = r'E:\wild4952\repository\code'
os.chdir(path)
import PETpack as pet
import folium
import json
import vincent
import pandas as pd

df = pd.read_excel(r'climate_data.xlsx',header=0)                     # Read climate data csv into pandas dataframe

web = folium.Map(                                                     # Create empty map and zoom to particular location
    location=[39.7370, -110.8338],
    zoom_start=7,
    tiles='Stamen Terrain')

for index, row in df.iterrows():                                      # Loop over dateframe 
    tem = row[1:13]                                                   # Monthly temperature values
    model = pet.ET1(tem,df.iloc[index,14],2000)                       # Run model with latitude pulled from dataframe row
    scatter = vincent.Line(model, width=400, height=200)              # Creater scatterplot
    scatter.axis_titles(x='Month', y='Potential ET (mm)')
    scatter.legend(title='Models')
    scatter_dict = json.loads(scatter.to_json())
    popup = folium.Popup(max_width=650)                               # Create popup space
    folium.Vega(scatter_dict, height=250, width=525).add_to(popup)    # Fill popup space with chart
    folium.CircleMarker([df.iloc[index,14], df.iloc[index,15]],       # Add to map before iterating again
                        color='crimson', fill=True, fill_color='crimson',
                        popup=popup).add_to(web)

web.save('pet-map.html')                                              # Save map