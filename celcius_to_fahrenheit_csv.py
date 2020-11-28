import pandas as pd

cold_weather_data = pd.read_csv('WeatherData/ColdnHumid/halifax/halifaxWeatherTotalCelsius.csv')

def celcius_to_fahrenheit(temperature):
    return round(((temperature * 9/5) + 32), 2)

cold_weather_data['Max Temp (°C)'] = cold_weather_data.apply(lambda row: celcius_to_fahrenheit(row['Max Temp (°C)']), axis=1)
cold_weather_data['Min Temp (°C)'] = cold_weather_data.apply(lambda row: celcius_to_fahrenheit(row['Min Temp (°C)']), axis=1)

cold_weather_data['Max Temp (°C)'].fillna(round(cold_weather_data['Max Temp (°C)'].mean(), 2), inplace=True)
cold_weather_data['Min Temp (°C)'].fillna(round(cold_weather_data['Min Temp (°C)'].mean(), 2), inplace=True)

cold_weather_data.to_csv(path_or_buf='WeatherData/ColdnHumid/halifax/halifaxWeatherTotal.csv')
