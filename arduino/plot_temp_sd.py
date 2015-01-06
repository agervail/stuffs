#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import datetime

begin = datetime.datetime(2014,12,28,22,17)

df = pd.DataFrame.from_csv('TEMP.TXT', header=None)

#df.index = [k / 60000.0 for k in df.index]
df.index = [begin + datetime.timedelta(milliseconds=k) for k in df.index]

df.plot()

plt.show()
