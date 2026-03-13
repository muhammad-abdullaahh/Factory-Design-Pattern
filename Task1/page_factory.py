from homepage import HomePage
from contactpage import ContactPage
from aboutpage import AboutPage

class PageFactory:

    @staticmethod
    def create_page(page_type):

        if page_type == "home":
            return HomePage()

        elif page_type == "contact":
            return ContactPage()

        elif page_type == "about":
            return AboutPage()