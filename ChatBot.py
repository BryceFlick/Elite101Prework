import time
import sys

class Chatbot:

    def __init__(self, name, age, money=0, socks=0, shirt=0, pants=0, hat=0):
        self.name = name
        self.age = age
        self.money = money
        self.socks = socks
        self.shirt = shirt
        self.pants = pants
        self.hat = hat

        # Store prices
        self.prices = {
            "hat": 12.0,
            "shirt": 18.0,
            "socks": 2.0,
            "pants": 21.0
        }

    # Welcome Function
    def welcome(self):
        time.sleep(0.3)
        print(f"\nWelcome {self.name}!")
        time.sleep(0.25)
        print(f"Let's look at some cool styles for {self.age}-year-olds.")

    # Store menu
    def store_Menu(self):
        time.sleep(0.25)
        while True:
            try:
                navigate = int(input(
                    "\nHi, how can I help you navigate through the store?\n"
                    "1. Check what we got!\n"
                    "2. Go to your cart\n"
                    "3. Add more money to your account\n"
                    "4. Leave the site\n"
                ))

                if navigate == 1:
                    print("What we are selling:")
                    for item, price in self.prices.items():
                        print(f"{item.capitalize()}: ${price:.2f}")

                elif navigate == 2:
                    self.GoToCart()

                elif navigate == 3:
                    self.Add_money()

                elif navigate == 4:
                    self.exit()

                else:
                    print("Invalid option. Try again.")
            
            except ValueError:
                print("Please enter a valid option.")

    # Add more money to buy
    def Add_money(self):
        while True:
            time.sleep(0.25)
            try:
                amount = float(input("How much money do you want to add? $"))
                self.money += amount
                print(f"You now have ${self.money:.2f} in your account.")
                break
            except (ValueError, TypeError):
                print("Please enter a valid number.")

    # check money
    def check_money(self):
        time.sleep(0.25)
        print(f"You have ${self.money:.2f} in your account.")

    # exit
    def exit(self):
        time.sleep(1)
        print(f"Bye! See you soon {self.name}")
        sys.exit()

    # Buying system
    def GoToCart(self):
        self.check_money()
        print("What do you want to buy? (hat/shirt/socks/pants)")
        item = input("Enter item name: ").lower()

        if item not in self.prices:
            print("Sorry, we don’t sell that item.")
            return

        try:
            quantity = int(input("How many do you want to buy? "))
        except (ValueError, TypeError):
            print("Please enter an integer for the quantity.")
            return

        cost = self.prices[item] * quantity

        if cost <= self.money:
            self.money -= cost
            setattr(self, item, getattr(self, item) + quantity)
            print(f"Your card was accepted...You bought {quantity} {item}(s) for ${cost:.2f}.")
            self.check_money()
        else:
            print("Your card declined...please add more money to your account.")


def main():
    name = input("What is your name? ")
    time.sleep(.5)
        
    while True:
        try:
            age = int(input("How old are you? "))
            break
        except (ValueError, TypeError):
            print("Please enter an integer for age.")

    store = Chatbot(name, age)
    store.welcome()
    store.store_Menu()


if __name__ == "__main__":
    main()
