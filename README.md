# 🚗 Usage-Based Insurance System

## 📘 Project Overview

This project implements a modular **usage-based insurance (UBI)** system that simulates how insurance providers can adjust premiums based on driver behavior data. Using synthetic telematics data — such as speed, braking, acceleration, time of day, and road type — the system analyzes behavior, computes risk, adjusts premiums accordingly, and offers actionable safety feedback to the driver.

The goal is to encourage safer driving and fairer insurance pricing using data-driven insights.

---

## 🔧 Development Workflow

### ✅ 1. Created GitHub Repository
A dedicated GitHub repository was initialized to manage the source code with version control and enable future collaboration.

### 💻 2. Developed Locally in VS Code
Development was carried out in **Visual Studio Code** using modular Python scripts. The project follows best practices by separating logic into clear modules:
- data handling
- behavior analysis
- scoring and pricing
- feedback generation

### 🚀 3. Pushed Code to GitHub
After local development and testing, Git was used to commit and push all modules to GitHub. This setup enables collaborative development and remote backup of code.

---

## 📂 Code Structure and Modules

| File | Description |
|------|-------------|
| `data_handler.py` | Collects and stores telematics data like speed, acceleration, braking, etc. |
| `driver_behavior.py` | Analyzes behavior data to identify risky driving patterns. |
| `risk_evaluator.py` | Converts the risk factor into a numerical risk score. |
| `policy_pricing.py` | Dynamically adjusts the base insurance premium based on the risk score. |
| `user_feedback.py` | Generates personalized feedback and safety tips. |
| `core.py` | Orchestrates the full pipeline from data generation to output and feedback. |

---

## 🔁 Workflow Pipeline

The system follows a streamlined pipeline:

1. **Telematics Data Collection**  
   Simulates raw driving data for multiple trip events.

2. **Behavior Analysis**  
   Identifies risky driving patterns such as excessive speed or harsh braking.

3. **Risk Scoring**  
   Assigns a risk score (0.0 to 1.0) based on behavior frequency and severity.

4. **Pricing Adjustment**  
   Modifies the base insurance premium (up to 50%) depending on the risk score.

5. **Feedback Generation**  
   Produces personalized suggestions to help the driver improve safety and lower future premiums.

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.7 or above
- Required libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `scikit-learn`

> Install dependencies listed in `requirements.txt`.

---

### 📥 Installation & Usage

1. Clone the repo:

   ```bash
   git clone https://github.com/MrVarshu/Devops_Insurance.git
   cd Devops_Insurance

2. Install dependencies
   ```bash
   pip install -r requirements.txt
3. Run the main program
   ```bash
   python main.py

### Future Enhancements
- Incorporate machine learning models for more accurate risk prediction.

- Add support for multiple drivers with separate profiles.

- Integrate privacy-preserving features such as data anonymization and encryption.

- Develop a real-time web or mobile interface for driver feedback.

- Use real telematics datasets for validation and tuning.
