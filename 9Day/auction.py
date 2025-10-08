import art

auctioners = {}
winner = ""

print(art.auction_hammer)

def add_bid():
    new_auc = input("What is your name? ")
    new_bid = int(input("What is your bid? $"))
    auctioners[new_auc] = new_bid

def winner_is(dictionary):
    tmp:int = 0
    res:str = ""
    for auc in dictionary:
        if dictionary[auc] > tmp:
            res = auc
            tmp = dictionary[auc]
    print(f"The winner is: {res}")

add_bid()

while 1:
    bid_counter = input("Are there any other bidders? Type 'yes' or 'no'\n")
    match bid_counter:
        case 'yes':
            add_bid()
        case 'no':
            winner_is(auctioners)
            break
        case _:
            bid_counter = input("Invalid answer, try again. Type 'yes' or 'no'\n")


