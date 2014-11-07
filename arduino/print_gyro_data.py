import time
import pandas as pd


df = pd.DataFrame.from_csv('GYRO.TXT', header=-1)
#df = df.head(50)
df.columns = ['yaw', 'pitch', 'roll']
data_offset = df.index[0]



of = round(time.time() * 1000) - data_offset

cmt = lambda: int(round(time.time() * 1000) - of)

i = 0
while i < len(df.index) - 1:
#for i in range(len(df.index)-1):
  #time.sleep(0.01)
  t = cmt()
  #print t, df.index[i]
  if t > df.index[i]:
    if t < df.index[i+1]:
      print df['yaw'][df.index[i]], df['pitch'][df.index[i]], df['roll'][df.index[i]]
    i += 1


#  else:
#    time.sleep(
