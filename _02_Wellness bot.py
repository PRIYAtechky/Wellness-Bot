import random

class WellnessChatbot:
    def __init__(self):
        self.greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
        self.menu_options = {
            "1": "Get stress management tips",
            "2": "Schedule reminders for self-care activities",
            "3": "Receive mental health support",
            "4": "Access resources for seeking help",
            "5": "Listen to calming music",
            "6": "Play mini-games",
            "7": "Take quizzes",
            "8": "Check weather forecast",
            "9": "Check Crypto forecast",
            "10": "Translate",
            "11": "Set reminders"
        }
        self.calming_music = ["Sound of Rain", "Classical Music", "Ocean Waves", "Birds Chirping"]
        self.mini_games = ["Guess the Number", "Word Scramble", "Tic Tac Toe"]
        self.quizzes = {"Math": ["What is 2 + 2?", "What is the square root of 16?"],
                        "Science": ["What is the chemical symbol for water?", "What is the powerhouse of the cell?"]}
        self.weather_forecast = {"Monday": "Sunny", "Tuesday": "Partly Cloudy", "Wednesday": "Rainy", "Thursday": "Clear"}
        self.crypto_forecast = {"Bitcoin": "$50,000", "Ethereum": "$3,000", "Dogecoin": "$0.20"}

    def greet_user(self):
        return random.choice(self.greetings)

    def display_menu(self):
        menu = "What can I assist you with today?\n"
        for option, description in self.menu_options.items():
            menu += f"{option}. {description}\n"
        menu += "Please enter the corresponding number:"
        return menu

    def handle_user_input(self, user_input):
        if user_input == "1":
            return self.get_stress_management_tips()
        elif user_input == "2":
            return self.schedule_reminders()
        elif user_input == "3":
            return self.get_mental_health_support()
        elif user_input == "4":
            return self.get_resources_for_help()
        elif user_input == "5":
            return self.listen_to_calming_music()
        elif user_input == "6":
            return self.play_mini_games()
        elif user_input == "7":
            return self.take_quizzes()
        elif user_input == "8":
            return self.check_weather_forecast()
        elif user_input == "9":
            return self.check_crypto_forecast()
        elif user_input == "10":
            return self.translate_text()
        elif user_input == "11":
            return self.set_reminders()
        else:
            return "Invalid option. Please choose a number from the menu."

    def get_stress_management_tips(self):
        tips = ["Practice deep breathing exercises.", "Take short breaks between study sessions.", "Stay physically active.", "Get enough sleep.", "Try mindfulness meditation."]
        return random.choice(tips)

    def schedule_reminders(self):
        return "Reminder feature coming soon!"

    def get_mental_health_support(self):
        return "Remember, it's okay to not be okay. Reach out to a trusted friend or professional for support."

    def get_resources_for_help(self):
        return "Here are some resources you can explore: [Resource 1], [Resource 2], [Resource 3]"

    def listen_to_calming_music(self):
        return f"Now playing: {random.choice(self.calming_music)}"

    def play_mini_games(self):
        return f"Let's play {random.choice(self.mini_games)}!"

    def take_quizzes(self):
        topic = random.choice(list(self.quizzes.keys()))
        question = random.choice(self.quizzes[topic])
        return f"Here's a {topic} quiz question: {question}"

    def check_weather_forecast(self):
        day = random.choice(list(self.weather_forecast.keys()))
        forecast = self.weather_forecast[day]
        return f"Weather forecast for {day}: {forecast}"

    def check_crypto_forecast(self):
        crypto = random.choice(list(self.crypto_forecast.keys()))
        value = self.crypto_forecast[crypto]
        return f"Forecast for {crypto}: {value}"

    def translate_text(self):
        return "Translation feature coming soon!"

    def set_reminders(self):
        return "Reminder setting feature coming soon!"

# Main function to interact with the chatbot
def main():
    chatbot = WellnessChatbot()
    print(chatbot.greet_user())
    while True:
        print(chatbot.display_menu())
        user_input = input().strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chatbot.handle_user_input(user_input)
        print(response)

if __name__ == "__main__":
    main()
