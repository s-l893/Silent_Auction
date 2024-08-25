status = ""
auction = {}
other_users = True
highest_bid = 0
winner = ""

print(r"""
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
""")
print ("Welcome to the silent bidding program.")

while other_users == True: 
    name = input("What is your name?\n")
    bid = int(input("What is your bid price?\n"))
    auction[name] = bid
    status = input("Are there any users who would like to bid? Type 'yes' to continue or 'no' to declare the winner of the auction\n").lower()
    if status == "yes":
        print ("\n" * 300)
    elif status == "no":
        for person in auction:
            if auction[person] > highest_bid:
                highest_bid = auction[person]
                winner = person
        other_users = False

print (f"The winner of the action is {winner} with a bid of {highest_bid}.")


