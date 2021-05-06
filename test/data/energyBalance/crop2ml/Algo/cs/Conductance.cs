double h;
h = Math.Max(10, plantHeight) / 100;
conductance = (wind * Math.Pow(vonKarman, 2)) / (Math.Log((heightWeatherMeasurements - d * h) / (zm * h)) * Math.Log((heightWeatherMeasurements - d * h) / (zh * h)));
