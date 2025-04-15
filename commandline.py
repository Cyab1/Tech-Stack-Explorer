import argparse
import requests
from datetime import datetime, timedelta
from colorama import Fore, Style, init  # pip install colorama
import json
import os

# Initialize colorama
init(autoreset=True)
CACHE_FILE = "repo_cache.json"
CACHE_EXPIRY_HOURS = 6


def get_cached_repos(language):
    if not os.path.exists(CACHE_FILE):
        return None

    with open(CACHE_FILE, "r") as f:
        cache = json.load(f)
        cached_data = cache.get(language)
        if cached_data and (
            datetime.now() - datetime.fromisoformat(cached_data["timestamp"])
        ) < timedelta(hours=CACHE_EXPIRY_HOURS):
            return cached_data["repos"]
    return None


def cache_repos(language, repos):
    cache = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            cache = json.load(f)

    cache[language] = {"repos": repos, "timestamp": datetime.now().isoformat()}

    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f)


def fetch_trending_repos(language="python", days=7):
    # Check cache first
    cached_repos = get_cached_repos(language)
    if cached_repos:
        print(Fore.YELLOW + "⚡ Using cached results (from last 6 hours)")
        return cached_repos

    url = "https://api.github.com/search/repositories"
    params = {
        "q": f"language:{language} created:>{(datetime.now() - timedelta(days=days)).date()}",
        "sort": "stars",
        "order": "desc",
    }
    headers = {"Accept": "application/vnd.github.v3+json"}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        repos = response.json()["items"][:5]
        cache_repos(language, repos)
        return repos
    except Exception as e:
        print(Fore.RED + f"⚠️ Error: {e}")
        return []


def main():
    parser = argparse.ArgumentParser(description="Find trending GitHub repos")
    parser.add_argument(
        "-l", "--language", default="python", help="Programming language filter"
    )
    parser.add_argument("-d", "--days", type=int, default=7, help="Time window in days")
    args = parser.parse_args()

    repos = fetch_trending_repos(args.language, args.days)

    print(
        Fore.CYAN
        + f"\n🌟 Top {len(repos)} Trending {args.language.upper()} Repos (Last {args.days} Days):\n"
    )
    for repo in repos:
        print(Fore.GREEN + f"📌 {repo['name']}")
        print(
            Fore.BLUE + f"   Description: {repo.get('description', 'No description')}"
        )
        print(Fore.YELLOW + f"   ⭐ Stars: {repo['stargazers_count']}")
        print(Fore.MAGENTA + f"   🔗 URL: {repo['html_url']}\n")


if __name__ == "__main__":
    main()
