
import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "a9f8495ab86dc8ac487d2ad8330eab77"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 401:
            result.config(text="❌ Invalid API Key")
            return

        if response.status_code == 404:
            result.config(text="❌ City not found")
            return

        data = response.json()

        temp_c = data["main"]["temp"]
        temp_f = (temp_c * 9 / 5) + 32
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"].title()
        wind = data["wind"]["speed"]

        result.config(
            text=f"""
City : {city.title()}

Temperature : {temp_c:.1f} °C
Temperature : {temp_f:.1f} °F
Humidity    : {humidity} %
Condition   : {weather}
Wind Speed  : {wind} m/s
"""
        )

    except Exception as e:
        result.config(text=f"Error:\n{e}")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x350")

tk.Label(root, text="Enter City Name", font=("Arial", 14)).pack(pady=10)

city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 11), justify="left")
result.pack(pady=10)

root.mainloop()