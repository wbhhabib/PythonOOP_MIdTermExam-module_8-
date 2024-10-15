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

hall1 = Hall(8, 2, 5)

for hall in Star_Cinema.hall_list:
    print(f"Hall No: {hall.hall_no}, Rows: {hall.rows}, Cols: {hall.cols}")