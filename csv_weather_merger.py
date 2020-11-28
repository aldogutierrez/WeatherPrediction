import pandas as pd
import os.path

file2015 = pd.read_csv('WeatherData/ColdnHumid/halifax/halifax_2015_P1D.csv')
file2016 = pd.read_csv('WeatherData/ColdnHumid/halifax/halifax_2016_P1D.csv')
file2017 = pd.read_csv('WeatherData/ColdnHumid/halifax/halifax_2017_P1D.csv')
file2018 = pd.read_csv('WeatherData/ColdnHumid/halifax/halifax_2018_P1D.csv')
file2019 = pd.read_csv('WeatherData/ColdnHumid/halifax/halifax_2019_P1D.csv')

complete = pd.concat([file2015, file2016, file2017, file2018, file2019], ignore_index=False)

save_path = 'WeatherData/ColdnHumid/halifax'

fileExt = 'halifaxWeatherTotalCelsius.csv'

completeName = os.path.join(save_path, fileExt)

solarFile = open(completeName, mode='w')
complete.to_csv(path_or_buf=completeName)

solarFile.close()