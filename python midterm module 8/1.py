class Star_Cinema: 
    hall_list= []

    def entry_hall(self,num):
        self.hall_list.append(num)

Hall = Star_Cinema()
Hall.entry_hall(1)
Hall.entry_hall(2)
Hall.entry_hall(3)
Hall.entry_hall(4)
print(Hall.hall_list)