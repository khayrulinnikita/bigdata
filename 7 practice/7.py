import pandas as pd
import tarantool
connection = tarantool.connect("localhost", 3301, user='admin', password='pass')

tester = connection.space('queue')


data = tester.select()

df = pd.DataFrame(data, columns=['Day', 'TickTime', 'Speed'])

print('median speed = ', df.groupby(['Day'])['Speed'].median())
print('min ticktime', df.groupby(['Day'])['TickTime'].min())
print('max ticktime:', df.groupby(['Day'])['TickTime'].max())
