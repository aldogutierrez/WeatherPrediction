import pandas as pd
import os.path

file2015 = pd.read_csv('WeatherData/ColdnDry/denver_hum/denver_hum_2015.csv')
file2016 = pd.read_csv('WeatherData/ColdnDry/denver_hum/denver_hum_2016.csv')
file2017 = pd.read_csv('WeatherData/ColdnDry/denver_hum/denver_hum_2017.csv')
file2018 = pd.read_csv('WeatherData/ColdnDry/denver_hum/denver_hum_2018.csv')
file2019 = pd.read_csv('WeatherData/ColdnDry/denver_hum/denver_hum_2019.csv')

complete = pd.concat([file2015, file2016, file2017, file2018, file2019], ignore_index=False)

save_path = 'WeatherData/ColdnDry/denver_hum'

fileExt = 'denverHumidityTotal.csv'

completeName = os.path.join(save_path, fileExt)

solarFile = open(completeName, mode='w')
complete.to_csv(path_or_buf=completeName)

solarFile.close()