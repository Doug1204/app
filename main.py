import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty

import instaBot

username = ''
password = ''

class MainWindow(Screen):
    pass


class InstaWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def getInfo(self):
        global username, password
        if self.username.text and self.password.text:
            username = self.username.text
            password = self.password.text
            self.parent.current = 'InstaChoice'

class Insta_choiceWindow(Screen):
    pass

class SpamWindow(Screen):
    user = ObjectProperty(None)
    message = ObjectProperty(None)
    number = ObjectProperty(None)

    def send(self):
        global username, password
        if not self.number.text.isdigit():
            self.number.text = ''
            return None
        if self.user.text and self.message.text:
            x = instaBot.bot(username, password)
            x.spam(self.user.text, self.message.text, int(self.number.text))


class UnfollowerWindow(Screen):
    user = ObjectProperty(None)

    def check(self):
        global username, password
        if self.user.text:
            x = instaBot.bot(username, password)
            x.getUnfollow(self.user.text)
            self.manager.get_screen('viewUnfollow').view = '  '.join(x.unfollow)
            if username == self.user.text:
                self.parent.current = 'changeFolowing'
            else:
                self.parent.current = 'viewUnfollow'

class Change_followWindow(Screen):
    pass

class See_unfollowersWindow(Screen):
    view = StringProperty('None')

class Choice_tictactoeWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class Scroller(ScrollView):
    pass

class myGrid(GridLayout):
    pass


class CodeApp(App):
    def build(self):
        return WindowManager()


if __name__ == "__main__":
    main = CodeApp()
    main.run()