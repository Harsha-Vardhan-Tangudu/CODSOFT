import tkinter as tk
from tkinter import messagebox
import requests

class MysticWeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("☀️ EnchantedWeather: The Mystical Weather Forecast ☔️")
        self.geometry("400x300")
        self.configure(bg="#0E121B")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Enter city name or zip code:", bg="#0E121B", fg="#C0D3D9", font=("Arial", 14, "bold"))
        self.label.pack(pady=20)

        self.input_entry = tk.Entry(self, font=("Arial", 12), bg="#1A2130", fg="#C0D3D9")
        self.input_entry.pack(padx=20, pady=5, fill=tk.BOTH, ipadx=10, ipady=5)

        get_weather_button = tk.Button(self, text="Get Weather", command=self.get_weather, bg="#346751", fg="white", font=("Arial", 12, "bold"))
        get_weather_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", bg="#0E121B", fg="#FFA33D", font=("Arial", 16, "bold"))
        self.result_label.pack(pady=20)

    def get_weather(self):
        try:
            location = self.input_entry.get()
            weather_data = self.retrieve_weather(location)

            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]
            description = weather_data["weather"][0]["description"]

            self.result_label.config(text=f"🌦️ Temperature: {temperature}°C\n💧 Humidity: {humidity}%\n💨 Wind Speed: {wind_speed} km/h\n🌄 Description: {description}")
        except KeyError:
            messagebox.showerror("Error", "Location not found. Please enter a valid city name or zip code.")

    def retrieve_weather(self, location):
        api_key = "YOUR_API_KEY"
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": location,
            "appid": api_key,
            "units": "metric"
        }
        response = requests.get(base_url, params=params)
        weather_data = response.json()
        return weather_data

if __name__ == "__main__":
    app = MysticWeatherApp()
    app.mainloop()
