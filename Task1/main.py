from page_factory import PageFactory
from popup_factory import PopupFactory

page = PageFactory.create_page("home")
page.display()

popup = PopupFactory.create_popup("alert")
popup.show()