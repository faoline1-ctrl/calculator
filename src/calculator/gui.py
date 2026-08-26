import tkinter as tk
from .operations import OPERATIONS

def create_app():
    # 1. Create the main application window
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("320x480")   # width x height in pixels
    root.resizable(False, False) # prevent window resizing (optional)

    # State Variables
    state = {
        "first_num": None,
        "current_op": None, 
        "reset_screen": False
    }

    # 2. Create the display Entry widget
    display = tk.Entry(
        root,
        font=("Helvetica", 24),
        justify="right",              # Aligns numbers to the right like a real calculator
        bd=10,                        # Border wdith for a slight 3d effect
        relief=tk.SUNKEN              # Sunken border style
    )

    # 3. Position the display on the grid
    display.grid(
        row=0,
        column=0,
        columnspan=4,                # Spans across all 4 button columns
        padx=10,
        pady=15,
        ipady=8,                     # Internal vertical padding to make the screen taller
        sticky="nsew"                # Streches the entry to fill available space
    )

    # 4. Optional: Set default text
    display.insert(0, "0")

    # Helper function to update display text
    def set_display(val: str):
        display.delete(0, tk.END)
        display.insert(0, val)

    # Button Click Handler
    def on_click(char: str):
        current_text = display.get()

        # CASE 1: Clear
        if char == "C":
            state["first_num"] = None
            state["current_op"] = None
            state["reset_screen"] = False
            set_display("0")
        
        # CASE 2: Backspace ('DEL')
        elif char == "DEL":
            if current_text not in ("0", "Error") and len(current_text) > 1:
                set_display(current_text[:-1])
            else:
                set_display("0")

        # CASE 3: Digits an Decimal point
        elif char in "0123456789.":
            if state["reset_screen"] or current_text == "0":
                if char == ".":
                    set_display("0.")
                else:
                    set_display(char)
                state["reset_screen"] = False
            else:
                # Prevent multiple decimal points in one number
                if char == "." and "." in current_text:
                    return
                set_display(current_text + char)
        
        # CASE 4: Math Operators ( +, -, *, /, %)
        elif char in OPERATIONS:
            try:
                state["first_num"] = float(current_text) if "." in current_text else int(current_text)
            except ValueError:
                state["first_num"] = 0
            state["current_op"] = char
            state["reset_screen"] = True

        # CASE 5: Equals ('=')
        elif char == "=":
            if state["first_num"] is not None and state["current_op"] is not None:
                try:
                    num2 = float(current_text) if "." in current_text else int(current_text)
                    num1 = state["first_num"]
                    op_func = OPERATIONS[state["current_op"]]

                    result = op_func(num1, num2)

                    # Format result: if it's a whole number like 4.0 show as 4
                    if isinstance(result, float) and result.is_integer():
                        result = int(result)
                    set_display(str(result))
                    state["first_num"] = result
                    state["current_op"] = None
                    state["reset_screen"] = True
                except ZeroDivisionError:
                    set_display("Error")
                    state["first_num"] = None
                    state["current_op"] = None
                    state["reset_screen"] = True
                    

    # Button Matrix Definition
    buttons = [
        ["C", "%", "DEL", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", ".", "=", None]   # We'll handle '=' specially or let it span
    ]

    for row_idx, row in enumerate(buttons, start=1):  # start=1 because row 0 is the display
        for col_idx, text in enumerate(row):
            if text is None:
                continue

            # Special case: Make the "=" button wider (spanning 2 columns if at the bottom)
            if text == "=":
                btn = tk.Button(
                    root,
                    text=text,
                    font=("Helvetica", 16, "bold"),
                    bg="#4CAF50",
                    fg="black",
                    relief=tk.RAISED,
                    bd=3,
                    command=lambda t=text: on_click(t)
                )
                btn.grid(row=row_idx, column=col_idx, columnspan=2, padx=4, pady=4, sticky="nsew")
            else:
                btn = tk.Button(
                    root,
                    text=text,
                    font=("Helvetica", 16),
                    relief=tk.RAISED,
                    bd=3,
                    command=lambda t=text: on_click(t)
                )
                btn.grid(row=row_idx, column=col_idx, padx=4, pady=4, sticky="nsew")

    # Make all rows and columns strech proportionally
    for i in range(4):
        root.columnconfigure(i, weight=1, uniform="col")
    for i in range(1, 6):
        root.rowconfigure(i, weight=1, uniform="row")

    # 5. Start the event loop
    root.mainloop()

if __name__ == "__main__":
    create_app()




