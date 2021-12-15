# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:05:46 2021

@author: Aleksandar
"""

import pandas as pd
import sqlite3

date_df = pd.DataFrame({"Date": pd.date_range("01-01-2021", "31-12-2031")})

date_df["Day"] = date_df.Date.dt.day

date_df["Day_in_Week"] = date_df.Date.dt.weekday

date_df["Week"] = date_df.Date.dt.isocalendar().week

date_df["Month"] = date_df.Date.dt.month

date_df["Quarter"] = date_df.Date.dt.quarter

date_df["Year"] = date_df.Date.dt.year

date_df["Year_half"] = (date_df.Quarter + 1) // 2

date_df.insert(0, 'date_id', (date_df.Year.astype(str) + date_df.Month.astype(str).str.zfill(2) + date_df.Day.astype(str).str.zfill(2)).astype(int))


konekcija = sqlite3.connect("chinook.db")
kursor = konekcija.cursor()
kursor.execute("DROP TABLE IF EXISTS dim_date;")
date_df.to_sql("dim_date", konekcija)


read = pd.read_sql_query("SELECT * FROM dim_date WHERE year = 2021 AND month = 4 AND date_id < 20210410;", konekcija)

print(read)
