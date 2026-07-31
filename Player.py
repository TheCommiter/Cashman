import time
class Player:
    def __init__(self, name: str, starting_amount: int, pin: str):
        self.name = name
        self.balance = starting_amount
        self.pin = pin
        self.locked = True
        self.lockdown = False

    def lockdown_timer(self):
        seconds = 120
        self.lockdown = True
        while seconds > 0:

            time.sleep(1)
            seconds -= 1
        self.lockdown = False
    def credit(self, amount): # NEVER CALL THIS DIRECTLY. USE transfer()
        if self.locked:
            print("Player " + self.name + " is locked!")
            return
        self.balance += amount
    def debit(self, amount): # NEVER CALL THIS DIRECTLY. USE transfer()
        if self.locked:
            print("Player " + self.name + " is locked!")
            return
        self.balance -= amount
    def transfer(self, amount, recipient: Player):
        self.unlock()
        if self.locked:
            return
        if amount > self.balance:
            raise ValueError("You cannot transfer more than you have!")
        self.debit(amount)
        recipient.credit(amount)
        print("Transfer successful!")
        self.lock()
    def unlock(self):
        if self.lockdown:
            return
        if not self.locked:
            print("Player " + self.name + " is unlocked!")
            return
        pin_attempt = input("Enter your pin to unlock: ")
        attempts = 0
        while pin_attempt != self.pin and attempts < 4:
            pin_attempt = input("Enter your pin to unlock: ")
            attempts += 1
        if pin_attempt != self.pin:
            self.lockdown_timer()
            return
        self.locked = False
    def lock(self):
        if self.locked:
            print("Player " + self.name + " is locked!")
            return
        self.locked = True
    def reset_pin(self, authority: Player):
        pin_attempt = input("Enter BANK pin to unlock: ")
        attempts = 0
        while pin_attempt != authority.pin and attempts < 4:
            pin_attempt = input("Enter BANK pin to unlock: ")
            attempts += 1
        if pin_attempt != authority.pin:
            self.lockdown_timer()
            return
        print("\033[H\033[2J", end="")
        pin = input("New PIN (4-Digit, Only Numbers): ")
        while len(pin) != 4 or pin.isdigit() != True:
            pin = input("Sorry, try again. PIN: ")
        self.pin = pin

    def __str__(self):
        return f"Player {self.name} has ${self.balance}"