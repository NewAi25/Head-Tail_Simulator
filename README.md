# 🧪 Head-Tail_Simulator_Biased_vs_Fair_Coin_Flip_Analysis

**Head-Tail Simulator** is a Python GUI application designed to simulate and visualize the statistical outcomes of flipping both fair and biased coins. It allows users to compare the distributions of outcomes, analyze the probability of getting a specific number of tails, perform a chi-square goodness-of-fit test, and export results — all from a user-friendly interface.
![image alt](https://github.com/NewAi25/Head-Tail_Simulator/blob/50cd3c3d02da1b879a2b614b29d4387deb4216ea/Capture2.PNG)
![image alt](https://github.com/NewAi25/Head-Tail_Simulator/blob/50cd3c3d02da1b879a2b614b29d4387deb4216ea/Capture.PNG)
![image alt](https://github.com/NewAi25/Head-Tail_Simulator/blob/50cd3c3d02da1b879a2b614b29d4387deb4216ea/fair%201.PNG)
![image alt](https://github.com/NewAi25/Head-Tail_Simulator/blob/50cd3c3d02da1b879a2b614b29d4387deb4216ea/fair.PNG)
---

## 🎯 Purpose

This project helps users:

- Understand how bias affects the outcome distribution of coin flips.
- Compare fair vs biased simulations visually and statistically.
- Practice probabilistic reasoning and statistical testing (chi-square).
- Learn simulation, plotting, and GUI design in Python.

---

## 📌 Features

✅ Simulate 100,000 coin flip trials for both **fair** and **biased** coins  
✅ Visualize empirical probability distributions side by side  
✅ Run chi-square test to check how closely results follow theoretical expectations  
✅ Export biased distribution data as a `.csv` file  
✅ Easy-to-use **Tkinter GUI** — no command line needed

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/NewAi25/Head-Tail_Simulator_Biased_vs_Fair_Coin_Flip_Analysis.git
cd Head-Tail_Simulator_Biased_vs_Fair_Coin_Flip_Analysis

2. Install Dependencies
Make sure Python 3.6+ is installed, then run:

bash
Copy
Edit
pip install matplotlib scipy
3. Run the Application
bash
Copy
Edit
python Head-tail.py
🖥️ Interface Overview
You’ll be asked to enter:

Number of Flips: How many times the coin is flipped per trial.

Desired Tails: How many tails you are specifically interested in observing.

Bias (0.0–1.0): The probability that the coin lands on tails (e.g. 0.7 means 70% chance of tails).

Click Run Simulation to see results and graphs. You can then optionally export the biased data.

📊 Example Scenario
You want to see how likely it is to get exactly 6 tails when flipping a biased coin 10 times with a 70% chance of tails.

Input:
Flips: 10

Desired Tails: 6

Bias: 0.7

Output:
Estimated Biased Probability: ~0.2003

Estimated Fair Probability: ~0.2051

Chi-square p-value: (example: 0.96 — suggests simulated results align with theory)

A graph will be displayed showing how the distribution shifts due to bias.

✅ Test Cases
Test #	Flips	Tails	Bias	Expected Behavior
1	10	5	0.5	Symmetric fair distribution (centered at 5)
2	10	0	0.0	Always heads → 100% chance of 0 tails
3	10	10	1.0	Always tails → 100% chance of 10 tails
4	10	7	0.8	High probability shifted toward more tails

📂 Exported Data Sample
CSV export includes:

csv
Copy
Edit
Number of Tails,Probability
0,0.0003
1,0.0011
...
10,0.1225
🔬 Behind the Scenes
Simulation: Runs 100,000 virtual trials for each setting.

Randomness: Uses Python's random to simulate biased flips.

Statistics: Uses SciPy's chisquare() test to compare observed vs expected frequencies.

Graphing: Uses matplotlib to display probability distributions.

💡 Future Improvements
Add input validation feedback inside GUI instead of popups

Allow saving charts as images

Integrate with Streamlit for web deployment

Add batch processing of multiple biases

📜 License
Distributed under the MIT License. See LICENSE for more information.

👤 Author
Developed by [Manisha]
📬 Feel free to connect on LinkedIn or contribute to the project!


