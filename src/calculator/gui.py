import tkinter as tk
from .operations import OPERATIONS

class CalculatorApp:
    def __init__(self, root=None):
        # 1. Main window
        self.root = root if root else tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("320x480")
        self.root.resizable(False, False)
        self._create_buttons()

        # 2. Calculator State
        self.first_num: float | int | None = None
        self.current_op: str | None = None
        self.reset_screen: bool = False

        # 3. Display Entry Widget
        self.display = tk.Entry(
            self.root,
            font=("Helvetica", 24),
            justify="right",
            bd=10,
            relief=tk.SUNKEN,
        )
        self.display.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=10,
            pady=15,
            ipady=8,
            sticky="nsew",
        )
        self.display.insert(0, "0")

    def set_display(self, val: str):
        self.display.delete(0, tk.END)
        self.display.insert(0, val)
        
    def on_click(self, char: str):
        current_text = self.display.get()

        # CASE 1: Clear
        if char == "C":
            self.first_num = None
            self.current_op = None
            self.reset_screen = False
            self.set_display("0")

        # CASE 2: Backspace ('DEL')
        elif char == "DEL":
            if current_text not in ("0", "Error") and len(current_text) > 1:
                self.set_display(current_text[:-1])
            else:
                self.set_display("0")

        # CASE 3: Digits and Decimal point
        elif char in "0123456789.":
            if self.reset_screen or current_text == "0":
                if char == ".":
                    self.set_display("0.")
                else:
                    self.set_display(char)
                self.reset_screen = False
            else:
                # Prevent multiple decimal points in one number
                if char == "." and "." in current_text:
                    return
                self.set_display(current_text + char)

        # CASE 4: Math Operators (+, -, *, /, %)
        elif char in OPERATIONS:
            try:
                self.first_num = (
                    float(current_text) if "." in current_text else int(current_text)
                )
            except ValueError:
                self.first_num = 0
            self.current_op = char
            self.reset_screen = True

        # CASE 5: Equals ('=')
        elif char == "=":
            if self.first_num is not None and self.current_op is not None:
                try:
                    num2 = (
                        float(current_text) if "." in current_text else int(current_text)
                    )
                    num1 = self.first_num
                    op_func = OPERATIONS[self.current_op]

                    result = op_func(num1, num2)

                    # Format result: whole numbers like 4.0 show as 4
                    if isinstance(result, float) and result.is_integer():
                        result = int(result)
                    self.set_display(str(result))
                    self.first_num = result
                    self.current_op = None
                    self.reset_screen = True
                except ZeroDivisionError:
                    self.set_display("Error")
                    self.first_num = None
                    self.current_op = None
                    self.reset_screen = True

    def _create_buttons(self):
        buttons = [
            ["C", "%", "DEL", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", None]
        ]

        for row_idx, row in enumerate(buttons, start=1):  # row 0 is the display
            for col_idx, text in enumerate(row):
                if text is None:
                    continue

                # "=" button spans 2 columns
                if text == "=":
                    btn = tk.Button(
                        self.root,
                        text=text,
                        font=("Helvetica", 16, "bold"),
                        bg="#4CAF50",
                        fg="black",
                        relief=tk.RAISED,
                        bd=3,
                        command=lambda t=text: self.on_click(t)
                    )
                    btn.grid(row=row_idx, column=col_idx, columnspan=2, padx=4, pady=4, sticky="nsew")
                else:
                    btn = tk.Button(
                        self.root,
                        text=text,
                        font=("Helvetica", 16),
                        relief=tk.RAISED,
                        bd=3,
                        command=lambda t=text: self.on_click(t)
                    )
                    btn.grid(row=row_idx, column=col_idx, padx=4, pady=4, sticky="nsew")

        # Make rows and columns stretch proportionally
        for i in range(4):
            self.root.columnconfigure(i, weight=1, uniform="col")
        for i in range(1, 6):
            self.root.rowconfigure(i, weight=1, uniform="row")

    def run(self):
        # Starts the Tkinter event loop.
        self.root.mainloop()

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()

