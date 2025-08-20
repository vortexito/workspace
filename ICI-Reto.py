"""
A01647993 - Christian André Salgado Ledezma
A01648054 - Damaris Mariel Ramos Mariscal
A01649125 - Braulio Garcia Rayas
A01649444 - Carlos Hernandez Aceves
A01642633 - Bernardo González Maza
"""

import math
import tkinter as tk
from tkinter import font as tkfont
from tkinter import *

# Gravitational constant in m^3 kg^-1 s^-2
G = 6.67428e-11

# Modular dictionary for exoplanet data.
# You can add or remove exoplanets here.
EXOPLANET_DATA = {
    "Proxima Centauri b": {
        "Discovery Date": "2016",
        "Mass": "1.17 Earths",
        "Radius": "1.1 Earths",
        "Orbital Period": "11.2 days",
        "Host Star": "Proxima Centauri",
        "Details": "The closest known exoplanet to our solar system, located in the habitable zone of its red dwarf star."
    },
    "TRAPPIST-1e": {
        "Discovery Date": "2017",
        "Mass": "0.69 Earths",
        "Radius": "0.92 Earths",
        "Orbital Period": "6.1 days",
        "Host Star": "TRAPPIST-1",
        "Details": "Considered one of the most promising potentially habitable exoplanets due to its size, temperature, and the star it orbits."
    },
    "Kepler-452b": {
        "Discovery Date": "2015",
        "Mass": "Estimated ~5 Earths",
        "Radius": "1.6 Earths",
        "Orbital Period": "385 days",
        "Host Star": "Kepler-452",
        "Details": "Nicknamed 'Earth's cousin', it was one of the first near-Earth-sized planets found in the habitable zone of a Sun-like star."
    },
    "Gliese 667 Cc": {
        "Discovery Date": "2011",
        "Mass": "3.8 Earths",
        "Radius": "Estimated ~1.5 Earths",
        "Orbital Period": "28 days",
        "Host Star": "Gliese 667 C",
        "Details": "Orbits a red dwarf in a triple-star system and receives about 90% of the light that Earth does."
    }
}


def excentricityCalculator(majorAxis, minorAxis):
    if majorAxis <= 0 or minorAxis <= 0:
        raise ValueError("Axes must be positive.")
    if minorAxis > majorAxis:
        raise ValueError("Minor axis cannot be greater than major axis.")
    return math.sqrt(1 - (minorAxis**2 / majorAxis**2))

def orbitalPeriodCalculator(majorAxis, M):
    if majorAxis <= 0 or M <= 0:
        raise ValueError("Semi-major axis and mass must be positive")
    return 2 * math.pi * math.sqrt(majorAxis**3 / (G * M))

def majorAxisCalculator(perihelion, aphelion):
    if perihelion <= 0 or aphelion <= 0:
        raise ValueError("Perihelion and aphelion must be positive")
    if perihelion > aphelion:
        raise ValueError("Perihelion cannot be greater than aphelion")
    return (perihelion + aphelion) / 2

def minorAxisCalculator(majorAxis, excentricity):
    if majorAxis <= 0 or not (0 <= excentricity <1):
        raise ValueError("Invalid major axis or excentricity")
    return majorAxis * math.sqrt(1 - excentricity**2)

def perihelionCalculator(majorAxis, excentricity):
    if majorAxis <= 0 or not (0 <= excentricity <1):
        raise ValueError("Invalid major axis or excentricity")
    return majorAxis * (1 - excentricity)

def aphelionCalculator(majorAxis, excentricity):
    if majorAxis <= 0 or not (0 <= excentricity < 1):
        raise ValueError("Invalid major axis or excentricity")
    return majorAxis * (1 + excentricity)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Exoplanet Information Calculator")
        self.geometry("800x600")

        self.title_font = tkfont.Font(family = "Arial", size = 24, weight = "bold")
        self.header_font = tkfont.Font(family = "Arial", size = 18)
        self.button_font = tkfont.Font(family = "Arial", size = 14)
        self.label_font = tkfont.Font(family = "Arial", size = 12)

        container = tk.Frame(self, padx = 10, pady = 10)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (MainMenu, ExoplanetListPage):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def open_calc_page(self, calculation_name):
        if "CalculationPage" in self.frames:
            self.frames["CalculationPage"].destroy()

        parent = self.winfo_children()[0]
        frame = CalculationPage(parent = parent, controller = self, calc_name = calculation_name)
        self.frames["CalculationPage"] = frame
        frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame("CalculationPage")

    def open_conversion_page(self):
        if "ConversionPage" in self.frames:
            self.frames["ConversionPage"].destroy()

        parent = self.winfo_children()[0]
        frame = ConversionPage(parent=parent, controller=self)
        self.frames["ConversionPage"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("ConversionPage")

    def open_exoplanet_info_page(self, exoplanet_name):
        if "ExoplanetInfoPage" in self.frames:
            self.frames["ExoplanetInfoPage"].destroy()
        
        parent = self.winfo_children()[0]
        frame = ExoplanetInfoPage(parent=parent, controller=self, exoplanet_name=exoplanet_name)
        self.frames["ExoplanetInfoPage"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("ExoplanetInfoPage")


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text = "Exoplanet Information Calculator", font = controller.title_font)
        label.pack(side = "top", fill = "x", pady = 20)

        label = tk.Label(self, text = "Select an option:", font = controller.header_font)
        label.pack(pady = 10)
        
        conversion_button = tk.Button(
            self,
            text="Unit Conversions",
            font=controller.button_font,
            command=lambda: controller.open_conversion_page()
        )
        conversion_button.pack(pady=10, ipady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(pady = 10)

        buttons = {
            "Excentricity": "excentricity", "Orbital Period": "orbitalPeriod",
            "Major Axis": "majorAxis", "Minor Axis": "minorAxis",
            "Perihelion": "perihelion", "Aphelion": "aphelion"
        }

        row, col = 0, 0
        for text, calc_name in buttons.items():
            button = tk.Button(
                button_frame,
                text = text,
                font = controller.button_font,
                width = 15,
                command = lambda name = calc_name: controller.open_calc_page(name)
            )
            button.grid(row = row, column = col, padx = 10, pady = 10, ipady = 15, sticky = "ew")
            col += 1
            if col > 1:
                col = 0
                row += 1
        
        # Button to open the exoplanet information page
        exoplanet_button = tk.Button(
            self,
            text="Potentially Habitable Exoplanets",
            font=controller.button_font,
            command=lambda: controller.show_frame("ExoplanetListPage")
        )
        exoplanet_button.pack(pady=20, ipady=10)

class ExoplanetListPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        title = tk.Label(self, text="Potentially Habitable Exoplanets", font=controller.title_font)
        title.pack(pady=20)

        subtitle = tk.Label(self, text="Select an exoplanet to learn more", font=controller.header_font)
        subtitle.pack(pady=10)

        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=20)
        
        # Dynamically create buttons from the data dictionary
        for planet_name in EXOPLANET_DATA:
            button = tk.Button(
                buttons_frame,
                text=planet_name,
                font=controller.button_font,
                width=20,
                command=lambda name=planet_name: controller.open_exoplanet_info_page(name)
            )
            button.pack(pady=7, ipady=5)

        back_button = tk.Button(self, text="Back to Menu", font=controller.button_font, command=lambda: controller.show_frame("MainMenu"))
        back_button.pack(pady=20)

class ExoplanetInfoPage(tk.Frame):
    def __init__(self, parent, controller, exoplanet_name):
        super().__init__(parent)
        self.controller = controller
        
        planet_info = EXOPLANET_DATA[exoplanet_name]

        title = tk.Label(self, text=exoplanet_name, font=controller.title_font)
        title.pack(pady=20)

        info_frame = tk.Frame(self)
        info_frame.pack(pady=10, padx=20)

        # Display all information from the dictionary
        row_counter = 0
        for key, value in planet_info.items():
            key_label = tk.Label(info_frame, text=f"{key}:", font=controller.label_font, weight="bold")
            key_label.grid(row=row_counter, column=0, sticky="ne", pady=5, padx=10)
            
            value_label = tk.Label(info_frame, text=value, font=controller.label_font, wraplength=500, justify="left")
            value_label.grid(row=row_counter, column=1, sticky="nw", pady=5, padx=10)
            row_counter += 1

        back_button = tk.Button(self, text="Back to Exoplanet List", font=controller.button_font, command=lambda: controller.show_frame("ExoplanetListPage"))
        back_button.pack(pady=20)

class ConversionPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self, text="Unit Conversions", font=self.controller.title_font)
        title.pack(pady=20)

        main_frame = tk.Frame(self)
        main_frame.pack(pady=20, padx=20)

        # Days to Seconds
        days_label = tk.Label(main_frame, text="Days:", font=self.controller.label_font)
        days_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.days_entry = tk.Entry(main_frame, font=self.controller.label_font, width=20)
        self.days_entry.grid(row=0, column=1, padx=10, pady=10)
        days_button = tk.Button(main_frame, text="Convert to Seconds", font=self.controller.button_font, command=self.convert_days)
        days_button.grid(row=0, column=2, padx=10, pady=10)
        self.days_result = tk.Label(main_frame, text="", font=self.controller.label_font, width=25)
        self.days_result.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        # Km to M
        km_label = tk.Label(main_frame, text="Kilometers (km):", font=self.controller.label_font)
        km_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.km_entry = tk.Entry(main_frame, font=self.controller.label_font, width=20)
        self.km_entry.grid(row=1, column=1, padx=10, pady=10)
        km_button = tk.Button(main_frame, text="Convert to Meters", font=self.controller.button_font, command=self.convert_km)
        km_button.grid(row=1, column=2, padx=10, pady=10)
        self.km_result = tk.Label(main_frame, text="", font=self.controller.label_font, width=25)
        self.km_result.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        # AU to M
        au_label = tk.Label(main_frame, text="Astronomical Units (AU):", font=self.controller.label_font)
        au_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.au_entry = tk.Entry(main_frame, font=self.controller.label_font, width=20)
        self.au_entry.grid(row=2, column=1, padx=10, pady=10)
        au_button = tk.Button(main_frame, text="Convert to Meters", font=self.controller.button_font, command=self.convert_au)
        au_button.grid(row=2, column=2, padx=10, pady=10)
        self.au_result = tk.Label(main_frame, text="", font=self.controller.label_font, width=25)
        self.au_result.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        back_button = tk.Button(self, text="Back to Menu", font=self.controller.button_font, command=lambda: self.controller.show_frame("MainMenu"))
        back_button.pack(pady=30)

    def convert_days(self):
        try:
            days = float(self.days_entry.get())
            seconds = days * 24 * 60 * 60
            self.days_result.config(text=f"{seconds:,.2f} seconds", fg="green")
        except ValueError:
            self.days_result.config(text="Invalid input", fg="red")

    def convert_km(self):
        try:
            km = float(self.km_entry.get())
            meters = km * 1000
            self.km_result.config(text=f"{meters:,.2f} meters", fg="green")
        except ValueError:
            self.km_result.config(text="Invalid input", fg="red")

    def convert_au(self):
        try:
            au = float(self.au_entry.get())
            meters = au * 1.496e+11
            self.au_result.config(text=f"{meters:.4e} meters", fg="green")
        except ValueError:
            self.au_result.config(text="Invalid input", fg="red")


class CalculationPage(tk.Frame):
    def __init__(self, parent, controller, calc_name):
        super().__init__(parent)
        self.controller = controller
        self.calc_name = calc_name
        self.entry_widgets = {}

        self.calc_requirements = {
            "excentricity": {"inputs": ["Semi-major axis (m):", "Semi-minor axis (m):"], "func": excentricityCalculator},
            "orbitalPeriod": {"inputs": ["Semi-major axis (m):", "Mass of central body (kg):"], "func": orbitalPeriodCalculator},
            "majorAxis": {"inputs": ["Perihelion (m):", "Aphelion (m):"], "func": majorAxisCalculator},
            "minorAxis": {"inputs": ["Semi-major axis (m):", "Excentricity:"], "func": minorAxisCalculator},
            "perihelion": {"inputs": ["Semi-major axis (m):", "Excentricity:"], "func": perihelionCalculator},
            "aphelion": {"inputs": ["Semi-major axis (m):", "Excentricity:"], "func": aphelionCalculator}
        }

        self.create_widgets()

    def create_widgets(self):
        calc_details = self.calc_requirements[self.calc_name]

        title_text = self.calc_name.replace('e', 'e', 1).replace('O', ' O', 1).replace('M', ' M', 1).replace('P', ' P', 1).replace('A', ' A', 1)
        title_text = ' '.join(word.capitalize() for word in title_text.replace('Axis', ' Axis').split())
        title = tk.Label(self, text=f"Calculate {title_text}", font=self.controller.title_font)
        title.pack(pady=20)

        input_frame = tk.Frame(self)
        input_frame.pack(pady = 20)

        for i, input_label in enumerate(calc_details["inputs"]):
            label = tk.Label(input_frame, text = input_label, font = self.controller.label_font)
            label.grid(row = i, column = 0, padx = 10, pady = 10, sticky = "w")

            entry = tk.Entry(input_frame, font = self.controller.label_font, width = 30)
            entry.grid(row = i, column = 1, padx = 10, pady = 10)
            self.entry_widgets[input_label] = entry

        self.result_label = tk.Label(self, text = "", font = self.controller.label_font, fg = "blue")
        self.result_label.pack(pady = 20)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)

        calc_button = tk.Button(button_frame, text="Calculate", font=self.controller.button_font, command=self.perform_calculation)
        calc_button.grid(row=0, column=0, padx=10)

        back_button = tk.Button(button_frame, text="Back to Menu", font=self.controller.button_font, command=lambda: self.controller.show_frame("MainMenu"))
        back_button.grid(row=0, column=1, padx=10)

    def perform_calculation(self):
        try:
            calc_details = self.calc_requirements[self.calc_name]
            calculation_function = calc_details["func"]
            input_labels = calc_details["inputs"]

            values = [float(self.entry_widgets[label].get()) for label in input_labels]

            result = calculation_function(*values)

            self.result_label.config(text = f"Result: {result:.4e}", fg = "green")

        except ValueError as e:
            self.result_label.config(text=f"Error: {e}", fg="red")
        except Exception as e:
            self.result_label.config(text=f"An unexpected error occurred: {e}", fg="red")

if __name__ == "__main__":
    app = App()
    app.mainloop()