import pandas as pd
import os.path

solarData = pd.read_csv('WeatherData/ColdnHumid/halifax/halifaxSolar/halifaxSolarTotal.csv')
weatherData = pd.read_csv('WeatherData/ColdnHumid/halifax/halifaxWeatherTotal.csv')

complete = pd.concat([weatherData, solarData], axis=1)
save_path = 'WeatherData/ColdnHumid'

fileExt = 'halifax_Weather_Solar.csv'

completeName = os.path.join(save_path, fileExt)

testFile = open(completeName, mode='w')
complete.to_csv(path_or_buf=completeName)

testFile.close()