class Solution(object):
    def corpFlightBookings(self, bookings, max_flight):
        n = len(bookings)
        diff = [0]*max_flight
        for i in range(n):
            start = bookings[i][0]
            end = bookings[i][1]
            seats = bookings[i][2]
            if(max_flight>end):
                diff[end]-=seats
                
            diff[start-1]+=seats
        for i in range(1,max_flight):
            diff[i]+=diff[i-1]
        return diff