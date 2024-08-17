import matplotlib.pyplot as plt
import requests
import pandas as pd


def pull_values(field_name, dataset):
    result = []
    for i in range(0, len(dataset)):
        result.append(float(dataset[i][field_name]))

    result.reverse()
    return result

data = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AVGO&apikey=19DT3TWG12D6GJOJ")
if data.status_code == 200:
    stock_monthly_data = data.json()['Monthly Time Series']

print(stock_monthly_data)

time = list(stock_monthly_data.keys())

time.reverse()

values = list(stock_monthly_data.values())

close = pull_values('4. close', values)



open = pull_values('1. open', values)

df = pd.DataFrame()

df['open'] = open
df['close'] = close




plt.plot(time, df)
#
plt.show()

'''
{
    'time' : {
            1.open: 
            }
}
'''

 #Saumya was here
