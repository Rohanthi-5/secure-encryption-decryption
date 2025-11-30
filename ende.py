import tkinter as tk
from tkinter import messagebox
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Encryption Function
def encrypt_message(message, c):
    """Encrypts a message with a random factor."""
    encrypted_message = f"{c:02}"
    random.seed(time.time())

    for char in message:
        x = ord(char)
        rand_factor = random.randint(1, 10)
        m = (x + c + rand_factor) % 25 + 5
        y = (m * x + c + rand_factor) % 1000

        encrypted_message += f"{m:02}{x:03}{y:03}{rand_factor:02}"

    return encrypted_message

# Decryption Function
def decrypt_message(encrypted_message, c):
    """Decrypts a message using the stored encryption format."""
    decrypted_message = ""
    i = 0

    original_c = int(encrypted_message[i:i+2])
    i += 2

    if c != original_c:
        raise ValueError("Decryption failed: Incorrect key.")

    while i < len(encrypted_message):
        m = int(encrypted_message[i:i+2])
        i += 2
        x = int(encrypted_message[i:i+3])
        i += 3
        y = int(encrypted_message[i:i+3])
        i += 3
        rand_factor = int(encrypted_message[i:i+2])
        i += 2

        # Validate decryption
        if (m * x + c + rand_factor) % 1000 != y:
            raise ValueError("Decryption mismatch: Data corruption or wrong key.")

        decrypted_message += chr(x)

    return decrypted_message

# Store encryption and decryption times & counts
encryption_times = []
decryption_times = []
encryption_count = 0
decryption_count = 0

# GUI Functions
def encrypt_action():
    global encryption_count
    message = entry_message.get("1.0", tk.END).strip()
    try:
        c = int(entry_c_encrypt.get())

        start_time = time.perf_counter()
        encrypted = encrypt_message(message, c)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        encryption_times.append(elapsed_time)

        encryption_count += 1  # Increment encryption count

        text_encrypted.delete(1.0, tk.END)
        text_encrypted.insert(tk.END, encrypted)
        update_encrypted_count()

        encryption_time_label_var.set(f"{elapsed_time:.6f} sec")
        encryption_count_var.set(f"{encryption_count}")
        update_graph()

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid key (integer).")

def decrypt_action():
    global decryption_count
    encrypted_input = text_encrypted.get(1.0, tk.END).strip()
    try:
        c = int(entry_c_decrypt.get())

        start_time = time.perf_counter()
        decrypted = decrypt_message(encrypted_input, c)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        decryption_times.append(elapsed_time)

        decryption_count += 1  # Increment decryption count

        text_decrypted.delete(1.0, tk.END)
        text_decrypted.insert(tk.END, decrypted)

        decryption_time_label_var.set(f"{elapsed_time:.6f} sec")
        decryption_count_var.set(f"{decryption_count}")
        update_graph()

    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")

def update_graph():
    """Updates encryption and decryption time graphs and calculates averages."""
    ax.clear()
    ax.plot(range(1, len(encryption_times) + 1), encryption_times, label="Encryption Time", marker="o")
    ax.plot(range(1, len(decryption_times) + 1), decryption_times, label="Decryption Time", marker="o")
    ax.set_xlabel("Run Number")
    ax.set_ylabel("Time (seconds)")
    ax.set_title("Encryption and Decryption Times")
    ax.legend()
    graph_canvas.draw()

    # Calculate and update averages
    avg_enc = sum(encryption_times) / len(encryption_times) if encryption_times else 0
    avg_dec = sum(decryption_times) / len(decryption_times) if decryption_times else 0

    average_encryption_time_var.set(f"{avg_enc:.6f} sec")
    average_decryption_time_var.set(f"{avg_dec:.6f} sec")

def update_message_count(event=None):
    count = len(entry_message.get("1.0", tk.END)) - 1
    message_count_var.set(f"{count}")

def update_encrypted_count(event=None):
    count = len(text_encrypted.get("1.0", tk.END)) - 1
    encrypted_count_var.set(f"{count}")

# GUI Setup
root = tk.Tk()
root.title("Ultra-Compact ASCII Encryption")
root.geometry("1000x600")

# Message Input
label_message = tk.Label(root, text="Message:")
label_message.grid(row=0, column=0, sticky="w")
entry_message = tk.Text(root, height=7, width=200)
entry_message.grid(row=0, column=1, columnspan=4)
entry_message.bind("<KeyRelease>", update_message_count)

label_message_count = tk.Label(root, text="Character Count:")
label_message_count.grid(row=0, column=5, sticky="w")

message_count_var = tk.StringVar(value="0")
label_message_value = tk.Label(root, textvariable=message_count_var)
label_message_value.grid(row=0, column=6, sticky="w")

# Encryption Key
label_c_encrypt = tk.Label(root, text="Encrypt Key (c):")
label_c_encrypt.grid(row=1, column=0, sticky="w")
entry_c_encrypt = tk.Entry(root, width=20)
entry_c_encrypt.grid(row=1, column=1)

# Encrypted Output
label_encrypted = tk.Label(root, text="Encrypted Message:")
label_encrypted.grid(row=2, column=0, sticky="w")
text_encrypted = tk.Text(root, height=7, width=200)
text_encrypted.grid(row=2, column=1, columnspan=4)
text_encrypted.bind("<KeyRelease>", update_encrypted_count)

label_encrypted_count = tk.Label(root, text="Encrypted Character Count:")
label_encrypted_count.grid(row=2, column=5, sticky="w")

encrypted_count_var = tk.StringVar(value="0")
label_encrypted_value = tk.Label(root, textvariable=encrypted_count_var)
label_encrypted_value.grid(row=2, column=6, sticky="w")

# Decryption Key
label_c_decrypt = tk.Label(root, text="Decrypt Key (c):")
label_c_decrypt.grid(row=3, column=0, sticky="w")
entry_c_decrypt = tk.Entry(root, width=20)
entry_c_decrypt.grid(row=3, column=1)

# Decrypted Output
label_decrypted = tk.Label(root, text="Decrypted Message:")
label_decrypted.grid(row=4, column=0, sticky="w")
text_decrypted = tk.Text(root, height=7, width=200)
text_decrypted.grid(row=4, column=1, columnspan=4)

# Buttons
button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_action)
button_encrypt.grid(row=5, column=0)

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_action)
button_decrypt.grid(row=5, column=1)

# Time Labels
tk.Label(root, text="Encryption Time:").grid(row=6, column=0, sticky="w")
encryption_time_label_var = tk.StringVar(value="0.000000 sec")
label_time = tk.Label(root, textvariable=encryption_time_label_var)
label_time.grid(row=6, column=1)

tk.Label(root, text="Decryption Time:").grid(row=7, column=0, sticky="w")
decryption_time_label_var = tk.StringVar(value="0.000000 sec")
label_decryption_time = tk.Label(root, textvariable=decryption_time_label_var)
label_decryption_time.grid(row=7, column=1)

# Average Time Labels
tk.Label(root, text="Avg Encryption Time:").grid(row=8, column=0, sticky="w")
average_encryption_time_var = tk.StringVar(value="0.000000 sec")
label_avg_encryption_time = tk.Label(root, textvariable=average_encryption_time_var)
label_avg_encryption_time.grid(row=8, column=1)

tk.Label(root, text="Avg Decryption Time:").grid(row=9, column=0, sticky="w")
average_decryption_time_var = tk.StringVar(value="0.000000 sec")
label_avg_decryption_time = tk.Label(root, textvariable=average_decryption_time_var)
label_avg_decryption_time.grid(row=9, column=1)

# Encryption & Decryption Count Labels
tk.Label(root, text="Encrypt Count:").grid(row=10, column=0, sticky="w")
encryption_count_var = tk.StringVar(value="0")
label_encryption_count = tk.Label(root, textvariable=encryption_count_var)
label_encryption_count.grid(row=10, column=1)

tk.Label(root, text="Decrypt Count:").grid(row=11, column=0, sticky="w")
decryption_count_var = tk.StringVar(value="0")
label_decryption_count = tk.Label(root, textvariable=decryption_count_var)
label_decryption_count.grid(row=11, column=1)

# Graph
fig, ax = plt.subplots(figsize=(6, 4))
graph_canvas = FigureCanvasTkAgg(fig, master=root)
graph_canvas.get_tk_widget().grid(row=12, column=0, columnspan=6)

root.mainloop()