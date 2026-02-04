# 🕷️ Web Scraper PRO V4 - Professional Async Web Scraper

A high-performance web scraper built with Python, asyncio, and aiohttp. Designed to extract data from multiple websites in parallel with intelligent rate limiting, automatic retry, and robust error handling.

**✅ 100% Compatible with Windows, macOS, and Linux**

---

## ✨ Key Features

- **Asynchronous Processing**: Uses asyncio and aiohttp for parallel HTTP requests
- **Intelligent Rate Limiting**: Controls request frequency to avoid server overload
- **Automatic Retry with Exponential Backoff**: Retries failed requests automatically
- **URL Validation**: Validates URLs before making requests
- **Detailed Logging**: Real-time feedback on scraping progress
- **Advanced Data Extraction**: Extracts structured data (title, author, date, summary, content, etc.)
- **Sentiment Analysis**: Analyzes sentiment of extracted content
- **Complete Statistics**: Calculates success rate, total time, and average speed
- **JSON Export**: Automatically saves results in formatted JSON
- **Professional Dashboard**: Visual interface with interactive charts and real-time updates
- **Site Rotation**: Automatically rotates between 30+ different sources for variety
- **Multi-platform Compatibility**: Works perfectly on Windows, macOS, and Linux

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|-----------|---------|---------|
| Python | 3.8+ | Main language |
| aiohttp | 3.9.1+ | Async HTTP client |
| BeautifulSoup4 | 4.12.2+ | HTML/XML parsing |
| lxml | 4.9.3+ | High-performance XML/HTML parser |
| python-dotenv | 1.0.0+ | Environment variable management |

---

## 📋 Prerequisites

Before running the project, you need to install:

### 1. Python 3.8+
- **Download**: https://www.python.org/downloads/
- **⚠️ IMPORTANT (Windows)**: During installation, check the box that says **"Add Python to PATH"**

### 2. Git
- **Download**: https://git-scm.com/download/win
- **⚠️ IMPORTANT**: Use default installation settings

### 3. Internet Connection
- Required to download dependencies and access websites for scraping

---

## 🚀 Quick Start (Easiest Way)

### For Windows Users

1. **Download the project**:
   ```powershell
   git clone https://github.com/lucasandre16112000-png/02-web-scraper-async.git
   cd 02-web-scraper-async
   ```

2. **Run the launcher** (double-click):
   ```
   RODAR_WEB_SCRAPER.vbs
   ```
   
   OR run in PowerShell:
   ```powershell
   .\RODAR_WEB_SCRAPER.bat
   ```

3. **That's it!** The dashboard will open automatically in your browser.

### For macOS/Linux Users

1. **Download the project**:
   ```bash
   git clone https://github.com/lucasandre16112000-png/02-web-scraper-async.git
   cd 02-web-scraper-async
   ```

2. **Run the setup**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python3 server.py
   ```

3. **Open your browser**: http://localhost:8000

---

## 📝 Step-by-Step Installation Guide

### Step 1: Clone the Repository

Open your terminal (or PowerShell on Windows) and run:

```bash
git clone https://github.com/lucasandre16112000-png/02-web-scraper-async.git
cd 02-web-scraper-async
```

### Step 2: Create Virtual Environment

A virtual environment isolates project dependencies from your system Python.

**Windows (PowerShell)**:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Windows (Command Prompt)**:
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

You'll know the virtual environment is active when you see `(venv)` at the beginning of your terminal line.

### Step 3: Install Dependencies

With the virtual environment activated:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Server

```bash
# Windows
python server.py

# macOS/Linux
python3 server.py
```

### Step 5: Open Dashboard

The browser will open automatically at: **http://localhost:8000**

If not, open your browser and go to: `http://localhost:8000`

### Step 6: Start Scraping

1. Click the **"🚀 Start Scraping PRO"** button
2. Watch the progress bar in real-time
3. See the data appear in charts and tables
4. Results are saved to `scraping_results.json`

---

## 🎯 Usage Examples

### Example 1: Run the Default Scraper

```bash
python server.py
```

Then click the button in the dashboard.

### Example 2: Use Scraper in Your Own Code

```python
import asyncio
from scraper import WebScraper

async def my_scraper():
    scraper = WebScraper(
        requests_per_second=2.0,  # Max 2 requests/second
        timeout=10,                # 10 second timeout
        max_retries=3              # Max 3 attempts
    )
    
    urls = ["https://example.com", "https://another-site.com"]
    articles = await scraper.scrape_articles(urls)
    
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}")
        print(f"Sentiment: {article['sentiment']}")

asyncio.run(my_scraper())
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Web Scraper Configuration
REQUESTS_PER_SECOND=2.0
TIMEOUT=10
MAX_RETRIES=3
LOG_LEVEL=INFO
```

### WebScraper Parameters

```python
scraper = WebScraper(
    requests_per_second=2.0,  # Requests per second (default: 2.0)
    timeout=10,                # Timeout in seconds (default: 10)
    max_retries=3,             # Max retry attempts (default: 3)
    output_dir=None            # Output directory (default: current)
)
```

---

## 📊 Dashboard Features

### Real-time Statistics
- Total articles collected
- Success/failure count
- Average engagement score
- Processing time

### Interactive Charts
- Sentiment distribution (pie chart)
- Articles by source (bar chart)
- Articles by category (pie chart)
- Top articles by engagement (line chart)

### Data Display
- Complete article list with all details
- Filterable by sentiment
- Sortable columns
- Expandable article details

---

## 🔄 Data Collection Process

1. **Site Selection**: Randomly selects from 30+ sources
2. **Fetching**: Asynchronously fetches content from selected sites
3. **Parsing**: Extracts structured data using BeautifulSoup
4. **Analysis**: Performs sentiment analysis and categorization
5. **Storage**: Saves results to JSON and displays in dashboard
6. **Visualization**: Updates charts and tables in real-time

---

## 📁 Project Structure

```
02-web-scraper-async/
├── scraper.py                # Main scraper with advanced features
├── server.py                 # Web server and API
├── dashboard.html            # Professional web interface
├── RODAR_WEB_SCRAPER.vbs    # Windows launcher (VBScript)
├── RODAR_WEB_SCRAPER.bat    # Windows launcher (Batch)
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── scraping_results.json     # Output file (generated)
```

---

## 🆘 Troubleshooting

### Problem: "Python not found" (Windows)

**Solution**:
1. Reinstall Python from https://www.python.org/downloads/
2. **Make sure to check "Add Python to PATH"**
3. Restart your computer
4. Open a new terminal and try again

### Problem: "ModuleNotFoundError: No module named 'aiohttp'"

**Solution**:
1. Make sure virtual environment is activated (you should see `(venv)` in terminal)
2. Run: `pip install -r requirements.txt`
3. Wait for installation to complete

### Problem: "Port 8000 already in use"

**Solution**:
1. Close the browser
2. Wait 5 seconds
3. Try again
4. OR change the port in `server.py` (line with `PORT = 8000`)

### Problem: "Connection timeout or network errors"

**Solution**:
1. Check your internet connection
2. Try again in a few minutes
3. Some websites may have rate limiting or blocking
4. The scraper has automatic retry with exponential backoff

### Problem: "Browser doesn't open automatically"

**Solution**:
1. Open your browser manually
2. Go to: http://localhost:8000
3. The server should be running in the terminal

### Problem: "No data appears in dashboard"

**Solution**:
1. Click the "🚀 Start Scraping PRO" button
2. Wait for the progress bar to complete
3. Check the terminal for any error messages
4. Make sure you have an active internet connection

---

## 📊 Output Format

### JSON Results

The scraper saves results to `scraping_results.json`:

```json
{
  "timestamp": "2026-02-03T20:00:00.000000",
  "sources": [
    {
      "name": "Hacker News",
      "url": "https://news.ycombinator.com",
      "articles_count": 15
    }
  ],
  "articles": [
    {
      "title": "Article Title",
      "url": "https://example.com/article",
      "author": "Author Name",
      "published_date": "2026-02-03",
      "summary": "Article summary...",
      "content": "Full article content...",
      "category": "Technology",
      "tags": ["python", "web", "scraping"],
      "views": 1000,
      "likes": 150,
      "comments": 45,
      "shares": 20,
      "engagement_score": 8.5,
      "sentiment": "positive",
      "keywords": ["python", "scraping", "data"],
      "image_url": "https://example.com/image.jpg",
      "reading_time": 5,
      "scraped_at": "2026-02-03T20:00:00.000000"
    }
  ],
  "statistics": {
    "total_articles": 150,
    "total_sources": 10,
    "successful_sources": 10,
    "failed_sources": 0,
    "total_time": 45.23,
    "items_per_second": 3.32,
    "average_engagement": 7.8,
    "sentiment_distribution": {
      "positive": 85,
      "neutral": 50,
      "negative": 15
    },
    "categories": {
      "Technology": 60,
      "Business": 40,
      "Science": 50
    }
  }
}
```

---

## 🔒 Best Practices & Ethics

1. **Respect robots.txt**: Check the site's `robots.txt` before scraping
2. **Use Rate Limiting**: Don't make requests too fast
3. **Check Terms of Service**: Ensure you have permission to scrape
4. **Identify Yourself**: Use appropriate User-Agent (done automatically)
5. **Don't Store Personal Data**: Be careful with sensitive information
6. **Be Respectful**: Don't overload servers with requests

---

## 📈 Performance Metrics

- **Async Processing**: Up to 10x faster than synchronous requests
- **Rate Limiting**: Configurable from 0.5 to 10 requests/second
- **Retry Logic**: Automatic recovery from transient failures
- **Memory Efficient**: Processes data in streams
- **Scalable**: Can handle 100+ URLs simultaneously

---

## 🔄 Data Sources (30+ Sites)

### Tech News
- Hacker News
- TechCrunch
- The Verge
- Wired
- Ars Technica
- AnandTech

### Programming
- Reddit r/programming
- Dev.to
- Medium
- CSS Tricks
- Smashing Magazine
- A List Apart

### Product & Startup
- Product Hunt
- Indie Hackers
- Y Combinator

### Community
- GitHub Trending
- Lobsters
- Hacker News New

### Analysis
- Slashdot
- InfoQ
- DZone
- SitePoint

### Design
- Web Designer Depot
- Dribbble
- Designer Hangout

### Learning
- FreeCodeCamp
- Scotch.io
- Egghead

### Showcase
- Codepen
- Codesignal

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 👨‍💻 Author

**Lucas André S**
- GitHub: https://github.com/lucasandre16112000-png

---

## 📞 Support

If you encounter issues:

1. Check the **Troubleshooting** section above
2. Review the **logs/scraper.log** file for details
3. Check your internet connection
4. Ensure Python and Git are properly installed
5. Open an issue on GitHub

---

## 🚀 Version History

### v4.0 (Current)
- ✅ Professional dashboard with real-time updates
- ✅ 30+ data sources with automatic rotation
- ✅ Advanced sentiment analysis
- ✅ Interactive charts and visualizations
- ✅ Complete data extraction (16+ fields)
- ✅ Windows launcher (.vbs) - no terminal visible
- ✅ 100% Windows compatibility

### v3.0
- ✅ Improved data extraction
- ✅ Better categorization
- ✅ Enhanced error handling

### v2.0
- ✅ Windows event loop compatibility
- ✅ Automatic setup scripts
- ✅ Environment variable support

### v1.0
- ✅ Basic async scraper
- ✅ Rate limiting
- ✅ Retry logic

---

**Made with ❤️ for easy web scraping**

Last updated: February 3, 2026
