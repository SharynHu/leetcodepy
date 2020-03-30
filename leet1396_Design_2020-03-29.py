class UndergroundSystem(object):

    def __init__(self):
        self.passengers = {}
        self.stations = {}
    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if id not in self.passengers:
            self.passengers[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStation, startTime = self.passengers[id]
        endStation, endTime = stationName, t
        if (startStation, endStation) not in self.stations:
            self.stations[(startStation, endStation)] = (0, 0)
        countPassengers, allTime = self.stations[(startStation, endStation)]
        self.stations[(startStation, endStation)] = countPassengers+1, allTime+endTime-startTime
        self.passengers.pop(id)
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        countPassengers, allTime = self.stations[(startStation, endStation)]
        return float(allTime)/countPassengers
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
