# -*- coding: utf-8 -*-
__author__ = 'agervail'

import matplotlib.pyplot as plt


with open('temperatures.txt', 'r') as f:
    lines = f.readlines()

temps = []
for l in lines:
    temps.append(float(l))


deriv = []
pics = []
falsePics = []
count = 0
for i in range(len(temps)-3):
    deriv.append(temps[i+2] - temps[i])
#     if deriv[-1] > 0.3:
#         count += 1
# print count
dist = 20
dTemp = 1.0
seuil = 0.3
lderiv = len(deriv)
i = 0
while i < lderiv:
#for i in range(lderiv):
    d = deriv[i]
    if abs(d) > seuil:
        chgtSigne = False
        minTemp = temps[i]
        maxTemp = temps[i]
        for j in range(i, min(i+dist, lderiv-1)):
            minTemp = min(minTemp, temps[j])
            maxTemp = max(maxTemp, temps[j])
            dd = deriv[j]
            if not chgtSigne and (dd * deriv[j+1] <= 0):
                chgtSigne = j + 1
            if chgtSigne and dd * (abs(d) / d * -1) > seuil:
                print 'picfound', d, dd, dd * (abs(d) / d * -1), i, j, maxTemp, minTemp

                if maxTemp - minTemp > dTemp:
                    print maxTemp - minTemp, 'OK'
                    pics.append(chgtSigne)
                else:
                    falsePics.append(chgtSigne)
                picFound = True
                i = j
                break
    i += 1
print pics

fig, ax1 = plt.subplots()

ax1.plot(temps)
plt.grid(True)
plt.xlabel(u'Temps (Minutes)')
plt.ylabel(u'Température (°C)')
plt.scatter(pics, [temps[x] for x in pics], c='r', s=[160]*len(pics), alpha=0.5)
# pics = falsePics
#plt.scatter(pics, [temps[x] for x in pics], c='r', s=[80]*len(pics), alpha=0.5)
# ax2 = ax1.twinx()
# ax2.plot(deriv, 'r')

plt.show()

'''
plt.plot(temps)
plt.plot(deriv)
plt.grid(True)
plt.xlabel(u'Temps (Minutes)')
plt.ylabel(u'Température (°C)')
plt.show()
'''