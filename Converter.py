import tkinter as Tk
from tkinter import ttk
root = Tk.Tk()
root.title('Currency Converter')
root.geometry("420x700")
items = {'USD': {'TRY': [0.51], 'SEK': [10.25], 'JPY': [134.71], 'EUR': [0.91]},'TRY': {'USD': [1.96], 'SEK': [0.53], 'JPY': [7.14], 'EUR': [0.047]},'SEK': {'USD': [0.097], 'TRY': [1.88], 'JPY': [13.15], 'EUR': [0.088]},'JPY': {'USD': [0.0074], 'TRY': [0.14], 'SEK': [0.076], 'EUR': [0.0067]},'EUR': {'USD': [1.10], 'TRY': [21.32], 'SEK': [11.37], 'JPY': [149.42]}}
Vars = { 'Input': Tk.StringVar(), "Result": Tk.StringVar() }
LBs = { 'From': Tk.Listbox(root, exportselection=0), 'To': Tk.Listbox(root, exportselection=0) }
[(Tk.Label(root, text=(lbName + ':')).pack() if IsLabel else LBs[lbName].pack(fill='both', expand=True)) for lbName in list(LBs) for IsLabel in [True, False]]
[[lb.insert('end', item) for item in items] for lb in [LBs[x] for x in list(LBs)]]
[x.pack(fill='x', expand=True) for x in [ttk.Entry(root, textvariable=Vars[name]) for name in ["Input", "Result" ]]]
ttk.Button(root, text="Convert", style='Pink.TButton', command=lambda: Vars["Result"].set(f"Result: " + str(float(Vars["Input"].get()) * items [list(items) [LBs['From'].curselection() [0]]] [list(items) [LBs['To'].curselection() [0]]] [0]))).pack(fill='y', expand=False, pady=6)
ttk.Style().configure('TLabel', background='#ffb6c1')
ttk.Style().configure('Pink.TButton', background='#ff007f', foreground='white', font=('Arial Bold',16))
root.configure(bg='#ff69b4')
root.mainloop()
