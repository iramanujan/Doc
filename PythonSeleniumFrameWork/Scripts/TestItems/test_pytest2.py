import pytest


from Scripts.TestItems import Frames, Dropdowns, Checkboxes_Radio, Buttons, alert_popup

class Testclas():

    def test_frames(self):
        Frames.framesTest()

    # def test_dropdown(self):
    #     Dropdowns.dropdownt()
    #
    # def test_Checkboxes(self):
    #     Checkboxes_Radio.checkboxTest()
    #
    # def test_radio(self):
    #     Checkboxes_Radio.radio()
    #
    # def test_button(self):
    #     Buttons.buttons()
    #
    # def test_alerts(self):
    #     alert_popup.alerts()