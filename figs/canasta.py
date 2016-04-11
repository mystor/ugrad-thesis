def value(num, suit):
    if num <= 2:
        return 20
    elif 3 == num and suit in ['H', 'D']:
        return 100 # red 3s are worth 100
    elif 3 <= num < 8:
        return 5
    elif 8 <= num:
        return 10

def main():
    # Read in the type of card.
    numbers := ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
    num := input("Card Number (" + '/'.join(numbers) + "): ")
    if num not in numbers:
        print("Invalid card number!")
        return

    suits := ['H', 'D', 'C', 'S']
    suit := input("Card Suit (" + '/'.join(suits) + "): ")
    if suit not in suits:
        print("Invalid card suit!")
        return

    # Get the value of the card
    print("Value:", value(numbers.index(num) + 1, suit))

main()
