# bidder_available=input('Is bidder available there? Y/N').upper()
# while bidder_available=='Y':
#     name=input('enter the name; ')
#     bid_amount=int(input('enter the bid amount; '))
#     print(bid_amount)
# print('\n'*100)
#
#
# ask_bidder=input('Do you wanna bid? Y/N').lower()
# if ask_bidder=='Y':
#     name=input('enter the name; ')
#     bid_amount=int(input('enter the bid amount; '))
#     bidder_available=input('Is bidder available there? Y/N').lower()
#     while bidder_available=='Y':
#         name = input('enter the name; ')
#         bid_amount = int(input('enter the bid amount; '))
#


# def bidder_available():
#     name=input('enter the name; ')
#     bid_amount=int(input('enter the bid amount; '))
#     print(bid_amount)
#     print('\n'*100)
# # bidder_available()
# asK_bidder=input('Do you want to bid? Y/N').lower()
# while asK_bidder=='y':
#     bidder_available()
#     ask_again=input('Do wanna bid? Y/N')
#     while ask_again=='Y':
#         bidder_available()
#     while ask_again=='n':
#         print('highest bid')



#
# bid=input('Do you want to bid? Y/N').upper(
# bid_list=[]
# while bid=='Y':
#     # bid_list=[]
#     name=input('enter your name; ')
#     price=int(input('how much money you want to bid? '))
#     bid_list.append(price)
#     should_continue=input('enter do you want to continue the bid process; Y/N')
#     if should_continue=='N':
#         max_bid=max(bid_list)
#         print(max_bid)
#
#
# continue biding=True




# name=input('enter the name; ')
# price=int(input('how much do you want to bid; '))
# bid={}
# bid[name]=price
# should_continue=True
# bid = {}
# while should_continue:
#     name = input('enter the name; ')
#     price = int(input('how much do you want to bid; '))
#     bid[name] = price
#     continue_biding=input('Do you want to bid? y/n')
#     if continue_biding=='n':




# def compare_bid(bidding_list):
#     highest_bid=0
#     for i in bidding_list:
#         bid_amount=bidding_list[i]
#         if bid_amount>highest_bid:
#             highest_bid=bid_amount
#             winner=bidding_list
#     print()

# import art
# print(art.logo)
def find_highest_bidder(bidding_dictionaries):
    highest_bid=0
    for i in bidding_dictionaries:
        price=bidding_dictionaries[i]
        if price>highest_bid:
            highest_bid=bid_amount
        print(highest_bid)
bids={}
anyone_for_bidding=True
while anyone_for_bidding:
    name=input('enter the name; ')
    bid_amount=int(input('enter the bid amount; '))
    bids[name]=bid_amount
    continue_bidding=input('do you want to continue bid? Y/N; ')
    if continue_bidding=='N':
        anyone_for_bidding=False
        find_highest_bidder(bids)
    elif continue_bidding=='Y':
        anyone_for_bidding=True
        print('\n'*22)




# name=input('enter the name; ')
# bid_amount=int(input('enter the bid amount; '))






