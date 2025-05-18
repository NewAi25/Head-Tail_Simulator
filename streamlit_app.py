import streamlit as st
import random
import matplotlib.pyplot as plt
import csv
from scipy.stats import chisquare
from math import comb
import io

def biased_coin_flip(prob_tail=0.5):
    return 'T' if random.random() < prob_tail else 'H'

def simulate_all_probabilities(trials, number_of_flips, prob_tail):
    results = [0] * (number_of_flips + 1)
    for _ in range(trials):
        tails_count = sum(1 for _ in range(number_of_flips) if biased_coin_flip(prob_tail) == 'T')
        results[tails_count] += 1
    return [count / trials for count in results], results

st.title("🪙 Coin Flip Simulator: Fair vs Biased")

flips = st.slider("Number of coin flips:", min_value=1, max_value=50, value=10)
tails = st.slider("Desired number of tails:", min_value=0, max_value=flips, value=5)
bias = st.slider("Bias (Probability of tails):", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
trials = 100000

if st.button("Run Simulation"):
    biased_probs, biased_counts = simulate_all_probabilities(trials, flips, bias)
    fair_probs, fair_counts = simulate_all_probabilities(trials, flips, 0.5)

    prob_desired = biased_probs[tails]
    st.write(f"**Estimated Probability** of exactly `{tails}` tails in `{flips}` flips (bias = `{bias}`): **{prob_desired:.4f}**")

    # Chi-square test
    expected = [comb(flips, k) * (bias ** k) * ((1 - bias) ** (flips - k)) * trials for k in range(flips + 1)]
    chi_stat, p_value = chisquare(f_obs=biased_counts, f_exp=expected)
    st.write(f"**Chi-square p-value**: `{p_value:.4f}` (lower = more biased)")

    # Line plot comparison
    fig, ax = plt.subplots(figsize=(10, 5))
    x = list(range(flips + 1))
    ax.plot(x, fair_probs, marker='o', label='Fair Coin (p=0.5)', color='blue')
    ax.plot(x, biased_probs, marker='o', label=f'Biased Coin (p={bias})', color='red')
    ax.set_xlabel("Number of Tails")
    ax.set_ylabel("Estimated Probability")
    ax.set_title(f"Tail Probability Distribution - {flips} Flips")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    st.pyplot(fig)

    # CSV download
    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(["Tails", "Biased Probability"])
    for i, p in enumerate(biased_probs):
        writer.writerow([i, p])
    st.download_button("📥 Download CSV", csv_buffer.getvalue(), file_name="biased_distribution.csv", mime='text/csv')
