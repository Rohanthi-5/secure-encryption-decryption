# Secure Text Encryption and Decryption Using Linear Transformations and Random Factors

A Python-based text encryption and decryption system built using mathematical transformations, ASCII manipulation, random factors, and performance analysis techniques. This project was developed as part of an internship at Aviratha Digital Labs and demonstrates how linear algebra concepts can be applied to secure communication.

---

## Features

- **Custom Encryption Algorithm** – Encrypts text using linear transformations derived from a user-provided key.
- **Accurate Decryption** – Recovers the original message by reversing the mathematical operations.
- **Random Factor Integration** – Adds randomness to encrypted output for improved security.
- **Lightweight Implementation** – Uses only Python standard libraries.
- **Performance Analysis** – Graphs encryption and decryption time using Matplotlib.
- **GUI Application** – Built using Tkinter for easy user interaction.
- **Suitable for Academic Use** – Ideal for demonstrating encryption concepts and algorithm design.

---

## Project Structure

```
Encrydecry/
│── ende.py          # Main script for encryption, decryption, GUI, and graph plotting
│── README.md        # Project documentation
```

## Algorithm Overview

The encryption algorithm is based on mathematical transformations:

- Converts characters into their ASCII values.
- Generates a multiplier using the key provided by the user.
- Applies a linear transformation to compute encrypted numeric values.
- Adds random factors so identical characters produce different encrypted outputs.
- Decryption reverses all mathematical operations to retrieve the original ASCII values.
- Ensures that incorrect keys fail validation, preventing unauthorized access.

---

## Installation

Clone the repository:

git clone https://github.com/your-username/encrydecry.git

cd encrydecry
Run the application:

## python ende.py

## Usage

- Enter the text you want to encrypt or decrypt.
- Provide a numeric key.
- Click **Encrypt** or **Decrypt**.
- View the resulting output in the GUI.
- Performance graphs will show encryption and decryption times.

---

## Performance Analysis

- Measures encryption and decryption time across multiple runs.
- Uses Matplotlib to visualize results.
- Helps evaluate the algorithm’s efficiency and optimization.

---

## Technologies Used

- Python
- Tkinter
- Matplotlib
- Linear Algebra
- Random Number Generation
- Basic Cryptography Concepts

---

## Author

**Rohanthi Nayani V**  
3rd Year BCA  
Aviratha Digital Labs – Internship Project  
Nagarjuna College of Management Studies

---

## License

This project is open-source and available for academic and learning purposes.
