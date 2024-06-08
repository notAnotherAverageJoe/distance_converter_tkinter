from tkinter import *
from tkinter import messagebox, filedialog

def miles_to_km():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.609, 2)
        kilometer_result_label.config(text=f"{km}")
        log_conversion(f"{miles} miles = {km} km")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

def km_to_miles():
    try:
        km = float(km_input.get())
        miles = round(km / 1.609, 2)
        miles_result_label.config(text=f"{miles}")
        log_conversion(f"{km} km = {miles} miles")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

def clear():
    miles_input.delete(0, END)
    km_input.delete(0, END)
    kilometer_result_label.config(text="0")
    miles_result_label.config(text="0")
    history_listbox.delete(0, END)

def clear_miles():
    miles_input.delete(0, END)
    kilometer_result_label.config(text="0")

def clear_km():
    km_input.delete(0, END)
    miles_result_label.config(text="0")

def create_tooltip(widget, text):
    tooltip = Label(window, text=text, bg="yellow", font=("Arial", 10))
    tooltip.place_forget()

    def show_tooltip(event):
        tooltip.place(x=event.x_root, y=event.y_root)

    def hide_tooltip(event):
        tooltip.place_forget()

    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)

def log_conversion(conversion):
    history_listbox.insert(END, conversion)

def toggle_dark_mode():
    if dark_mode_var.get():
        window.config(bg="#333333")
        for widget in window.winfo_children():
            widget.config(bg="#333333", fg="white")
    else:
        window.config(bg=bg_color)
        for widget in window.winfo_children():
            widget.config(bg=bg_color, fg="black")

def validate_input(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False

def show_about():
    messagebox.showinfo("About", "Distance Converter\nVersion 1.0\n\nConvert distances between miles and kilometers.")

def save_history():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            for item in history_listbox.get(0, END):
                file.write(f"{item}\n")

def load_history():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            history_listbox.delete(0, END)
            for line in file:
                history_listbox.insert(END, line.strip())

window = Tk()
window.title("Distance Converter")
window.config(padx=25, pady=25, bg="#f0f0f0")

font_style = ("Arial", 18)
bg_color = "#f0f0f0"

# Menu Bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save History", command=save_history)
file_menu.add_command(label="Load History", command=load_history)
file_menu.add_command(label="Clear History", command=lambda: history_listbox.delete(0, END))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

# Input validation
validate_command = window.register(validate_input)

# Miles to Kilometers
miles_input = Entry(window, width=7, font=font_style, validate="key", validatecommand=(validate_command, '%P'))
miles_input.grid(column=1, row=0, padx=10, pady=10, sticky="ew")
create_tooltip(miles_input, "Enter distance in miles")

miles_label = Label(window, text="Miles", font=font_style, bg=bg_color)
miles_label.grid(column=2, row=0, padx=10, pady=10, sticky="w")

is_equal_label = Label(window, text="is equal to", font=font_style, bg=bg_color)
is_equal_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")

kilometer_result_label = Label(window, text="0", font=font_style, bg=bg_color)
kilometer_result_label.grid(column=1, row=1, padx=10, pady=10, sticky="ew")

kilometer_label = Label(window, text="Km", font=font_style, bg=bg_color)
kilometer_label.grid(column=2, row=1, padx=10, pady=10, sticky="w")

calculate_button = Button(window, text="Calculate", command=miles_to_km, font=font_style, bg="#007acc", fg="white")
calculate_button.grid(column=1, row=2, padx=10, pady=10, sticky="ew")
window.bind('<Return>', lambda event: miles_to_km())  # Enter key shortcut

clear_miles_button = Button(window, text="Clear Miles", command=clear_miles, font=("Arial", 12), bg="#d9534f", fg="white")
clear_miles_button.grid(column=3, row=0, padx=10, pady=10)

# Kilometers to Miles
km_input = Entry(window, width=7, font=font_style, validate="key", validatecommand=(validate_command, '%P'))
km_input.grid(column=1, row=3, padx=10, pady=10, sticky="ew")
create_tooltip(km_input, "Enter distance in kilometers")

km_label = Label(window, text="Km", font=font_style, bg=bg_color)
km_label.grid(column=2, row=3, padx=10, pady=10, sticky="w")

is_equal_label_km = Label(window, text="is equal to", font=font_style, bg=bg_color)
is_equal_label_km.grid(column=0, row=4, padx=10, pady=10, sticky="e")

miles_result_label = Label(window, text="0", font=font_style, bg=bg_color)
miles_result_label.grid(column=1, row=4, padx=10, pady=10, sticky="ew")

miles_label_result = Label(window, text="Miles", font=font_style, bg=bg_color)
miles_label_result.grid(column=2, row=4, padx=10, pady=10, sticky="w")

calculate_button_km = Button(window, text="Calculate", command=km_to_miles, font=font_style, bg="#007acc", fg="white")
calculate_button_km.grid(column=1, row=5, padx=10, pady=10, sticky="ew")
window.bind('<Shift-Return>', lambda event: km_to_miles())  # Shift+Enter key shortcut

clear_km_button = Button(window, text="Clear Km", command=clear_km, font=("Arial", 12), bg="#d9534f", fg="white")
clear_km_button.grid(column=3, row=3, padx=10, pady=10)

# Clear Button
clear_button = Button(window, text="Clear All", command=clear, font=font_style, bg="#d9534f", fg="white")
clear_button.grid(column=1, row=6, padx=10, pady=10, sticky="ew")

# Conversion History
history_label = Label(window, text="Conversion History", font=("Arial", 16), bg=bg_color)
history_label.grid(column=0, row=7, columnspan=4, pady=10)

history_listbox = Listbox(window, width=40, height=10, font=("Arial", 14))
history_listbox.grid(column=0, row=8, columnspan=4, padx=10, pady=10, sticky="ew")

# Dark Mode Toggle
dark_mode_var = BooleanVar()
dark_mode_checkbox = Checkbutton(window, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode, font=("Arial", 14), bg=bg_color)
dark_mode_checkbox.grid(column=0, row=9, columnspan=4, pady=10)

# Make the UI responsive
# Make the UI responsive
for i in range(10):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
window.mainloop()