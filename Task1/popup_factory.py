from alert_popup import AlertPopup
from modal_popup import ModalPopup

class PopupFactory:

    @staticmethod
    def create_popup(popup_type):

        if popup_type == "alert":
            return AlertPopup()

        elif popup_type == "modal":
            return ModalPopup()