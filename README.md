# FileChecker

A Python tool that validates file sharing URLs and identifies broken or invalid links from various file hosting services.

## Features

- Validates URLs from Mega, Uptobox, Google Drive, MediaFire, and other file hosting services
- Processes CSV input and outputs broken links to a separate CSV file

## Requirements

### System Requirements
- Python 3.x
- Google Chrome browser
- ChromeDriver

### ChromeDriver Setup (REQUIRED)
**ChromeDriver is essential for this tool to work properly.**

1. **Download ChromeDriver**:
   - Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/)
   - Download the version that matches your Chrome browser version
   - Check your Chrome version: `chrome://version/` in address bar

2. **Install ChromeDriver**:
   - **Windows**: Place `chromedriver.exe` in a folder that's in your PATH (e.g., `C:\Windows\System32\`) or in the same folder as your project
   - **macOS/Linux**: Move to `/usr/local/bin/` or add to PATH


## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare Input**: Update `Input.csv` with your URLs:
   ```csv
   Name, Link
   File 1, https://mega.nz/file/example
   File 2, https://uptobox.com/example
   ```

2. **Run the tool**:
   ```bash
   python app.py
   ```

3. **Check Results**: Broken links will be saved to `Output.csv`


## Troubleshooting

### ChromeDriver Errors
- **"chromedriver not found"**: ChromeDriver is not in PATH or not installed
- **"session not created"**: ChromeDriver version doesn't match Chrome browser version
- **Solution**: Download the correct ChromeDriver version and ensure it's accessible

### Common Issues
- **Slow performance**: Tool waits 8 seconds on MEGA URLs for dynamic content to load
- **Network errors**: Check internet connection and firewall settings

## Files

- `app.py` - Main application
- `Input.csv` - URLs to check
- `Output.csv` - Broken links output
- `requirements.txt` - Python dependencies

## Author
-Created by Arshit Rawat

