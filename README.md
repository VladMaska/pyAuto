# pyAuto

⚙️ **pyAuto** is a simple Python CLI toolkit for automating common file system tasks like renaming, backing up, and cleaning folders.

---

## Features

- Rename files in bulk with customizable patterns
- Backup entire folders with timestamped copies
- Clean folders by deleting files with specific extensions

---

## Installation

```bash
git clone https://github.com/your-username/pyAuto.git
cd pyAuto
pip install -r requirements.txt
```

---

## Usage

```bash
# Rename files
python main.py rename --folder ~/Pictures --pattern "Vacation_{num}" --start 1

# Backup folder
python main.py backup --folder ~/Documents --dest ~/Backups

# Clean folder (delete tmp and log files)
python main.py clean --folder ~/Downloads --ext tmp,log
```

---

## Project Structure

```
pyAuto/
├── main.py
├── cli.py
├── pyauto/
│   ├── __init__.py
│   ├── renamer.py
│   ├── backup.py
│   └── cleaner.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## License

MIT
