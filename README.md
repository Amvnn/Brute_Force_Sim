#  Brute Force Simulator

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A fun **brute-force password cracking simulator** written in Python. This project demonstrates how brute-force algorithms work by generating all possible character combinations until the correct secret is found.

---

##  Features
- Generate random passwords using letters, digits, and symbols
- Brute-force simulation with live progress updates
- **Interactive demo mode** with continuous cracking attempts
- Customizable password length and frequency of progress output
- Educational project to understand brute-force mechanics

---

##  Installation
```bash
# Clone the repo
git clone https://github.com/your-username/brute-force-sim.git
cd brute-force-sim

# Run with Python 3
python main_demo.py --help
```

---

##  Usage

### Run a single demo with a chosen secret
```bash
python main_demo.py --secret=abc --print-frequency=100
```

### Run continuous simulation (random secrets)
```bash
python main_demo.py --continuous
```

 Press `CTRL+C` anytime to stop the demo.

---

##  Demo Preview
<details>
<summary>📺 Click to expand simulation output</summary>

```
 Cracking secret: 'xk9'
Attempts: 000123 | 45.67% | 1200.45/sec | ETA: 00:02.12
Success! Secret 'xk9' cracked in 2.3 seconds with 2749 attempts

 Cracking secret: 'az3'
Attempts: 000842 | 77.90% | 1150.00/sec | ETA: 00:00.98
 Success! Secret 'az3' cracked in 1.4 seconds with 1080 attempts
```
</details>

---

##  Roadmap / TODO
- [x] Basic brute-force engine
- [x] Interactive continuous demo
- [ ] Add multiprocessing for faster cracking
- [ ] Add GitHub Action smoke test
- [ ] Create GIF preview for README

---

##  License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
