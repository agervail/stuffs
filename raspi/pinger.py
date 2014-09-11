# -*- coding: utf-8 -*-

__author__ = 'agervail'
import requests
import os.path
import datetime
import csv

res = requests.get('http://ping.probayes.net/')
print res.text

if os.path.isfile('ping_result.csv'):
    d = []
    with open('ping_result.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            d.append(row)
    d.append([datetime.datetime.now(),res.elapsed.total_seconds(),res.status_code])
    with open('ping_result.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(d)

    '''
    df = pd.DataFrame.from_csv('ping_result.csv')
    df2 = pd.DataFrame({'delay': [res.elapsed.total_seconds()], 'code': [res.status_code]},
                       index=[datetime.datetime.now()])
    df = df.append(df2)
    # import ipdb; ipdb.set_trace()
    df.to_csv('ping_result.csv')
    df['delay'].plot()
    plt.savefig('graph_pings.jpg')
    '''
else:
    d = [[datetime.datetime.now(),res.elapsed.total_seconds(),res.status_code]]
    with open('ping_result.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(d)
    '''
    df = pd.DataFrame({'delay': [res.elapsed.total_seconds()], 'code': [res.status_code]},
                      index=[datetime.datetime.now()])
    df.to_csv('ping_result.csv')
    '''