h = max(10, plantHeight) / 100.0
conductance = (wind * vonKarman** 2) / (log((heightWeatherMeasurements - d * h) / (zm * h)) * log((heightWeatherMeasurements - d * h) / (zh * h)))

