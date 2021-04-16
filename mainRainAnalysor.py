import requests
import json
import pandas as pd
from matplotlib import pyplot as plt

url_r = requests.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/C-B0025-001?Authorization=CWB-F0F729CC-5010-4A48-96F0-61A90BCB1BCF&timeFrom=2020-06-01&timeTo=2021-04-10&statistics=false')
r = pd.DataFrame(json.loads(url_r.text))

dict_r = {}
for i, v in enumerate(r['records']['location']):
  dict_r[v['station']['stationNameEN']] = []
  for j in v['stationObsTimes']["stationObsTime"]:
    try:
      if j['weatherElements']['precipitation'] == 'T':
        #j['weatherElements']['precipitation'] = 0.1
        dict_r[v['station']['stationNameEN']].append(0.1)
      elif j['weatherElements']['precipitation'] == 'X':
        dict_r[v['station']['stationNameEN']].append(0.0)
      else: 
        dict_r[v['station']['stationNameEN']].append(float(j['weatherElements']['precipitation']))
    except:
      dict_r[v['station']['stationNameEN']].append(0.1)
      
      list_sum = []
for i in dict_r:
  list_sum.append(sum(dict_r[i]))
print(list_sum)

plt.plot(list_sum)
plt.show()
