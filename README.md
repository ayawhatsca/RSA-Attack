# RSA Encryption & Factoring Attack Simulation

This repository contains a Python-based educational tool that demonstrates the RSA cryptographic process. It covers key generation, encryption, decryption, and a **probabilistic factoring attack** to recover a private key from a public modulus $n$.

---

## 📋 Input Requirements

To ensure the program runs successfully, please follow these input guidelines:

* **Data Type:** You must enter a **positive integer** (e.g., `12`).
* **Value Range:** Since this script uses a small bit-size (4-5 bits) for demonstration purposes, it is recommended to input numbers between **1 and 50**.
* **Restrictions:** Do not enter letters, symbols, or spaces, as this will trigger a `ValueError`.
* **Modulus Constraint:** If your input is larger than the generated modulus $n$, the script is programmed to automatically regenerate a larger key until $n > \text{plaintext}$.

---

## 🚀 How to Run the Script

### Option 1: Using Visual Studio Code (Recommended)

1.  **Install Python:** Ensure you have [Python 3.x](https://www.python.org/) installed.
2.  **Open in VS Code:**
    * Save the code as `rsa_attack.py`.
    * Open the folder containing the file in VS Code.
3.  **Install Extensions:** Install the **Python Extension** by Microsoft.
4.  **Execute:**
    * Press the **Run** button (Play icon) in the top-right corner, or
    * Open the terminal (`Ctrl + ~`) and type:
        ```bash
        python rsa_attack.py
        ```

### Option 2: Running as a Windows Executable (.exe)

If you want to run the program without a Python environment, you can convert it to an `.exe` file:

1.  **Install PyInstaller:** Open your terminal/CMD and run:
    ```bash
    pip install pyinstaller
    ```
2.  **Build the EXE:** Navigate to your script's folder and run:
    ```bash
    pyinstaller --onefile rsa_attack.py
    ```
3.  **Locate the File:** Once finished, go to the newly created **`dist`** folder. You will find `rsa_attack.exe` there. Double-click it to run.

---

## 🧠 How It Works



The program follows these logical steps:

1.  **Key Generation:** Generates two random primes ($p$ and $q$), computes $n = p \times q$, and determines the public ($e$) and private ($d$) keys.
2.  **Encryption:** Converts your plaintext integer into ciphertext using the formula: $C = M^e \pmod{n}$.
3.  **Factoring Attack:** Uses a **Probabilistic Algorithm** to find the factors of $n$. This mimics a mathematical attack on the RSA modulus by finding the greatest common divisor (GCD).
4.  **Key Recovery:** Once $p$ and $q$ are found, it calculates the private key $d$ and decrypts the message to prove the attack was successful.

---

## ⚠️ Important Security Note

This project is for **educational purposes only**. The bit-length used here (4-5 bits) is extremely small to allow the attack to finish in seconds. In real-world applications, RSA uses 2048-bit or 4096-bit keys, which are currently impossible to factor using these methods on standard hardware.
