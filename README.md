# OSINT Checker

OSINT Checker is a modular Python tool for website and domain reconnaissance.

## Features

- HTTP headers analysis
- DNS records lookup
- WHOIS lookup
- SSL certificate info
- Tech stack detection
- Subdomain discovery
- Basic crawling
- Wayback Machine lookup
- Organization and people intelligence
- Google dorks generation

## Installation

```bash
Windows

git clone https://github.com/its-roxio/OSINT_recon.git
cd OSINT_recon
py -m pip install -r requirements.txt
py -m pip install dnspython

Linux

sudo apt update
sudo apt install -y git python3 python3-pip

cd ~
git clone https://github.com/its-roxio/OSINT_recon.git
cd OSINT_recon

python3 -m pip install --user -r requirements.txt
python3 -m pip install --user dnspython
```

## Usage

```bash
Windows 

cd OSINT_recon
python -m osint_recon --url example.com --full

Linux

python3 -m osint_recon --url google.com --full
```

## Notes

Use only on targets you are authorized to analyze.
