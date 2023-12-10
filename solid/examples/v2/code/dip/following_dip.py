from abc import ABC, abstractmethod

class CurrencyConverter(ABC):
    """Define an abstract class that acts as an interface"""
    def convert(self, from_currency, to_currency, amount) -> float:
        pass

class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using FX API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2
    
class App:
    """Now, App class depends on the CurrencyConverter interface, not the FXConverter class
    """
    def __init__(self, converter: CurrencyConverter) -> None:
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)

class AlphaConverter(CurrencyConverter):
    """In the future, you can support another currency coverter API
    For example, create AlphaConverter inherits from the  CurrencyConverter class
    """
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using Alpha API')
        print(f'{amount} {from_currency} = {amount * 1.15} {to_currency}')
        return amount * 1.15

if __name__ == "__main__":
    # converter = FXConverter()
    converter = AlphaConverter()
    app = App(converter)
    app.start()


