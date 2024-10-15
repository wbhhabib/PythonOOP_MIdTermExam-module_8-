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

    
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)


        seats_layout = [['free' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[show_id] = seats_layout
        


    def book_seats(self, id, seat_info):

        if id not in self.seats:
            print(f"Show ID {id} not found.")
            return

        for seat in seat_info:
            row = seat[0]
            col = seat[1]

            if 0 < row <= self.rows and 0 < col <= self.cols:
                if (self.seats[id])[row-1][col-1] == 'free':
                    (self.seats[id])[row-1][col-1] = 'booked'
    


    def view_show_list(self):
        print(f"All Show List: {self.show_list}")


    def view_available_seats(self,id):
        for x in self.seats[id]:
            print(x)
        print('\n')


hall1 = Hall(10, 15, 1)

hall1.entry_show(1, "Movie A", "6:00 PM")

hall1.book_seats(1, [(2, 3), (5, 7), (9, 14),(0,2),(2,16)])

hall1.view_available_seats(1)
hall1.view_show_list()


