import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input1 = tk.Entry(self)
        self.input1.pack(side="left")
        self.input2 = tk.Entry(self)
        self.input2.pack(side="left")
        self.input3 = tk.Entry(self)
        self.input3.pack(side="left")

        self.calculate_button = tk.Button(self)
        self.calculate_button["text"] = "Hesapla"
        self.calculate_button["command"] = self.calculate
        self.calculate_button.pack(side="left")

        self.result_label = tk.Label(self)
        self.result_label.pack(side="left")

    def calculate(self):
        try:
            num1 = float(self.input1.get())
            num2 = float(self.input2.get())
            num3 = float(self.input3.get())
            result = num1 + num2 + num3
            self.result_label["text"] = f"Toplam: {result}"
        except ValueError:
            self.result_label["text"] = "Geçersiz giriş!"

root = tk.Tk()
app = Application(master=root)
app.mainloop()
