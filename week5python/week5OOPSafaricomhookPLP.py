
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage  
        self.battery_life = battery_life  
        self.__security_pin = None  
    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"Battery Life: {self.battery_life} hours")
    def set_security_pin(self, pin):
        if len(str(pin)) == 4:
            self.__security_pin = pin
            print("Security PIN set successfully!")
        else:
            print("PIN must be a 4-digit number!")

    def unlock_phone(self, pin):
        if pin == self.__security_pin:
            print("Phone unlocked successfully!")
        else:
            print("Invalid PIN. Try again.")
class SamsungSmartphone(Smartphone):
    def __init__(self, model, storage, battery_life, has_samsung_pay, supports_dex_mode):
        super().__init__("Samsung", model, storage, battery_life)
        self.has_samsung_pay = has_samsung_pay
        self.supports_dex_mode = supports_dex_mode
    def display_details(self):
        super().display_details()
        print(f"Samsung Pay: {'Available' if self.has_samsung_pay else 'Not Available'}")
        print(f"Dex Mode: {'Supported' if self.supports_dex_mode else 'Not Supported'}")
    def use_samsung_pay(self):
        if self.has_samsung_pay:
            print(f"Using Samsung Pay on {self.model}...")
        else:
            print(f"Samsung Pay is not available on {self.model}.")

    def enable_dex_mode(self):
        if self.supports_dex_mode:
            print(f"Enabling Dex Mode on {self.model}... Enjoy a desktop-like experience!")
        else:
            print(f"Dex Mode is not supported on {self.model}.")
if __name__ == "__main__":
    galaxy_s22 = SamsungSmartphone("Galaxy S22 Ultra", 256, 20, True, True)
    galaxy_s22.display_details()
    galaxy_s22.set_security_pin(5678)
    galaxy_s22.unlock_phone(5678)
    galaxy_s22.use_samsung_pay()
    galaxy_s22.enable_dex_mode()

    print("\n")
    
    galaxy_a13 = SamsungSmartphone("Galaxy A13", 128, 30, False, False)
    galaxy_a13.display_details()
    galaxy_a13.use_samsung_pay()
    galaxy_a13.enable_dex_mode()
