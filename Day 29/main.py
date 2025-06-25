
import tkinter as tk
from tkinter import ttk, messagebox
from converter import fetch_conversion_rate, load_currency_list

def convert_currency():
    try:
        base = base_currency.get()
        target = target_currency.get()
        amount = float(amount_entry.get())

        rate = fetch_conversion_rate(base, target)
        converted = round(amount * rate, 2)
        result_label.config(text=f"{amount} {base} = {converted} {target}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
    except RuntimeError as e:
        messagebox.showerror("Error", str(e))

# --- GUI Setup ---
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x280")
root.configure(bg="#1e1e1e")  # Dark background

# Dark theme styling
style = ttk.Style()
style.theme_use("default")
style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 12))
style.configure("TEntry", fieldbackground="#2e2e2e", foreground="white")
style.configure("TCombobox", fieldbackground="#2e2e2e", background="#2e2e2e", foreground="white")
style.configure("TButton", background="#3c3c3c", foreground="white")

currency_options = load_currency_list()

# Base currency
ttk.Label(root, text="Base Currency").pack(pady=(10, 0))
base_currency = ttk.Combobox(root, values=currency_options)
base_currency.pack()
base_currency.set("USD")

# Target currency
ttk.Label(root, text="Target Currency").pack(pady=(10, 0))
target_currency = ttk.Combobox(root, values=currency_options)
target_currency.pack()
target_currency.set("INR")

# Amount entry
ttk.Label(root, text="Amount").pack(pady=(10, 0))
amount_entry = ttk.Entry(root)
amount_entry.pack()

# Convert button
ttk.Button(root, text="Convert", command=convert_currency).pack(pady=12)

# Result display
result_label = ttk.Label(root, text="", font=("Segoe UI", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()