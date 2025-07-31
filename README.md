````markdown
# 🗂️ Auto File Organizer

A Python utility to automatically organize your files based on type, date, or custom rules — perfect for keeping your Downloads folder tidy and stress-free.

> Built with simplicity, modularity, and future extensibility in mind.

---

## 🚀 Features

- 🔄 Move files to folders based on extension
- 📁 Create folder structures on the fly
- 🧠 Supports rule files (`.json`) for custom behaviors
- 🔙 Undo functionality (recover your last batch of moves)
- 🛠 Easily extendable with new rules, filters, or backends
- 🧠 Auto organizers files on drop

---

## 🧪 How It Works

You define a set of file rules like this:

```json
{
  ".jpg": "Images",
  ".pdf": "Documents/PDFs",
  ".zip": "Archives"
}
````

Then run the script to organize your target folder. The script:

1. Scans the folder for files.
2. Applies the rules to determine destinations.
3. Moves the files accordingly.
4. Records each move in `undo.json` so it can be reversed later.

---

## 🛠️ Installation

```bash
git clone https://github.com/compiledchaos/auto_file_organizer.git
cd auto_file_organizer
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

### With Arguments

```bash
python cli.py --simulate --rules myrules.json --logfile logs/output.log
```

---

## 🔙 Undo Last Organize

```bash
python -c "from organizer.core import undo; undo()"
```

This will read from `undo.json` and move all files back to their original locations.

---

## 🧠 Contributing

Pull requests, suggestions, and issue reports are welcome.
If you want to contribute a feature (like the Watcher or GUI), open an issue first to discuss it!

---

## 📝 License

This project is licensed under the MIT License.

---

## 👤 Author

Built by [compiledchaos](https://github.com/compiledchaos) (Sachin Karthikeyan).
````

