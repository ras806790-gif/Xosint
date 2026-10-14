<div align="center">

<img src="assets/xosint-logo.png" alt="Xosint Logo" width="500">

# Xosint 
### Lightweight public username checker for Android & Termux

[![Platform](https://img.shields.io/badge/platform-Termux%20%7C%20Android-3DDC84?style=for-the-badge)](#requirements)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)

**Xosint** checks whether public profile URLs respond for a given username.
Designed to run on Termux without Kali Linux.

</div>

> **Important:** Results are indicators, not identity verification. A responding page does not prove that an account exists or belongs to a particular person. Sites may block automated requests, change URLs, or return misleading responses.

## Features
- Android and Termux friendly
- Checks a curated list of public profile URLs
- Concurrent requests with a modest worker limit
- Saves timestamped TXT reports
- Uses Python standard library only

## Requirements
- Android with [Termux](https://termux.dev/)
- Python 3.9+
- Internet access

Kali Linux is **not required**.

## Install

```bash
pkg update
pkg install git python -y
git clone https://github.com/ras806790-gif/Xosint.git
cd Xosint
chmod +x install.sh
./install.sh
```

## Usage

```bash
python xosint.py
```

Or specify a username:

```bash
python xosint.py example_username
```

Reports are saved in the current folder, e.g. `xosint_example_username_20261013_120000.txt`.

## Status labels

| Status | Meaning |
|---|---|
| `POTENTIAL` | URL responded successfully; verify manually. |
| `NOT DETECTED` | Site returned HTTP 404; this does not prove no account exists. |
| `UNKNOWN` | Response may indicate a block, rate limit, or uncertain result. |
| `ERROR` | Network, DNS, TLS, or timeout error. |

## Project structure

```text
Xosint/
├── .github/workflows/python-check.yml
├── docs/SAFETY.md
├── xosint/__init__.py
├── .gitignore
├── LICENSE
├── README.md
├── install.sh
├── requirements.txt
└── xosint.py
```

## Responsible use
Use only for lawful research of public information. Respect website terms, rate limits, and privacy. Do not use the tool to harass, stalk, dox, or target anyone. Xosint does not access private accounts, passwords, or hidden data.

See [Safety notes](docs/SAFETY.md).

## inspired

https://github.com/sherlock-project/sherlock

## SUPPORT DEVELOPER
TIKTOK 
titok.com/@rasyafunix               

INSTAGRAM 
Instagram.com/@rasyahgh

TELEGRAM
t.me/roxinih


## Contributing
<img src="assets/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f26636f6c756d6e733d3235266d61783d313030303026267265706f3d736865726c6f636b2d70726f6a6563742f736865726c6f636b.svg" alt="Xosint Logo" width="500">

## License
MIT. See [LICENSE](LICENSE).
