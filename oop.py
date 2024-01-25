class parkingGarage():
    garage = 'welcome'

    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        self.spots_in_use = []

    ### This will decrease the amount of tickets available by 1
    ### This will decrease the amount of spots_in_use available by 1
    def takeTicket(self):
        ticket_prompt = input("Would you to see if there are any available parking spaces today? ")
        while True:
            if ticket_prompt == 'no':
                print("Have a great day!")
                break
            elif ticket_prompt == 'yes':
                if len(self.tickets) < 1:
                    print("There are no spots available at this time.")
                    break
                else:
                    print("There are", len(self.tickets)-1, "spaces available.")
                    give_ticket = input("Would you like to park for 1 hour? ($15) ")
                    if give_ticket == 'no':
                        break
                    elif give_ticket == 'yes':
                        for i in self.tickets:
                            print("This is your parking spot number: ", i)
                            self.spots_in_use.append(i)
                            self.tickets.remove(i)
                            break
                        print("Please select the payment option when you are ready to leave. Thank you! ")
                        break
        
    ### This will update the "current_ticket" dictionary key "paid" to True
    ### This will take money (5s and 10s) from user and tell them if amount entered isn't enough
    def payParking(self, ticket_num):
        self.ticket_num = ticket_num
        self.current_ticket = {'paid': False, 'balance': 20}
        for i in self.spots_in_use:
            if self.ticket_num not in self.spots_in_use:
                print("Sorry, that is an invalid ticket number. ")
            else:
                while self.current_ticket['paid'] == False:
                    # This next part is a self-note\example for int\input... I confuse myself often with the two
                    # Putting the input variable into a new variable containing int function:

                    pay_tkt_a = input("Please insert cash now: You will be charged $10 for one hour of parking. ")
                    pay_tkt = int(pay_tkt_a)
                    if pay_tkt == 5:
                        # compact for simplification
                        more_left = int(input("$5.00: Accepted. $5.00 remaining... "))
                        if more_left == 5:
                            print("Thank you! You have 15 minutes to exit the lot. Have a wonderful day!")
                            break
                        elif more_left == 10:
                            print("Dispensing change...\nYou have 15 minutes to exit the lot. Have a nice day!")
                            break
                    elif pay_tkt == 10:
                        self.current_ticket['paid'] = True
                        print("Thank you! You have 15 minutes to exit the lot. Have a wonderful day!")
                        break
                    else:
                        print("Sorry! That is not a five or ten dollar bill. Please try again. ")

    ### This updates the lists in __init__ if the current_ticket dict key 'paid' is True.
    def leaveGarage(self):
        if self.current_ticket['paid'] == True:
            for i in self.spots_in_use:
                self.tickets.append(i)
                self.spots_in_use.remove(i)
                break
            print(self.spots_in_use)

garage = parkingGarage()
garage.takeTicket()
garage.payParking(1)
garage.leaveGarage()