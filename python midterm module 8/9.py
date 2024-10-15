class Star_Cinema: 
    hall_list= []

    def entry_hall(self,num):
        self.hall_list.append(num)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        #seats is a private attribute
        self.__seats = {}  
        self.show_list = []  
        self.rows = rows  
        self.cols = cols  
        self.hall_no = hall_no  
        self.hall_list.append(self)

    
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)


        seats_layout = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.__seats[show_id] = seats_layout
        


    def book_seats(self, id, seat_info):

        if id not in self.__seats:
            print(f"Show ID {id} not found.")
            return

        for seat in seat_info:
            row = seat[0]
            col = seat[1]

            if 0 < row <= self.rows and 0 < col <= self.cols:
                if (self.__seats[id])[row-1][col-1] == 0:
                    (self.__seats[id])[row-1][col-1] = 1
                    print(f"Seat ({row}, {col}) has been successfully booked.")
                else:
                    print(f"Seat ({row}, {col}) is already booked.")
            else:
                print(f"Invalid seat position ({row}, {col}).")


    def view_show_list(self):
        print('\n')
        for xx in self.show_list :
            print(f"MOVIE NAME: {xx[1]} SHOW ID: {xx[0]} TIME: {xx[2]}")
        print('\n')

    def view_available_seats(self,id):
        print(f"Available seats for show {id} : ")
        for x in self.__seats[id]:
            print(x)
        print('\n')


hall1 = Hall(10, 15, 1)
hall1.entry_show('1', "Movie A", "6:00 PM")
hall1.book_seats('1', [(2, 3), (5, 7), (9, 14),(0,2),(2,16)])


def show_option():
    print(".....................................")
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")

aa = True

while aa:
    show_option()
    opt = input("ENTER OPTION: ")
    if opt=='1':
        hall1.view_show_list()
    elif opt=='2':
        s_id = input("ENTER SHOW ID: ")
        hall1.view_available_seats(s_id)
    elif opt =='3':
        ss_id = input("Show ID: ")
        n_o_t = input("Number of Ticket? : ")
        n_o_t = int(n_o_t)
        while n_o_t:
            s_r = input("Enter seat Row : ")
            s_c =  input("Enter seat Col : ")
            s_r = int(s_r)
            s_c = int(s_c)
            hall1.book_seats(ss_id, [(s_r, s_c)])
            n_o_t-=1
    elif opt == '4':
        aa = False
    else :
        print("Wrong input.")


