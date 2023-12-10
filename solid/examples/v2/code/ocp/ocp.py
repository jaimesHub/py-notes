# class Printer:
#     """This class might have one responsibility
#     Printing data and generating output
#     """
#     def print_pdf(self, data: any):
#         pass

#     def print_web_document(self, data: any):
#         pass

#     def print_page(self, data: any):
#         pass

#     def verify_data(self, data: any):
#         pass

# what's problem with this class ?
    # If we need to print word or excel, we need to add a new method
    # but it actually is not closed for modification

# Refactoring code

from abc import ABC, abstractmethod

class PrinterImplementation:
    @abstractmethod
    def verify_data(self, data: any):
        pass

class WebPrinter(PrinterImplementation):
    def verify_data(self, data: any):
        print("Web printer implementation")

class PDFPrinter(PrinterImplementation):
    def verify_data(self, data: any):
        print("PDF printer implementation")

class PagePrinter(PrinterImplementation):
    def verify_data(self, data: any):
        print("Page printer implementation")