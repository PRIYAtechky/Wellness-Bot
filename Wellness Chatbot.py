import random
import time
import requests
import pygame

class WellnessCompanion:
    def _init_(self):
        pygame.init()
        pygame.mixer.init()
        self.positive_messages = ["You're doing great!", "You're amazing!", "You've got this!", "Stay positive!"]
        self.weather_api_key = "YOUR_WEATHER_API_KEY"
    
    def get_positive_message(self):
        return random.choice(self.positive_messages)
    
    def play_calming_music(self):
        pygame.mixer.music.load("calming_music.mp3")
        pygame.mixer.music.play(-1)  # Play indefinitely
        input("Press Enter to stop playing music...")
        pygame.mixer.music.stop()
    
    def get_weather_forecast(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
        else:
            return "Sorry, unable to fetch weather information."
    
    def start(self):
        print("Welcome to the Wellness Companion!")
        while True:
            print("\nWhat would you like to do?")
            print("1. Get a positive message")
            print("2. Listen to calming music")
            print("3. Check weather forecast")
            print("4. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                print("Your positive message:")
                print(self.get_positive_message())
            elif choice == "2":
                print("Playing calming music... (Press Enter to stop)")
                self.play_calming_music()
            elif choice == "3":
                city = input("Enter your city: ")
                print("Fetching weather forecast...")
                print(self.get_weather_forecast(city))
            elif choice == "4":
                print("Thank you for using the Wellness Companion. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Example usage
companion = WellnessCompanion()
companion.start()
