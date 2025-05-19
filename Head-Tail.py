import tkinter as tk
from tkinter import messagebox, filedialog
import random
import matplotlib.pyplot as plt
import csv
from scipy.stats import chisquare
from math import comb

# Core simulation logic
def biased_coin_flip(prob_tail=0.5):
    return 'T' if random.random() < prob_tail else 'H'

def simulate_all_probabilities(trials, number_of_flips, prob_tail):
    results = [0] * (number_of_flips + 1)
    for _ in range(trials):
        tails = sum(1 for _ in range(number_of_flips) if biased_coin_flip(prob_tail) == 'T')
        results[tails] += 1
    normalized = [count / trials for count in results]
    return normalized, results

def export_csv(probabilities):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Number of Tails", "Probability"])
            for i, p in enumerate(probabilities):
                writer.writerow([i, p])
        messagebox.showinfo("Export Successful", f"Data exported to:\n{file_path}")

def run_simulation():
    try:
        flips = int(entry_flips.get())
        desired_tails = int(entry_tails.get())
        bias = float(entry_bias.get())
        trials = 100000

        if not (0 <= desired_tails <= flips):
            raise ValueError("Tails must be between 0 and number of flips.")
        if not (0 <= bias <= 1):
            raise ValueError("Bias must be between 0 and 1.")

        # Simulations
        biased_probs, biased_counts = simulate_all_probabilities(trials, flips, bias)
        fair_probs, fair_counts = simulate_all_probabilities(trials, flips, 0.5)

        # Chi-square test
        expected = [comb(flips, k) * (bias**k) * ((1 - bias)**(flips - k)) * trials for k in range(flips + 1)]
        chi_stat, p_val = chisquare(biased_counts, f_exp=expected)

        # Result
        result_text = (
            f"Biased P({desired_tails} tails): {biased_probs[desired_tails]:.4f}   "
            f"Fair P({desired_tails} tails): {fair_probs[desired_tails]:.4f}\n"
            f"Chi-square p-value (bias vs theoretical): {p_val:.4f}"
        )
        label_result.config(text=result_text)

        # Plotting
        x = list(range(flips + 1))
        plt.figure(figsize=(10, 5))
        plt.plot(x, fair_probs, label="Fair Coin (p=0.5)", marker='o')
        plt.plot(x, biased_probs, label=f"Biased Coin (p={bias})", marker='o')
        plt.xlabel("Number of Tails")
        plt.ylabel("Estimated Probability")
        plt.title(f"Probability Distribution over {flips} Flips")
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

        # Enable export
        export_button.config(state='normal', command=lambda: export_csv(biased_probs))

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Biased vs Fair Coin Flip Simulator")

# Inputs
tk.Label(root, text="Number of Flips:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_flips = tk.Entry(root)
entry_flips.grid(row=0, column=1, padx=10, pady=5)
entry_flips.insert(0, "10")

tk.Label(root, text="Desired Tails:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_tails = tk.Entry(root)
entry_tails.grid(row=1, column=1, padx=10, pady=5)
entry_tails.insert(0, "5")

tk.Label(root, text="Bias (0.0 to 1.0):").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_bias = tk.Entry(root)
entry_bias.grid(row=2, column=1, padx=10, pady=5)
entry_bias.insert(0, "0.5")

# Buttons and output
tk.Button(root, text="Run Simulation", command=run_simulation).grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="", wraplength=400)
label_result.grid(row=4, column=0, columnspan=2, pady=5)

export_button = tk.Button(root, text="Export Biased CSV", state='disabled')
export_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
