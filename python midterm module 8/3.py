class Star_Cinema: 
    hall_list= []

    def entry_hall(self,num):
        self.hall_list.append(num)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no): 
        self.seats = {}  
        self.show_list = []  
        self.rows = rows  
        self.cols = cols  
        self.hall_no = hall_no  
        self.hall_list.append(self)

    
    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        

        seats_layout = [['free']*self.cols]*self.rows        
        self.seats[id] = seats_layout


hall1 = Hall(5, 5, 1)
hall1.entry_show("S1", "Movie A", "6:00 PM")


for hall in Star_Cinema.hall_list:
    print(f"Hall No:  , {hall.hall_no}")
    print(f"Shows:  , {hall.show_list}")
    print(f"Seats:  , {hall.seats}")
    