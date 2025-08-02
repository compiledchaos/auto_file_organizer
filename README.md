# 🗂️ Auto File Organizer

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-19%20passed-brightgreen.svg)](./tests.py)

A powerful, flexible Python utility to automatically organize your files based on extensions, custom rules, or real-time monitoring. Perfect for keeping your Downloads folder, desktop, or any directory clean and organized.

> **Built with simplicity, modularity, and extensibility in mind** — from basic CLI usage to advanced GUI and real-time monitoring.

---

## ✨ Features

### 🔧 **Core Functionality**
- 🔄 **Smart File Organization** - Automatically move files to folders based on extensions
- 📁 **Dynamic Folder Creation** - Creates destination folders on-the-fly
- 🧠 **Custom Rules** - Support for JSON rule files with flexible configurations
- 🔙 **Full Undo Support** - Safely reverse any organization with complete history tracking
- 🎯 **Simulation Mode** - Preview changes before applying them
- 🔄 **Reset Functionality** - Clear organization history when needed

### 🖥️ **Multiple Interfaces**
- 💻 **Command Line Interface** - Full-featured CLI with comprehensive options
- 🖼️ **Graphical User Interface** - User-friendly GUI for non-technical users
- 👁️ **Real-time File Watcher** - Automatically organize files as they're added

### 🛡️ **Robust & Reliable**
- 📝 **Comprehensive Logging** - Detailed logs with file and console output options
- ⚡ **Error Handling** - Graceful handling of permission errors, missing files, and edge cases
- 🔄 **Retry Logic** - Automatic retry for temporary file access issues
- 🧪 **Thoroughly Tested** - 19 comprehensive tests covering all functionality

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/compiledchaos/auto_file_organizer.git
cd auto_file_organizer

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -e .
```

### Basic Usage

```bash
# Organize your Downloads folder with default rules
auto-organize --source ~/Downloads

# Preview changes without moving files
auto-organize --source ~/Downloads --simulate

# Use custom rules
auto-organize --source ~/Downloads --rules my_rules.json

# Enable logging
auto-organize --source ~/Downloads --logfile organizer.log
```

---

## 📖 Usage Guide

### 🖥️ Command Line Interface

```bash
auto-organize [OPTIONS]

Options:
  --source PATH          Source directory to organize (default: ~/Downloads)
  --rules PATH           Custom JSON rules file
  --simulate             Preview changes without moving files
  --undo                 Undo the last organization
  --reset                Clear organization history
  --logfile PATH         Enable file logging
  --gui                  Launch graphical interface
  --watchdog             Enable real-time file monitoring
  --help                 Show help message
```

### 🖼️ Graphical Interface

```bash
# Launch the GUI
auto-organize --gui
```

The GUI provides:
- 📁 **Folder Selection** - Easy directory browsing
- ▶️ **One-Click Organization** - Simple organize button
- 🔙 **Undo Support** - Reverse changes with one click
- 🔄 **Reset Option** - Clear history when needed
- 📝 **Real-time Feedback** - Status updates and progress display

### 👁️ Real-time File Watcher

```bash
# Monitor and auto-organize files as they're added
auto-organize --source ~/Downloads --watchdog
```

Perfect for:
- 📥 **Downloads folders** - Organize files as they download
- 🖥️ **Desktop cleanup** - Keep desktop organized automatically
- 📁 **Project directories** - Maintain organized file structures

---

## ⚙️ Configuration

### Default Rules

The organizer comes with sensible defaults:

```json
{
  ".txt": "Documents",
  ".pdf": "Documents",
  ".doc": "Documents",
  ".docx": "Documents",
  ".jpg": "Images",
  ".jpeg": "Images",
  ".png": "Images",
  ".gif": "Images",
  ".mp4": "Videos",
  ".avi": "Videos",
  ".mov": "Videos",
  ".zip": "Archives",
  ".rar": "Archives",
  ".7z": "Archives"
}
```

### Custom Rules

Create your own `rules.json` file:

```json
{
  ".py": "Code/Python",
  ".js": "Code/JavaScript",
  ".css": "Code/Stylesheets",
  ".html": "Code/Web",
  ".xlsx": "Spreadsheets",
  ".pptx": "Presentations",
  ".sketch": "Design/Sketch",
  ".fig": "Design/Figma"
}
```

---

## 🔄 Advanced Features

### Undo Functionality

```bash
# Undo the last organization
auto-organize --undo

# Or undo specific operations
auto-organize --source ~/Downloads --undo
```

### Simulation Mode

```bash
# Preview what would happen without making changes
auto-organize --source ~/Downloads --simulate
```

### Logging

```bash
# Log to file
auto-organize --source ~/Downloads --logfile ~/organizer.log

# View logs in real-time
tail -f ~/organizer.log
```

### Reset History

```bash
# Clear all organization history
auto-organize --reset
```

---

## 🧪 How It Works

1. **📂 Scan** - Identifies all files in the source directory
2. **🎯 Match** - Applies rules to determine destination folders
3. **📁 Create** - Creates destination folders if they don't exist
4. **🔄 Move** - Safely moves files with retry logic for errors
5. **📝 Record** - Logs all moves in `~/.auto_file_organizer/undo.json`
6. **✅ Verify** - Confirms successful operations

### File Safety

- **🔒 Backup on Conflict** - Existing files are backed up before replacement
- **🔄 Retry Logic** - Automatic retry for permission errors
- **📝 Complete History** - Every move is recorded for undo capability
- **🛡️ Error Handling** - Graceful handling of edge cases

---

## 🧪 Testing

The project includes comprehensive tests covering all functionality:

```bash
# Run all tests
pytest tests.py -v

# Run specific test categories
pytest tests.py::TestComprehensiveFileOrganizer::test_core_file_organization -v
pytest tests.py::TestComprehensiveFileOrganizer::test_gui_comprehensive -v
pytest tests.py::TestComprehensiveFileOrganizer::test_watchdog_functionality -v
```

**Test Coverage:**
- ✅ Core file organization
- ✅ CLI interface and arguments
- ✅ GUI functionality
- ✅ Watchdog file monitoring
- ✅ Error handling and edge cases
- ✅ Undo and reset operations
- ✅ Custom rules and logging

---

## 🏗️ Project Structure

```
auto_file_organizer/
├── organizer/
│   ├── __init__.py
│   ├── core.py              # Core FileOrganizer class
│   ├── cli.py               # Command line argument parsing
│   ├── commands.py          # CLI and entry point functions
│   ├── app.py               # GUI application
│   ├── file_watcher.py      # Real-time file monitoring
│   ├── logger_code.py       # Logging configuration
│   └── utils/
│       ├── __init__.py
│       ├── data.py          # Rules and history management
│       ├── gui_utils.py     # GUI utility functions
│       ├── logger_setup.py  # Logger setup utilities
│       └── record.py        # Move recording and undo logic
├── tests.py                 # Comprehensive test suite
├── setup.py                 # Package configuration
├── requirements.txt         # Dependencies
└── README.md               # This file
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **🐛 Report Issues** - Found a bug? Open an issue with details
2. **💡 Suggest Features** - Have ideas? Share them in the discussions
3. **🔧 Submit PRs** - Ready to code? Fork and submit a pull request
4. **📖 Improve Docs** - Help make the documentation better
5. **🧪 Add Tests** - More test coverage is always appreciated

### Development Setup

```bash
# Clone and setup development environment
git clone https://github.com/compiledchaos/auto_file_organizer.git
cd auto_file_organizer
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -e .[dev]

# Run tests
pytest tests.py -v

# Run with coverage
pytest tests.py --cov=organizer
```

---

## 📋 Requirements

- **Python 3.8+**
- **watchdog** - For file system monitoring
- **tkinter** - For GUI (usually included with Python)
- **setuptools** - For package management

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Sachin Karthikeyan** ([compiledchaos](https://github.com/compiledchaos))

- 📧 Email: sachinprathik8@gmail.com
- 🌐 GitHub: [@compiledchaos](https://github.com/compiledchaos)

---

## 🙏 Acknowledgments

- Thanks to the Python community for excellent libraries
- Inspired by the need for better file organization tools
- Built with ❤️ for developers and end-users alike

---

**⭐ If this project helped you, please consider giving it a star!**

