import tkinter as tk
from tkinter import ttk, messagebox
import re
import random
import string
import pyperclip

# -----------------------------
# Password Analysis
# -----------------------------
def analyze_password(event=None):

    password = password_entry.get()

    score = 0

    if len(password) >= 8:
        score += 20

    if len(password) >= 12:
        score += 10

    if re.search(r"[A-Z]", password):
        score += 20

    if re.search(r"[a-z]", password):
        score += 20

    if re.search(r"\d", password):
        score += 15

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15

    progress["value"] = score

    strength_label.config(
        text=f"Strength Score: {score}/100"
    )

    if score < 40:

        style.configure(
            "Custom.Horizontal.TProgressbar",
            background="red"
        )

        result_label.config(
            text="Weak Password ❌",
            fg="red"
        )

    elif score < 70:

        style.configure(
            "Custom.Horizontal.TProgressbar",
            background="orange"
        )

        result_label.config(
            text="Medium Password ⚠️",
            fg="orange"
        )

    elif score < 90:

        style.configure(
            "Custom.Horizontal.TProgressbar",
            background="green"
        )

        result_label.config(
            text="Strong Password ✅",
            fg="lightgreen"
        )

    else:

        style.configure(
            "Custom.Horizontal.TProgressbar",
            background="cyan"
        )

        result_label.config(
            text="Very Strong Password 🔥",
            fg="cyan"
        )

    # Password Statistics
    uppercase = len(re.findall(r"[A-Z]", password))
    lowercase = len(re.findall(r"[a-z]", password))
    numbers = len(re.findall(r"\d", password))
    special = len(re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password))

    stats_label.config(
        text=
        f"Length: {len(password)}\n"
        f"Uppercase: {uppercase}\n"
        f"Lowercase: {lowercase}\n"
        f"Numbers: {numbers}\n"
        f"Special Characters: {special}"
    )

    # Entropy Calculation
    entropy = round(len(password) * 4.7, 2)

    entropy_label.config(
        text=f"Entropy: {entropy} bits"
    )

    # Recommendations
    tips = []

    if len(password) < 12:
        tips.append("• Use at least 12 characters")

    if uppercase == 0:
        tips.append("• Add uppercase letters")

    if lowercase == 0:
        tips.append("• Add lowercase letters")

    if numbers == 0:
        tips.append("• Add numbers")

    if special == 0:
        tips.append("• Add special characters")

    if not tips:
        recommendation_label.config(
            text="Excellent password security! ✅"
        )
    else:
        recommendation_label.config(
            text="\n".join(tips)
        )
    common_passwords = [
        "password",
        "123456",
        "qwerty",
        "admin",
        "welcome",
        "password123"
    ]

    risk = "Low Risk ✅"
    risk_color = "lightgreen"

    if password.lower() in common_passwords:
        risk = "High Risk ❌"
        risk_color = "red"

    elif len(password) < 8:
        risk = "Medium Risk ⚠️"
        risk_color = "orange"

    elif password.isalpha():
        risk = "Medium Risk ⚠️"
        risk_color = "orange"

    elif password.isdigit():
        risk = "Medium Risk ⚠️"
        risk_color = "orange"

    risk_label.config(
        text=f"Risk Level: {risk}",
        fg=risk_color
    )

# -----------------------------
# Show / Hide Password
# -----------------------------
def toggle_password():

    if password_entry.cget("show") == "*":
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# -----------------------------
# Main Window
# -----------------------------
# -----------------------------
# Generate Password
# -----------------------------
def generate_password():

    chars = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(
        random.choice(chars)
        for _ in range(14)
    )

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    analyze_password()


# -----------------------------
# Copy Password
# -----------------------------
def copy_password():

    password = password_entry.get()

    if password:

        pyperclip.copy(password)

        messagebox.showinfo(
            "Copied",
            "Password copied successfully!"
        )


# -----------------------------
# Export Report
# -----------------------------
def export_report():

    password = password_entry.get()

    with open(
        "password_security_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write("PASSWORD SECURITY REPORT\n")
        file.write("========================\n\n")
        file.write(f"Password Length: {len(password)}\n")
        file.write(f"{strength_label.cget('text')}\n")
        file.write(f"{entropy_label.cget('text')}\n")
        file.write(f"{risk_label.cget('text')}\n")

    messagebox.showinfo(
        "Success",
        "TXT Report Saved Successfully!"
    )

    with open(
        "password_security_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "PASSWORD SECURITY REPORT\n"
        )

        file.write(
            "========================\n\n"
        )

        file.write(
            f"Password Length: {len(password)}\n"
        )

        file.write(
            f"{strength_label.cget('text')}\n"
        )

        file.write(
            f"{entropy_label.cget('text')}\n"
        )

        file.write(
            f"{risk_label.cget('text')}\n"
        )

    messagebox.showinfo(
        "Success",
        "TXT Report Saved Successfully!"
    )
root = tk.Tk()

root.title("Password Security Analyzer Pro")
root.geometry("1000x750")
root.resizable(False, False)
root.configure(bg="#0f172a")

# -----------------------------
# Progress Bar Style
# -----------------------------
style = ttk.Style()

style.theme_use("default")

style.configure(
    "Custom.Horizontal.TProgressbar",
    thickness=25
)

# -----------------------------
# Main Card
# -----------------------------
card = tk.Frame(
    root,
    bg="#1e293b"
)

card.pack(
    padx=30,
    pady=30,
    fill="both",
    expand=True
)

# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    card,
    text="🔐 Password Security Analyzer Pro",
    font=("Segoe UI", 24, "bold"),
    bg="#1e293b",
    fg="white"
)

title.pack(pady=(25, 10))

subtitle = tk.Label(
    card,
    text="Analyze password strength and security",
    font=("Segoe UI", 11),
    bg="#1e293b",
    fg="#94a3b8"
)

subtitle.pack()

# -----------------------------
# Password Input
# -----------------------------
password_label = tk.Label(
    card,
    text="Enter Password",
    font=("Segoe UI", 12, "bold"),
    bg="#1e293b",
    fg="white"
)

password_label.pack(pady=(30, 10))

password_entry = tk.Entry(
    card,
    width=35,
    font=("Segoe UI", 16),
    show="*",
    relief="flat"
)

password_entry.pack(ipady=8)

password_entry.bind(
    "<KeyRelease>",
    analyze_password
)

# -----------------------------
# Show/Hide Button
# -----------------------------
show_button = tk.Button(
    card,
    text="👁 Show / Hide Password",
    command=toggle_password,
    font=("Segoe UI", 10)
)

show_button.pack(pady=15)

# -----------------------------
# Strength Score
# -----------------------------
strength_label = tk.Label(
    card,
    text="Strength Score: 0/100",
    font=("Segoe UI", 14, "bold"),
    bg="#1e293b",
    fg="white"
)

strength_label.pack(pady=10)

# -----------------------------
# Progress Bar
# -----------------------------
progress = ttk.Progressbar(
    card,
    length=500,
    maximum=100,
    style="Custom.Horizontal.TProgressbar"
)

progress.pack(pady=10)

# -----------------------------
# Result Label
# -----------------------------
result_label = tk.Label(
    card,
    text="Waiting for password...",
    font=("Segoe UI", 12),
    bg="#1e293b",
    fg="#94a3b8"
)

result_label.pack(pady=10)
button_frame = tk.Frame(
    card,
    bg="#1e293b"
)

button_frame.pack(pady=15)

generate_btn = tk.Button(
    button_frame,
    text="🔑 Generate Password",
    command=generate_password,
    font=("Segoe UI", 10)
)

generate_btn.grid(
    row=0,
    column=0,
    padx=10
)

copy_btn = tk.Button(
    button_frame,
    text="📋 Copy Password",
    command=copy_password,
    font=("Segoe UI", 10)
)

copy_btn.grid(
    row=0,
    column=1,
    padx=10
)
report_btn = tk.Button(
    button_frame,
    text="📄 Export Report",
    command=export_report,
    font=("Segoe UI", 10)
)

report_btn.grid(
    row=0,
    column=2,
    padx=10
)
stats_title = tk.Label(
    card,
    text="📊 Password Statistics",
    font=("Segoe UI", 13, "bold"),
    bg="#1e293b",
    fg="white"
)

stats_title.pack(pady=(20, 10))

stats_label = tk.Label(
    card,
    text="Length: 0\nUppercase: 0\nLowercase: 0\nNumbers: 0\nSpecial Characters: 0",
    font=("Segoe UI", 11),
    bg="#1e293b",
    fg="#cbd5e1",
    justify="left"
)

stats_label.pack()
entropy_title = tk.Label(
    card,
    text="🧠 Password Entropy",
    font=("Segoe UI", 13, "bold"),
    bg="#1e293b",
    fg="white"
)

entropy_title.pack(pady=(20, 10))

entropy_label = tk.Label(
    card,
    text="Entropy: 0 bits",
    font=("Segoe UI", 11),
    bg="#1e293b",
    fg="#38bdf8"
)

entropy_label.pack()
recommendation_title = tk.Label(
    card,
    text="💡 Security Recommendations",
    font=("Segoe UI", 13, "bold"),
    bg="#1e293b",
    fg="white"
)

recommendation_title.pack(pady=(20, 10))

recommendation_label = tk.Label(
    card,
    text="Start typing a password...",
    font=("Segoe UI", 11),
    bg="#1e293b",
    fg="#facc15",
    justify="left"
)

recommendation_label.pack()
risk_title = tk.Label(
    card,
    text="⚠️ Password Risk Assessment",
    font=("Segoe UI", 13, "bold"),
    bg="#1e293b",
    fg="white"
)

risk_title.pack(pady=(20, 10))

risk_label = tk.Label(
    card,
    text="Risk Level: Unknown",
    font=("Segoe UI", 12, "bold"),
    bg="#1e293b",
    fg="yellow"
)

risk_label.pack()

# -----------------------------
# Footer
# -----------------------------
footer = tk.Label(
    card,
    text="Developed using Python & Tkinter",
    font=("Segoe UI", 10),
    bg="#1e293b",
    fg="#64748b"
)

footer.pack(side="bottom", pady=20)

root.mainloop()