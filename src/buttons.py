from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class AboutButton(Button):
    def __init__(self, **kwargs):
        super(AboutButton,self).__init__(**kwargs)
        self.text= 'Back to About'
        self.rgba= (37/255, 150/255, 190/255, 0.5)
        self.background_color= (37/255, 150/255, 190/255, 0.7)
        self.size_hint= (.3, .15)
        self.font_size= 40

    def on_release(self):
        self.parent.parent.parent.current = "about"