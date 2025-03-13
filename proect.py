import tkinter as tk
from tkinter import messagebox

def record_transaction(buy_sell):
    try:
        amount = float(entry_amount.get())
        rate = float(entry_rate.get())

        if amount <= 0 or rate <= 0:
            raise ValueError("Значення повинні бути додатними).")

        transaction_type = "Купівля" if buy_sell == "buy" else "Продаж"
        total_uah = amount * rate if buy_sell == "buy" else amount / rate
        transaction_data = f"{transaction_type}: {amount:.2f} USD за {rate:.2f} грн/USD, Сума в грн: {total_uah:.2f}\n"

        with open("tranz.txt", "a") as f:
            f.write(transaction_data)

        messagebox.showinfo("Результат", f"Транзакція записана до файлу tranz.txt.")
        clear_entries()

    except ValueError as e:
        messagebox.showerror("Помилка", str(e))


def clear_entries():
    entry_amount.delete(0, tk.END)
    entry_rate.delete(0, tk.END)


root = tk.Tk()
root.title("Запис транзакцій")

label_amount = tk.Label(root, text="Кількість USD:")
entry_amount = tk.Entry(root)
label_rate = tk.Label(root, text="Курс (грн/USD):")
entry_rate = tk.Entry(root)
button_buy = tk.Button(root, text="Купити", command=lambda: record_transaction("buy"))
button_sell = tk.Button(root, text="Продати", command=lambda: record_transaction("sell"))

label_amount.grid(row=0, column=0, sticky="w")
entry_amount.grid(row=0, column=1, sticky="ew")
label_rate.grid(row=1, column=0, sticky="w")
entry_rate.grid(row=1, column=1, sticky="ew")
button_buy.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
button_sell.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

root.columnconfigure(1, weight=1)
root.mainloop()
