# 🕷️ Web Scraper PRO - Professional Dashboard

A professional asynchronous web scraper with interactive dashboard, rotation of 30+ sources, advanced analytics, and modern visual interface. Built with Python, `asyncio`, and `aiohttp`.

**✅ 100% Compatible with Windows, macOS, and Linux**

---

## ✨ Key Features

- **🚀 Asynchronous Processing**: Multiple HTTP requests in parallel with `asyncio` and `aiohttp`
- **🔄 Rotation of 30+ Sources**: Always collects data from different websites
- **📊 Interactive Dashboard**: Professional visual interface with real-time graphs
- **🎯 Advanced Analytics**: Sentiment analysis, engagement scoring, intelligent categorization
- **⚡ Smart Rate Limiting**: Controls requests without overloading servers
- **🔁 Automatic Retry**: Exponential backoff for failed requests
- **✅ URL Validation**: Validates before making requests
- **📝 Detailed Logging**: Real-time progress feedback
- **📁 JSON Export**: Automatically saves structured data
- **🖥️ Cross-Platform**: Works on Windows, macOS, and Linux

---

## 🛠️ Required Programs to Download

Before you start, you need to download and install these two programs:

### 1. **Git** (Required to clone the project)
- **Download**: https://git-scm.com/downloads
- **Why**: To download the project from GitHub
- **Installation**: Download and run the installer, click "Next" on all screens

### 2. **Python** (Required to run the scraper)
- **Download**: https://www.python.org/downloads/
- **Version**: Python 3.8 or higher (recommended: Python 3.10+)
- **Installation**: 
  - Download and run the installer
  - **IMPORTANT**: Check the box that says **"Add Python to PATH"** ✅
  - Click "Install Now"
  - Wait for installation to complete

---

## 📂 Project Structure

```
/02-web-scraper-async
├── scraper_pro_v4.py           # Main scraper (final version)
├── server_pro_v4.py            # Web server with dashboard
├── dashboard_pro.html          # Professional visual interface
├── RODAR_WEB_SCRAPER.vbs       # Windows launcher (recommended)
├── RODAR_WEB_SCRAPER.bat       # Windows launcher (backup)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── DASHBOARD.md                # Dashboard guide
└── LEIA-ME-CLIENTE.txt         # Client instructions
```

---

## 🚀 Quick Start Guide (RECOMMENDED)

### Windows - Click 2 Times (Easiest)

1. **Download and Install Git**: https://git-scm.com/downloads
2. **Download and Install Python**: https://www.python.org/downloads/
   - ⚠️ Check "Add Python to PATH" during installation
3. **Open PowerShell** in the project folder
4. **Run**:
   ```powershell
   git clone https://github.com/lucasandre16112000-png/02-web-scraper-async.git
   cd 02-web-scraper-async
   ```
5. **Double-click** `RODAR_WEB_SCRAPER.vbs`
6. **Wait** for the browser to open
7. **Click** "🚀 Start Scraping PRO"
8. **Done!** Dashboard shows data in real-time

---

## 📋 Step-by-Step Installation Guide

### Step 1: Download Required Programs

#### For Windows:
1. Download Git: https://git-scm.com/downloads
2. Download Python: https://www.python.org/downloads/
3. Run both installers and follow the default options

#### For macOS:
1. Download Git: https://git-scm.com/downloads
2. Download Python: https://www.python.org/downloads/
3. Or use Homebrew:
   ```bash
   brew install git python3
   ```

#### For Linux (Ubuntu/Debian):
```bash
sudo apt-get update
sudo apt-get install git python3 python3-pip python3-venv
```

---

### Step 2: Clone the Project

Open **PowerShell** (Windows) or **Terminal** (macOS/Linux) and run:

```bash
git clone https://github.com/lucasandre16112000-png/02-web-scraper-async.git
cd 02-web-scraper-async
```

---

### Step 3: Create Virtual Environment

A virtual environment isolates project dependencies from your system.

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

✅ You'll see `(venv)` at the start of your terminal line when activated.

---

### Step 4: Install Dependencies

With the virtual environment activated, run:

```bash
pip install -r requirements.txt
```

This installs all required Python libraries.

---

### Step 5: Run the Dashboard Server

**Windows:**
```powershell
python server_pro_v4.py
```

**macOS/Linux:**
```bash
python3 server_pro_v4.py
```

You should see:
```
================================================================================
🌐 PROFESSIONAL WEB SERVER PRO V4 - SITE ROTATION
================================================================================
✅ Server started at: http://localhost:8000
🌍 Opening in browser...
⏹️  Press CTRL+C to stop the server
================================================================================
```

---

### Step 6: Use the Dashboard

1. **Browser opens automatically** at `http://localhost:8000`
2. **Click** the button "🚀 Start Scraping PRO"
3. **Watch** the progress bar and real-time updates
4. **See** graphs and statistics appear automatically
5. **Explore** the list of 50+ collected articles

---

## 🎯 Using the Dashboard

### What You'll See

- **Status Section**: Real-time progress of the scraper
- **Statistics Cards**: Total articles, sources, categories, engagement
- **Graphs**: 
  - Sentiment distribution (pie chart)
  - Articles per source (bar chart)
  - Articles per category (pie chart)
  - Top articles by engagement (bar chart)
- **Article List**: All collected articles with details

### How to Interact

1. **Start Scraping**: Click "🚀 Start Scraping PRO" button
2. **Watch Progress**: See the progress bar update in real-time
3. **View Results**: Graphs and statistics update automatically
4. **Scroll Down**: See the complete list of articles
5. **Stop Server**: Press `CTRL+C` in the terminal to stop

---

## 📊 Data Collected

Each article contains:
- ✅ Title
- ✅ URL
- ✅ Author
- ✅ Publication date
- ✅ Summary
- ✅ Full content
- ✅ Category (12 types)
- ✅ Tags
- ✅ Views, Likes, Comments
- ✅ Engagement score
- ✅ Sentiment analysis
- ✅ Keywords

---

## 📡 30+ Data Sources

**Tech News:**
Hacker News, TechCrunch, The Verge, Wired, Ars Technica, AnandTech

**Programming:**
Reddit r/programming, Dev.to, Medium, CSS Tricks, Smashing Magazine

**Product & Startup:**
Product Hunt, Indie Hackers, Y Combinator

**Community:**
GitHub Trending, Lobsters, Hacker News New

**Analysis:**
Slashdot, InfoQ, Dzone, SitePoint

**Design:**
Web Designer Depot, Dribbble, Designer Hangout

**Learning:**
FreeCodeCamp, Scotch.io, Egghead

**Showcase:**
Codepen, Codesignal

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|:---|:---|:---|
| **Python** | 3.8+ | Main language |
| **aiohttp** | 3.9.1 | Asynchronous HTTP client/server |
| **BeautifulSoup4** | 4.12.2 | HTML/XML parsing |
| **lxml** | 4.9.3 | High-performance XML/HTML parser |
| **python-dotenv** | 1.0.0 | Environment variable management |

---

## 🤔 Troubleshooting

### Problem: "Python is not recognized"

**Solution**:
1. Reinstall Python from https://www.python.org/downloads/
2. **Important**: Check "Add Python to PATH" during installation
3. Restart your computer
4. Open a new terminal and try again

### Problem: "ModuleNotFoundError: No module named 'aiohttp'"

**Solution**:
1. Make sure the virtual environment is activated (you should see `(venv)` in the terminal)
2. Run: `pip install -r requirements.txt`

### Problem: "Git is not recognized"

**Solution**:
1. Download and install Git from https://git-scm.com/downloads
2. Restart your computer
3. Open a new terminal and try again

### Problem: "Dashboard won't open in browser"

**Solution**:
1. Check that the server is running (should show "Server started at http://localhost:8000")
2. Manually open your browser and go to: `http://localhost:8000`
3. Make sure port 8000 is not in use by another program

### Problem: "Connection refused" or "ERR_CONNECTION_REFUSED"

**Solution**:
1. Make sure the server is running: `python server_pro_v4.py`
2. Wait a few seconds for the server to start
3. Refresh the browser page
4. If the problem persists, restart the server

---

## 📁 Output Format (JSON)

The scraper saves results to `scraping_results_pro.json`:

```json
{
  "timestamp": "2026-02-03T20:00:00.000000",
  "articles": [
    {
      "title": "Example Article",
      "url": "https://example.com",
      "author": "John Doe",
      "published_date": "2026-02-03",
      "summary": "Article summary...",
      "content": "Full content...",
      "category": "AI/ML",
      "tags": ["ai", "machine-learning"],
      "views": 1000,
      "likes": 250,
      "comments": 50,
      "shares": 100,
      "engagement_score": 85.5,
      "sentiment": "positive",
      "keywords": ["ai", "ml", "learning"]
    }
  ],
  "statistics": {
    "total_items": 56,
    "successful_items": 56,
    "failed_items": 0,
    "total_time": 12.45,
    "items_per_second": 4.5,
    "status": "completed"
  }
}
```

---

## 🔒 Best Practices & Ethics

- **Respect robots.txt**: Check before scraping
- **Use Rate Limiting**: Don't overload servers
- **Check Terms of Service**: Make sure you have permission
- **Identify Yourself**: Use appropriate User-Agent (automatic)
- **Don't Store Personal Data**: Be careful with sensitive information

---

## 📝 Advanced Configuration

### Custom Environment Variables

Create a `.env` file:

```
REQUESTS_PER_SECOND=2.0
TIMEOUT=10
MAX_RETRIES=3
LOG_LEVEL=INFO
```

### Using the Scraper in Your Code

```python
import asyncio
from scraper_pro_v4 import WebScraperPro

async def main():
    scraper = WebScraperPro()
    results = await scraper.scrape()
    print(f"✅ {len(results)} articles collected!")

asyncio.run(main())
```

---

## 🔄 Current Version (v4.0)

- ✅ Rotation of 30+ sources
- ✅ Professional interactive dashboard
- ✅ Advanced analytics (sentiment, engagement)
- ✅ Intelligent categorization (12 categories)
- ✅ Complete data extraction
- ✅ 100% Windows compatibility
- ✅ Automatic launcher (.vbs)
- ✅ Modern visual interface

---

## 👨‍💻 Author

Lucas André S - [GitHub](https://github.com/lucasandre16112000-png)

---

## 📝 License

MIT License - See LICENSE file for details

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

---

## 📞 Support

If you encounter issues:
1. Check the "Troubleshooting" section above
2. Check logs in `logs/scraper.log`
3. Open an issue on GitHub

---

**Ready to start? Run `python server_pro_v4.py` and open http://localhost:8000 in your browser!** 🚀
