import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from responses import responses  # You must have responses.py ready!

# Load employee dataset
csv_file = "C:\\Users\\Ayush Pandit\\Downloads\\employees_dataset.csv"
df = pd.read_csv(csv_file)

# Main functions
def resp(user_input):
    user_input = user_input.lower().strip()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

def emp_infor(empid, field):
    emp_data = df[df["empid"] == empid]
    
    if emp_data.empty:
        return "Employee ID not found. Please check and try again."
    
    if field in df.columns:
        return f"Your {field.replace('_', ' ')} is {emp_data.iloc[0][field]}."
    else:
        return "I couldn't find that information. Try asking about salary, leaves, or allowances."

def process_user_input(event=None):
    user_input = user_entry.get()
    if not user_input.strip():
        return

    chat_text.config(state='normal')
    chat_text.tag_configure('user', justify='right', foreground='#0b5ed7', font=("Arial", 12, "bold"))
    chat_text.insert(tk.END, f"You: {user_input}\n", 'user')

    if user_input.lower() == "bye":
        bot_message = responses.get("bye", "Goodbye!")
        chat_text.tag_configure('bot', justify='left', foreground='#28a745', font=("Arial", 12))
        chat_text.insert(tk.END, f"Bot: {bot_message}\n\n", 'bot')
        chat_text.config(state='disabled')
        user_entry.delete(0, tk.END)
        root.after(1000, root.destroy)  # Close after 1 second
        return

    # First try general response
    bot_message = resp(user_input)
    if bot_message != "I'm sorry, I didn't understand that. Can you please rephrase?":
        pass
    else:
        # Try employee specific fields
        if "salary" in user_input:
            bot_message = emp_infor(empid_global, "basic_salary")
        elif "grade pay" in user_input:
            bot_message = emp_infor(empid_global, "grade_pay")
        elif "da" in user_input or "dearness allowance" in user_input:
            bot_message = emp_infor(empid_global, "DA")
        elif "home rent" in user_input:
            bot_message = emp_infor(empid_global, "home_rent")
        elif "conveyance allowance" in user_input or "convience allowance" in user_input:
            bot_message = emp_infor(empid_global, "convience_allowance")
        elif "absent" in user_input:
            bot_message = emp_infor(empid_global, "absent")
        elif "earned leave" in user_input:
            bot_message = emp_infor(empid_global, "earned_leave")
        elif "casual leave" in user_input:
            bot_message = emp_infor(empid_global, "casual_leave")
        elif "maternity leave" in user_input:
            bot_message = emp_infor(empid_global, "maternity_leave")
        elif "washing allowance" in user_input:
            bot_message = emp_infor(empid_global, "washing_allowance")
        else:
            bot_message = "I'm not sure how to answer that. Try asking about salary, leaves, or HR policies."

    chat_text.tag_configure('bot', justify='left', foreground='#28a745', font=("Arial", 12))
    chat_text.insert(tk.END, f"Bot: {bot_message}\n\n", 'bot')

    chat_text.config(state='disabled')
    user_entry.delete(0, tk.END)
    user_entry.focus()
    chat_text.see(tk.END)

def ask_empid():
    global empid_global

    while True:
        empid_global = simpledialog.askstring("Employee ID", "Please enter your Employee ID:")

        if empid_global is None:
            if not messagebox.askyesno("Exit", "You must enter an Employee ID to use the chatbot.\nDo you want to exit?"):
                continue  # Ask again
            else:
                root.destroy()  # Exit the app
                return

        empid_global = empid_global.strip().upper()

        if empid_global not in df["empid"].values:
            messagebox.showerror("Invalid ID", "Invalid Employee ID. Please try again.")
        else:
            messagebox.showinfo("Success", f"Employee ID {empid_global} accepted successfully! 🎉")
            break


# ----------------------------------------------------
# Tkinter GUI starts here
import tkinter.simpledialog as simpledialog

root = tk.Tk()
root.title("HR Online Chatbot")
root.geometry("900x650")
root.configure(bg="#f0f2f5")

# Heading
heading = tk.Label(root, text="HR Helpdesk Online Chatbot", font=("Arial", 32, "bold"), fg="#333", bg="#f0f2f5")
heading.pack(pady=(20, 10))

# Horizontal line (Separator)
hr_line = ttk.Separator(root, orient='horizontal')
hr_line.pack(fill='x', padx=20, pady=10)

# Chat Frame
chat_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
chat_frame.pack(padx=20, pady=10, fill='both', expand=True)

# Chat area (Text Widget)
chat_text = tk.Text(chat_frame, height=20, width=100, state='disabled', wrap='word', bg="white", font=("Arial", 12), relief="flat")
chat_text.pack(padx=10, pady=10, fill='both', expand=True)

# Frame for user input and button
input_frame = tk.Frame(root, bg="#f0f2f5")
input_frame.pack(padx=20, pady=(5, 20), fill='x')

# Entry box for user input
user_entry = tk.Entry(input_frame, font=("Arial", 14), bg="white", relief="solid", bd=1)
user_entry.pack(side='left', fill='x', expand=True, padx=(0, 10), ipady=8)

# Submit button
submit_button = tk.Button(input_frame, text="Send ➤", font=("Arial", 14, "bold"), bg="#0b5ed7", fg="white", activebackground="#084298", activeforeground="white", command=process_user_input)
submit_button.pack(side='right', ipadx=10, ipady=5)

# Bind Enter key to submit
root.bind('<Return>', process_user_input)

# Focus cursor
user_entry.focus()

# Ask for Employee ID before proceeding
root.after(500, ask_empid)

# Run the application
root.mainloop()