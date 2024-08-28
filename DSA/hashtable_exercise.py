class Weather():
    def __init__(self):
        try:
            self.nyc_temp = []
            with open('nyc_weather.csv', 'r') as f:
                next(f)  
                for line in f:
                    line = line.strip()
                    token = line.split(',')
                    day = token[0]
                    temp = float(token[1])
                    self.nyc_temp.append([day, temp])
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(f'An error occurred: {e}')
    def weekAvg(self):
        if len(self.nyc_temp) < 7:
            return 'Not enough data to calculate average'
        count = 0
        sum = 0
        for i,j in self.nyc_temp:
            if count > 7:
                break
            sum += j
        return sum/7
    

if __name__ == "__main__":
    weather = Weather()
    # weather.weekAvg()
    print(f'Average temperature for the past week in NYC: {weather.weekAvg()}')