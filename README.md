# Password Generator (CLI)

A simple command-line password generator built as a Python practice project. Lets you choose the password length and which character types to include (lowercase is always included; numbers, uppercase, and symbols are optional).

## Folder Structure

```
.
├── main.py       # App entry point
├── helper.py     # Reusable y/n input validation helper
├── README.md
├── .gitignore
└── LICENSE
```

## Usage

Run the app:

```bash
python main.py
```

You'll be prompted for a length, then asked which character types to include:

```
Enter password length: 12
Include numbers? (y/n): y
Include uppercase? (y/n): y
Include symbols? (y/n): n
Generated password: qk3jRt9mZxo1
```

## How It Works

- `helper.py` contains `ask()`, which repeatedly prompts a yes/no question until the user enters `y` or `n`.
- `main.py` builds up a pool of allowed characters based on the user's choices, then picks characters from that pool one at a time using `random.choice()` to build the final password.

## ⚠️ Note on Security

This project was built purely as a **Python practice exercise**, it is **not intended for generating real, security-sensitive passwords**.

It uses Python's built-in `random` module, which relies on a Mersenne Twister pseudo-random number generator (PRNG). This PRNG is fast and great for simulations, games, or general-purpose randomness, but it is **not cryptographically secure**: given enough observed output, it's possible to predict future values. That makes it unsuitable for anything where unpredictability actually matters, like passwords, tokens, or encryption keys.

For real-world password generation, use Python's [`secrets`](https://docs.python.org/3/library/secrets.html) module instead. It's built specifically for security-sensitive tasks and draws from the OS's cryptographically secure random source. Example swap:

```python
import secrets

password = "".join(secrets.choice(characters) for _ in range(length))
```

## License

See [LICENSE](./LICENSE) for details.