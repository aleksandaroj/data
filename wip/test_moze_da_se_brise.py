# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:06:00 2021

@author: Aleksandar
"""
import requests as r
from bs4 import BeautifulSoup
import pandas as pd
import pycountry
from dataprep.clean import clean_country

df_active_volc = pd.read_csv('most_active_volcanoes.csv')

df_active_volc

clean_country(df_active_volc, 'country')

df_active_volc_a2 = clean_country(df_active_volc, column='country')

## Creation a list of countries and continents

df = pd.DataFrame({'country': ['American Samoa', 'Canada', 'France', 'Serbia']})

df2 = clean_country(df, 'country', output_format='alpha-2')

clean_country(df_active_volc, column='country', output_format='alpha-2')

df_active_volc = df_active_volc['Country'].pycountry.countries.get(name)

def findCountry (country_name):
    try:
        return pycountry.countries.get(name=country_name).alpha_2
    except:
        return ("not founded")

df_active_volc['country_alpha_2'] = df_active_volc.apply(lambda row: findCountry(row.country_name), axis = 1)

