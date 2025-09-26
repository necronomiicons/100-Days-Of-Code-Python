#Silent Auction
print("Welcome to silent auction!")
other_bidder = "yes"
all_bidders = {}

while other_bidder == "yes":
    if len(all_bidders) > 0:
        print("\n" * 100)
    name = input("What is your name? \n")
    bid = input("What is your bid? \n$")
    all_bidders[name] = bid
    other_bidder = input("Are there any other bidders? \n")


highest_bidder = ""
for bidder in all_bidders:
    if(highest_bidder == ""):
        highest_bidder =  bidder
        continue
    if all_bidders[bidder] > all_bidders[highest_bidder]:
        highest_bidder = bidder

print(f"Highest bidder is {highest_bidder} with ${all_bidders[highest_bidder]}.")