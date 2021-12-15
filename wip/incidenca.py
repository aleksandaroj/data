import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

datumi = pd.date_range('2021-10-06', date.today(), freq='d').to_list()
broj_zarazenih = [2965, 3572, 3154, 2971, 2846, 2583, 2069, 2604, 2965, 2864, 2719, 2384, 2068, 1695, 1987, 2145, 2138,
                  2007, 1613, 1374, 989, 1249, 1304, 1402, 1366, 1277, 1056, 834, 918, 1125, 1046, 901, 787, 705, 568,
                  575, 686, 609, 550, 391, 404, 266, 376, 414, 387, 326, 330, 274, 178, 248, 230, 287, 218, 210, 145,
                  116, 162, 214, 198, 210, 172, 119, 138, 124, 132, 160, 135, 162, 89, 60, 88]
inzidenzLevel = [7, 10, 14]
n = []

try:
    df = pd.DataFrame({'Datum': datumi, 'BrojZ': broj_zarazenih})
    for i in inzidenzLevel:
        g = str(i) + '-Tage Inzidenz'
        n.append(g)
        df[g] = df['BrojZ'].rolling(window=i).sum() / 69.6
    # df = df[inzidenzLevel[0] - 1:]  # umesto sklanjanja prvog dela gde nema podataka
    df = df.tail(inzidenzLevel[-1] + 1)  # dodacemo da se crta samo poslednjih 15 dana
    # df.plot.line(x='Datum', y=n, ylim=(0, 200)).axhline(y=35, color='red')
    df.plot.line(x='Datum', y=n).axhline(y=35, color='red')
    plt.show()
except ValueError:
    print('Nema dovoljno podataka.')
