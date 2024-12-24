from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup


# Encapsulation: Data Management Class
class DataManager:
    def __init__(self):
        self.users = {"admin": "admin123"}  # username: password
        self.games = [{"name": "Minecraft", "price": 20}]
        self.transactions = []

    def validate_user(self, username, password):
        return self.users.get(username) == password

    def add_game(self, name, price):
        self.games.append({"name": name, "price": price})

    def get_games(self):
        return self.games

    def add_transaction(self, username, items):
        self.transactions.append({"username": username, "items": items})


# Inheritance: Main Interface
class LoginScreen(BoxLayout):
    def __init__(self, app, manager, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.manager = manager
        self.orientation = 'vertical'

        # Login fields
        self.add_widget(Label(text="Username:"))
        self.username_input = TextInput(multiline=False)
        self.add_widget(self.username_input)

        self.add_widget(Label(text="Password:"))
        self.password_input = TextInput(password=True, multiline=False)
        self.add_widget(self.password_input)

        # Login button
        login_button = Button(text="Login")
        login_button.bind(on_press=self.validate_login)
        self.add_widget(login_button)

    def validate_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        if self.manager.validate_user(username, password):
            self.app.switch_to_dashboard(username)
        else:
            Popup(title="Login Failed",
                  content=Label(text="Invalid username or password"),
                  size_hint=(0.8, 0.4)).open()


# Polymorphism: Dashboard with Overriding for Games and Transactions
class Dashboard(BoxLayout):
    def __init__(self, app, username, manager, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.manager = manager
        self.username = username
        self.orientation = 'vertical'

        self.add_widget(Label(text=f"Welcome, {username}!"))

        # Buttons for navigating sections
        shop_button = Button(text="Shop")
        shop_button.bind(on_press=self.show_shop)
        self.add_widget(shop_button)

        games_button = Button(text="Manage Games")
        games_button.bind(on_press=self.manage_games)
        self.add_widget(games_button)

    def show_shop(self, instance):
        self.app.show_shop()

    def manage_games(self, instance):
        self.app.manage_games()


class ShopScreen(BoxLayout):
    def __init__(self, app, manager, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.manager = manager
        self.orientation = 'vertical'

        # Display available games
        self.add_widget(Label(text="Available Games:"))
        for game in self.manager.get_games():
            self.add_widget(Label(text=f"{game['name']} - ${game['price']}"))

        # Back button
        back_button = Button(text="Back")
        back_button.bind(on_press=lambda x: self.app.switch_to_dashboard())
        self.add_widget(back_button)


class ManageGamesScreen(BoxLayout):
    def __init__(self, app, manager, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.manager = manager
        self.orientation = 'vertical'

        # Add game fields
        self.add_widget(Label(text="Game Name:"))
        self.game_name_input = TextInput(multiline=False)
        self.add_widget(self.game_name_input)

        self.add_widget(Label(text="Game Price:"))
        self.game_price_input = TextInput(multiline=False)
        self.add_widget(self.game_price_input)

        # Add game button
        add_game_button = Button(text="Add Game")
        add_game_button.bind(on_press=self.add_game)
        self.add_widget(add_game_button)

        # Back button
        back_button = Button(text="Back")
        back_button.bind(on_press=lambda x: self.app.switch_to_dashboard())
        self.add_widget(back_button)

    def add_game(self, instance):
        name = self.game_name_input.text
        price = self.game_price_input.text
        if name and price.isdigit():
            self.manager.add_game(name, int(price))
            Popup(title="Success",
                  content=Label(text="Game added successfully!"),
                  size_hint=(0.8, 0.4)).open()
        else:
            Popup(title="Error",
                  content=Label(text="Invalid input"),
                  size_hint=(0.8, 0.4)).open()


class GamingApp(App):
    def build(self):
        self.manager = DataManager()
        self.screen = LoginScreen(self, self.manager)
        return self.screen

    def switch_to_dashboard(self, username=None):
        self.screen.clear_widgets()
        self.screen = Dashboard(self, username, self.manager)
        self.root.clear_widgets()
        self.root.add_widget(self.screen)

    def show_shop(self):
        self.screen.clear_widgets()
        self.screen = ShopScreen(self, self.manager)
        self.root.clear_widgets()
        self.root.add_widget(self.screen)

    def manage_games(self):
        self.screen.clear_widgets()
        self.screen = ManageGamesScreen(self, self.manager)
        self.root.clear_widgets()
        self.root.add_widget(self.screen)


if __name__ == "__main__":
    GamingApp().run()
