class Star_Cinema:
    hall_list = []

    def __init__(self):
        pass

    def entry_hall(self, hall):
        self.hall_list.append(hall)
    
    def __repr__(self):
        for hall in self.hall_list:
            print(f'Hall No: {hall.hall_no}')
            print(f'Rows: {hall._rows}, Columns: {hall._cols}')
        
            print(f'\nAvailable shows are below')
            for show in hall._show_list:
                print(f'Show ID: {show[0]}, Name: {show[1]}, Time: {show[2]}')
            
            print('\nAvailable seats are')
            for show_id, seat_arrangement in hall._seats.items():
                print(f'Available seats for show ID: {show_id}')
                for row in seat_arrangement:
                    print(" ".join(map(str, row)))
                print()
            
            print()
        return f'------------ Hello, Welcome --------------'
    


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        super().__init__()
        self.entry_hall(self)
    
   # nutun movie entry
    def entry_show(self, id, movie_name, time):
        for show in self._show_list:
            if show[0] == id:
                print(f'Show ID {id} Already Exists')
                return
        
        show = (id, movie_name, time)
        self._show_list.append(show)

        seat = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                row.append(0)
            seat.append(row)
        self._seats[id] = seat


    # cinema er tickit katbo
    def book_seats(self, id, booking):
        if id in self._seats:
            for book in booking:
                row = int(book[0])
                col = int(book[1])

                if (row < 0 or (self._rows <= row) or (col < 0) or (self._cols <= col)):
                    print(f'\nInvalid seat position ({row}, {col}). Please try again')
                    continue

                if self._seats[id][row][col] == 0:
                    self._seats[id][row][col] = 1
                    print(f'\nSeat ({row}, {col}) is booked for for show {id}')
                else:
                    print(f'\nSeat ({row}, {col}) is alreay booked for the show id {id}. Please try again.')
        else:
            print(f'\nInvalid show id: {id}. Please try agian.')
    

    # ki ki movie currently cinema hall a cholce
    def view_show_list(self):
        if len(self._show_list) != 0:
            print('-----------------------------------------------')
            for show in self._show_list:
                print(f'Movie Name:  {show[1]}')
                print(f'Show ID:  {show[0]}')
                print(f'Time:  {show[2]}')
                print()
            print('-----------------------------------------------')
        else:
            print(f'No movies are available today.')
    


    # kon kon seat available ache 
    def view_available_seats(self, id):
        if len(self._show_list) == 0:
            print('\nSorry! No shows are available today.')
            return
        
        if id in self._seats:
            print(f'\nAvailable seats for show {id} :')
            for i in range(len(self._seats[id])):
                for j in range(len(self._seats[id])):
                    print(f'Seat({i}, {j})')
            print(f'Updated seat matrix for hall {self._hall_no}:')
            for row in self._seats[id]:
                for element in row:
                    print(element, end = " ")
                print()
        else:
            print(f'\nSorry! Invalid Show Id: {id}. Please try again')

    # representation 
    def __repr__(self) -> str:
        print(f'\nAvailable shows are down below')
        for show in self._show_list:
            print(f'Show ID: {show[0]}, Name: {show[1]}, Time: {show[2]}')
        print(f'Available seats are down below')

        for show_id, seat_arrangement in self._seats.items():
            print(f'Available seats for show ID: {show_id}')
            for row in seat_arrangement:
                print(" ".join(map(str, row)))
            print()
        return f'--------------- Hello, Welcome --------------\n'

hall_1 = Hall(7, 7, 1)    
hall_1.entry_show("101", "Air", "11 December, 2024  2:00 PM")
hall_1.entry_show("102", "Swimmer", "12 December, 2024  3:00 PM")

while True:
    print(f'1. Veiw all show today')
    print(f'2. Veiw available seats')
    print(f'3. Book ticket')
    print(f'4. Exit')

    ch = int(input('Enter Option: '))
    if ch == 1:
        hall_1.view_show_list()
    elif ch == 2:
        id = input('Enter show Id: ')
        hall_1.view_available_seats(id)
    elif ch == 3: 
        id = input('Show ID: ')
        seats = int(input('Number of tickets: '))
        if seats == 0:
            print(f'\nInvalid seats {seats}. Please try again')
            continue
        
        bookings = []
        while seats != 0:
            row = input('Enter seat row: ')
            col = input('Enter seat col: ')
            bookings.append((row, col))
            seats -= 1
        
        hall_1.book_seats(id, bookings)
    elif ch == 4:
        break
    else:
        print(f'\nInvalid options. Please select between 1, 2, 3 or 4')

        



    