# 🌟 Tech Stack Explorer CLI

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A command-line tool to discover trending GitHub repositories by programming language. Perfect for developers to stay updated with what's hot in their tech stack!


## ✨ Features

- 🔍 Find top 5 trending repos by language (Python, JavaScript, Go, etc.)
- ⏳ Filter by time window (last 7/30/90 days)
- 💾 Smart caching to avoid GitHub API rate limits
- 🎨 Colorful terminal output for better readability
- ⚡ Lightweight (~50 LOC) with clean architecture

## 🛠 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tech-stack-explorer.git
cd tech-stack-explorer
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```

 ## 🚀 Usage
Basic usage (defaults to Python repos from last 7 days):
```bash
python tech_explorer.py
```
Advanced options:
```bash
python tech_explorer.py --language javascript --days 30
```
## 📊 Example Output
🌟 Top 5 Trending JAVASCRIPT Repos (Last 30 Days):

📌 awesome-ai
   Description: Curated list of AI resources
   ⭐ Stars: 4231
   🔗 URL: https://github.com/user/awesome-ai

📌 nextjs-boilerplate
   Description: Production-ready Next.js template
   ⭐ Stars: 2876
   🔗 URL: https://github.com/user/nextjs-boilerplate

🧠 How It Works
1. Makes authenticated requests to GitHub's search API

2. Caches results locally for 6 hours (saves to repo_cache.json)

3. Formats output with:

- Language filtering

- Time window selection

- Color-coded terminal display   

## 🛠️ Dependencies
- requests - HTTP requests

- colorama - Terminal colors

- Python 3.7+

## 🔧 Possible Extensions
- Add GitHub authentication for higher rate limits

- Export results to CSV/JSON

- Interactive language selection

- Daily automated email reports

## 🤝 Contributing
PRs welcome! To contribute:

1. Fork the project

2. Create your feature branch (git checkout -b feature/amazing-feature)

3. Commit your changes (git commit -m 'Add some amazing feature')

4. Push to the branch (git push origin feature/amazing-feature)

5. Open a Pull Request

📜 License
MIT © Siyabonga