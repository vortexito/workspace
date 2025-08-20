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
from PIL import Image, ImageTk # Import Pillow library

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
        "Details": "The closest known exoplanet to our solar system, located in the habitable zone of its red dwarf star.",
        "Image": "Kepler_442b.png"
    },
    "Kepler-442 b": {
        "Discovery Date": "2015",
        "Mass": "2.35 Earths",
        "Radius": "1.34 Earths",
        "Orbital Period": "112 days",
        "Host Star": "Kepler-442",
        "Details": "Located in the habitable zone of a K-dwarf star, it is one of the most Earth-like planets discovered by the Kepler mission.",
        "Image": "Kepler_442b.png"
    },
    "Kepler-452 b": {
        "Discovery Date": "2015",
        "Mass": "Estimated ~5 Earths",
        "Radius": "1.6 Earths",
        "Orbital Period": "385 days",
        "Host Star": "Kepler-452",
        "Details": "Nicknamed 'Earth's cousin', it was one of the first near-Earth-sized planets found in the habitable zone of a Sun-like star.",
        "Image": "Kepler_452b.png"
    },
    "Kepler-186 f": {
        "Discovery Date": "2014",
        "Mass": "Unknown (likely similar to Earth, ~1.4 Earths estimated)",
        "Radius": "1.11 Earths",
        "Orbital Period": "129.9 days",
        "Host Star": "Kepler-186",
        "Details": "The first Earth-sized planet discovered in the habitable zone of its star. Located around 580 light-years away in the constellation Cygnus, it receives about one-third of the sunlight Earth does, suggesting a cooler environment where liquid water could exist if an atmosphere is present.",
        "Image": "Kepler_186f.png"
    },
    "Kepler-62 e": {
        "Discovery Date": "2013",
        "Mass": "Estimated ~4.5 Earths",
        "Radius": "1.61 Earths",
        "Orbital Period": "122.4 days",
        "Host Star": "Kepler-62",
        "Details": "A super-Earth located in the habitable zone of a K-type star, about 990 light-years away in the constellation Lyra. It is likely a rocky or ocean-covered planet, making it one of the most promising candidates for habitability found by the Kepler mission.",
        "Image": "Kepler_62e.png"
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

        self.title_font = tkfont.Font(family="Arial", size=24, weight="bold")
        self.header_font = tkfont.Font(family="Arial", size=18)
        self.button_font = tkfont.Font(family="Arial", size=14)
        self.label_font = tkfont.Font(family="Arial", size=12)
        self.label_font_bold = tkfont.Font(family="Arial", size=12, weight="bold")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, ExoplanetListPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def open_calc_page(self, calculation_name):
        self._open_page("CalculationPage", calc_name=calculation_name)

    def open_conversion_page(self):
        self._open_page("ConversionPage")

    def open_exoplanet_info_page(self, exoplanet_name):
        self._open_page("ExoplanetInfoPage", exoplanet_name=exoplanet_name)

    def _open_page(self, page_class_name, **kwargs):
        # A generic function to create and show a page
        if page_class_name in self.frames:
            self.frames[page_class_name].destroy()
        
        parent = self.winfo_children()[0]
        
        # This gets the class from its name (e.g., "CalculationPage" -> CalculationPage class)
        PageClass = globals()[page_class_name]
        
        frame = PageClass(parent=parent, controller=self, **kwargs)
        self.frames[page_class_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(page_class_name)

class BackgroundImageFrame(tk.Frame):
    def __init__(self, parent, controller, image_path):
        super().__init__(parent)
        self.controller = controller

        try:
            img = Image.open(image_path)
            img = img.resize((800, 600), Image.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(img)
            
            bg_label = tk.Label(self, image = self.bg_image)
            bg_label.place(x = 0, y = 0, relwidth =1, relheight =1)
        except FileNotFoundError:
            print(f"Warning: Background image not found at '{image_path}'")
        except Exception as e:
            print(f"Error loading background image: {e}")

class MainMenu(BackgroundImageFrame):
    def __init__(self, parent, controller):
        # Initialize the background image frame with the main background
        super().__init__(parent, controller, image_path="Background.png")

        label = tk.Label(self, text="Exoplanet Information Calculator", font=controller.title_font, bg='#333', fg='white')
        label.pack(side="top", fill="x", pady=20)

        label = tk.Label(self, text="Select an option:", font=controller.header_font, bg='#444', fg='white')
        label.pack(pady=10)
        
        conversion_button = tk.Button(self, text="Unit Conversions", font=controller.button_font, command=lambda: controller.open_conversion_page())
        conversion_button.pack(pady=10, ipady=10)

        button_frame = tk.Frame(self, bg=self.cget('bg'))
        button_frame.pack(pady=10)

        buttons = {"Excentricity": "excentricity", "Orbital Period": "orbitalPeriod", "Major Axis": "majorAxis", "Minor Axis": "minorAxis", "Perihelion": "perihelion", "Aphelion": "aphelion"}
        row, col = 0, 0
        for text, calc_name in buttons.items():
            button = tk.Button(button_frame, text=text, font=controller.button_font, width=15, command=lambda name=calc_name: controller.open_calc_page(name))
            button.grid(row=row, column=col, padx=10, pady=10, ipady=15, sticky="ew")
            col += 1
            if col > 1: col = 0; row += 1
        
        exoplanet_button = tk.Button(self, text="Potentially Habitable Exoplanets", font=controller.button_font, command=lambda: controller.show_frame("ExoplanetListPage"))
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
        
        for planet_name in EXOPLANET_DATA:
            button = tk.Button(buttons_frame, text=planet_name, font=controller.button_font, width=20, command=lambda name=planet_name: controller.open_exoplanet_info_page(name))
            button.pack(pady=7, ipady=5)

        back_button = tk.Button(self, text="Back to Menu", font=controller.button_font, command=lambda: controller.show_frame("MainMenu"))
        back_button.pack(pady=20)

class ExoplanetInfoPage(BackgroundImageFrame):
    def __init__(self, parent, controller, exoplanet_name):
        planet_info = EXOPLANET_DATA[exoplanet_name]
        image_file = planet_info.get("Image", "Default.png") # Use a default if no image is specified
        super().__init__(parent, controller, image_path=image_file)
        
        # A semi-transparent overlay to make text more readable
        overlay = tk.Frame(self, bg='black', highlightthickness=0)
        overlay.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.7)

        title = tk.Label(overlay, text=exoplanet_name, font=controller.title_font, fg="white", bg='black')
        title.pack(pady=20)

        info_frame = tk.Frame(overlay, bg='black')
        info_frame.pack(pady=10, padx=20)

        row_counter = 0
        for key, value in planet_info.items():
            if key == "Image": continue # Don't display the image filename
            key_label = tk.Label(info_frame, text=f"{key}:", font=controller.label_font_bold, fg="white", bg='black')
            key_label.grid(row=row_counter, column=0, sticky="ne", pady=5, padx=10)
            value_label = tk.Label(info_frame, text=value, font=controller.label_font, wraplength=450, justify="left", fg="white", bg='black')
            value_label.grid(row=row_counter, column=1, sticky="nw", pady=5, padx=10)
            row_counter += 1

        back_button = tk.Button(self, text="Back to Exoplanet List", font=controller.button_font, command=lambda: controller.show_frame("ExoplanetListPage"))
        back_button.pack(side="bottom", pady=20)

class ConversionPage(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self, text="Unit Conversions", font=self.controller.title_font); title.pack(pady=20)
        main_frame = tk.Frame(self); main_frame.pack(pady=20, padx=20)
        
        # Days to Seconds
        tk.Label(main_frame, text="Days:", font=self.controller.label_font).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.days_entry = tk.Entry(main_frame, font=self.controller.label_font, width=20); self.days_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Button(main_frame, text="Convert to Seconds", font=self.controller.button_font, command=self.convert_days).grid(row=0, column=2, padx=10, pady=10)
        self.days_result = tk.Label(main_frame, text="", font=self.controller.label_font, width=25); self.days_result.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        # Km to M
        tk.Label(main_frame, text="Kilometers (km):", font=self.controller.label_font).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.km_entry = tk.Entry(main_frame, font=self.controller.label_font, width=20); self.km_entry.grid(row=1, column=1, padx=10, pady=10)
        tk.Button(main_frame, text="Convert to Meters", font=self.controller.button_font, command=self.convert_km).grid(row=1, column=2, padx=10, pady=10)
        self.km_result = tk.Label(main_frame, text="", font=self.controller.label_font, width=25); self.km_result.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        # AU to M
        tk.Label(main_frame, text="Astronomical Units (AU):", font=self.controller.label_font).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.au_entry = tk.Entry(main_frame, font=self.controller.label_font, width=20); self.au_entry.grid(row=2, column=1, padx=10, pady=10)
        tk.Button(main_frame, text="Convert to Meters", font=self.controller.button_font, command=self.convert_au).grid(row=2, column=2, padx=10, pady=10)
        self.au_result = tk.Label(main_frame, text="", font=self.controller.label_font, width=25); self.au_result.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        tk.Button(self, text="Back to Menu", font=self.controller.button_font, command=lambda: self.controller.show_frame("MainMenu")).pack(pady=30)

    def convert_days(self): self._convert(self.days_entry, lambda v: v * 86400, self.days_result, "seconds")
    def convert_km(self): self._convert(self.km_entry, lambda v: v * 1000, self.km_result, "meters")
    def convert_au(self): self._convert(self.au_entry, lambda v: v * 1.496e+11, self.au_result, "meters", scientific=True)
    def _convert(self, entry, func, result_label, unit, scientific=False):
        try:
            val = float(entry.get())
            result = func(val)
            format_str = "{:.4e}" if scientific else "{:,.2f}"
            result_label.config(text=f"{format_str.format(result)} {unit}", fg="green")
        except ValueError:
            result_label.config(text="Invalid input", fg="red")

class CalculationPage(tk.Frame):
    def __init__(self, parent, controller, calc_name, **kwargs):
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
        title_text = ' '.join(word.capitalize() for word in self.calc_name.replace('e', 'e', 1).replace('O', ' O', 1).replace('M', ' M', 1).replace('P', ' P', 1).replace('A', ' A', 1).replace('Axis', ' Axis').split())
        tk.Label(self, text=f"Calculate {title_text}", font=self.controller.title_font).pack(pady=20)

        input_frame = tk.Frame(self); input_frame.pack(pady=20)
        for i, input_label in enumerate(calc_details["inputs"]):
            tk.Label(input_frame, text=input_label, font=self.controller.label_font).grid(row=i, column=0, padx=10, pady=10, sticky="w")
            entry = tk.Entry(input_frame, font=self.controller.label_font, width=30); entry.grid(row=i, column=1, padx=10, pady=10)
            self.entry_widgets[input_label] = entry

        self.result_label = tk.Label(self, text="", font=self.controller.label_font, fg="blue"); self.result_label.pack(pady=20)
        button_frame = tk.Frame(self); button_frame.pack(pady=20)
        tk.Button(button_frame, text="Calculate", font=self.controller.button_font, command=self.perform_calculation).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Back to Menu", font=self.controller.button_font, command=lambda: self.controller.show_frame("MainMenu")).grid(row=0, column=1, padx=10)

    def perform_calculation(self):
        try:
            calc_details = self.calc_requirements[self.calc_name]
            values = [float(self.entry_widgets[label].get()) for label in calc_details["inputs"]]
            result = calc_details["func"](*values)
            self.result_label.config(text=f"Result: {result:.4e}", fg="green")
        except ValueError as e:
            self.result_label.config(text=f"Error: {e}", fg="red")
        except Exception as e:
            self.result_label.config(text=f"An unexpected error occurred: {e}", fg="red")

if __name__ == "__main__":
    app = App()
    app.mainloop()