class FXConverter:
    def convert(self, from_currency, to_currency, amount):
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2
    
class App:
    """App class uses FXConverter class
    Then App class is high-level module
    But App class heavily depends on FXConverter class which relies on FX's API
    In the future, if FX's API changes, it'll break the code
    Also, if you want to use a different API, you'll need to change the App class
    So we need to create an abstraction class (a layer) between FXConverter and App
    """
    def start(self):
        converter = FXConverter()
        converter.convert('EUR', 'USD', 100)

if __name__ == "__main__":
    app = App()
    app.start()