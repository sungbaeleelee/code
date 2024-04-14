import tkinter as tk
from tkinter import messagebox

def calculate_metrics(companies):
    # Sort companies by share in descending order
    sorted_companies = sorted(companies, key=lambda x: x[1], reverse=True)
    hhi = sum(share**2 for name, share in sorted_companies)
    cr_4 = sum(share for name, share in sorted_companies[:min(4, len(companies))])
    cr_8 = sum(share for name, share in sorted_companies[:min(8, len(companies))])
    included_companies_4 = [name for name, share in sorted_companies[:min(4, len(companies))]]
    included_companies_8 = [name for name, share in sorted_companies[:min(8, len(companies))]]
    return hhi, cr_4, cr_8, included_companies_4, included_companies_8

def add_company():
    try:
        name = name_entry.get()
        share = float(share_entry.get())
        companies.append((name, share))
        name_entry.delete(0, tk.END)
        share_entry.delete(0, tk.END)
        companies_list_var.set(f"Companies: {', '.join(f'{n}: {s}%' for n, s in companies)}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid share number.")

def calculate():
    if companies:
        hhi, cr_4, cr_8, included_companies_4, included_companies_8 = calculate_metrics(companies)
        result_var.set(f"HHI: {hhi}\nCR_4: {cr_4} (Includes: {', '.join(included_companies_4)})\nCR_8: {cr_8} (Includes: {', '.join(included_companies_8)})")
    else:
        messagebox.showinfo("No companies", "Please enter some company shares first.")

companies = []

root = tk.Tk()
root.title("Market Concentration Analysis")

messagebox.showinfo("Instructions", "Enter company names and shares one at a time. Click 'Add Company' to add them to the list. Click 'Calculate' when you're done adding companies to calculate HHI, CR_4, and CR_8.")

instructions_label = tk.Label(root, text="Enter company name and share percentage, then press 'Add Company'. Press 'Calculate' after adding all companies.")
instructions_label.pack(pady=10)

name_entry = tk.Entry(root)
name_entry.pack()
name_entry.insert(0, "Company Name")

share_entry = tk.Entry(root)
share_entry.pack()
share_entry.insert(0, "Share %")

add_button = tk.Button(root, text="Add Company", command=add_company)
add_button.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

companies_list_var = tk.StringVar()
companies_label = tk.Label(root, textvariable=companies_list_var)
companies_label.pack()

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

root.mainloop()
