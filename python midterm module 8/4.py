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


hall1 = Hall(10, 15, 1)

hall1.entry_show("S1", "Movie A", "6:00 PM")
hall1.book_seats("S1", [(2, 3), (5, 7), (9, 14)])
hall1.book_seats("S1", [(2, 3), (0, 0), (11, 15)])



hall2 = Hall(8, 12, 2)
hall2.entry_show("S2", "Movie B", "8:00 PM")
hall2.entry_show("S1", "Movie B", "8:00 PM")
hall2.book_seats("S2", [(1, 1), (7, 11), (4, 5)])


for hall in Star_Cinema.hall_list:
    print("................................................................................")
    print(f"Hall No: {hall.hall_no}")

    print('SHOWS: ')
    for xx in hall.show_list :
        print(f"MOVIE NAME: {xx[1]} SHOW ID: {xx[0]} TIME: {xx[2]}")
    print('\n')

    for key in hall.seats:
        print(f"Show Id: {key}")
        print(f"Seats : ")
        for x in hall.seats[key]:
            print(x)
        print('\n')
