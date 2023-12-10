class ReportDocument:
    """This class violates the SRP"""
    def generate_report(self, data: any):
        pass

    def create_pdf(self, report: any):
        pass

class User:
    """This class doesn't violate the SRP"""
    def login(self, email: str, password: str):
        pass

    def signup(self, email: str, password: str):
        pass

    def assignRole(self, role: any):
        pass