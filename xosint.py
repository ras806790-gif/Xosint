#!/usr/bin/env python3
"""Xosint: lightweight public-profile username checker for Termux/Android."""
import concurrent.futures
import datetime
import re
import sys
import urllib.error
import urllib.request
from urllib.parse import quote

VERSION = "1.0.0"
USER_AGENT = "Xosint/1.0.0 (public profile availability checker)"
TIMEOUT = 12
WORKERS = 8

SITES = [
    ("GitHub", "https://github.com/{u}"),
    ("GitLab", "https://gitlab.com/{u}"),
    ("Reddit", "https://www.reddit.com/user/{u}/"),
    ("Pinterest", "https://www.pinterest.com/{u}/"),
    ("Twitch", "https://www.twitch.tv/{u}"),
    ("SoundCloud", "https://soundcloud.com/{u}"),
    ("Medium", "https://medium.com/@{u}"),
    ("Keybase", "https://keybase.io/{u}"),
    ("Replit", "https://replit.com/@{u}"),
    ("Codeberg", "https://codeberg.org/{u}"),
    ("Hacker News", "https://news.ycombinator.com/user?id={u}"),
    ("Mastodon.social", "https://mastodon.social/@{u}"),
    ("TikTok", "https://www.tiktok.com/@{u}"),
    ("Instagram", "https://www.instagram.com/{u}/"),
    ("X", "https://x.com/{u}"),
    ("YouTube", "https://www.youtube.com/@{u}"),
    ("Facebook", "https://www.facebook.com/{u}"),
]

def check_site(item, username):
    name, template = item
    url = template.format(u=quote(username, safe="@._-"))
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            code, final_url = response.getcode(), response.geturl()
            return {"site": name, "status": "POTENTIAL" if code == 200 else "UNKNOWN",
                    "http": code, "url": final_url,
                    "note": "Verify manually; an HTTP response is not proof of an account."}
    except urllib.error.HTTPError as e:
        return {"site": name, "status": "NOT DETECTED" if e.code == 404 else "UNKNOWN",
                "http": e.code, "url": url,
                "note": "HTTP errors may be site-specific or temporary."}
    except (urllib.error.URLError, TimeoutError, OSError):
        return {"site": name, "status": "ERROR", "http": None, "url": url,
                "note": "Connection failed or site could not be reached."}

def main():
    print(r"""
 __  __           _
 \ \/ /___  ___  (_) __ _ _ __ | |_
  \  // _ \/ __| | |/ _` | '_ \| __|
  /  \  __/\__ \ | | (_| | | | | |_
 /_/\_\___||___/ |_|\__,_|_| |_|\__|
       Public Username OSINT
""")
    print(f"Xosint v{VERSION} | Termux / Android\n")
    username = " ".join(sys.argv[1:]).strip() if len(sys.argv) > 1 else input("Masukkan username: ").strip()
    username = username.lstrip("@").strip()
    if not username or len(username) > 100 or any(c.isspace() for c in username):
        print("Username tidak valid. Masukkan satu username tanpa spasi.")
        raise SystemExit(1)

    print(f"Target: @{username} | Situs: {len(SITES)}\n")
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(check_site, site, username) for site in SITES]
        for future in concurrent.futures.as_completed(futures):
            r = future.result()
            results.append(r)
            print(f"[{r['status']:<12}] {r['site']:<16} {r['url']}")

    order = {site[0]: i for i, site in enumerate(SITES)}
    results.sort(key=lambda r: order.get(r["site"], 999))
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", username)
    filename = f"xosint_{safe}_{stamp}.txt"
    with open(filename, "w", encoding="utf-8") as out:
        out.write(f"Xosint v{VERSION} — username: @{username}\n")
        out.write(f"Generated: {datetime.datetime.now().isoformat(timespec='seconds')}\n\n")
        for r in results:
            out.write(f"[{r['status']}] {r['site']} | HTTP: {r['http']} | {r['url']}\n")
            out.write(f"  Note: {r['note']}\n")
        out.write("\nResults are indicators, not identity verification.\n")
    print(f"\nReport saved: {filename}")

if __name__ == "__main__":
    main()
