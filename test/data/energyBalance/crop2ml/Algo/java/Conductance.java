double h;
h = Math.max(10, plantHeight) / 100;
conductance = (wind * Math.pow(vonKarman, 2)) / (Math.log((heightWeatherMeasurements - d * h) / (zm * h)) * Math.log((heightWeatherMeasurements - d * h) / (zh * h)));
