# CloudCheck

CloudCheck is a simple program that checks if a given website, or list of websites, use the cloudflare service or not.
###### CloudCheck is inspired by [christophetd's](https://github.com/christophetd) program [CloudFlair](https://github.com/christophetd/CloudFlair).

## Prerequisites

- python3+

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages from the `requirements.txt`.

```bash
> pip3 install -r requirements.txt
```

## Installation

Use `git clone` to download the repository to your local machine:

```bash
> git clone https://github.com/Pyenb/cloudcheck
```

## Usage

Open your download location and execute the script from a console window.

Execute the `cloudcheck.py`

```bash
> python cloudcheck.py

usage: cloudcheck.py [-h] [-u URL] [-f FILE] [-o]

Check if a given server / or list of servers uses the cloudflare service.

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     The domain to check
  -f FILE, --file FILE  Load a list of domains from a file.
  -o, --output          Output the websites using cloudflare to a file.
```

`URL` defines the website adress that you want to scan.\
`FILE` defines a file that you want to read and check if the given websites use cloudflare.\
`--output` outputs websites that use cloudflare to `cloudflare.txt`

The program will automatically remove anything before or after the URL, so `https://google.de/search?=abc` would become `google.de`

### Example with a single URL:

```bash
> python cloudcheck.py -u google.de

[!] google.de does not use cloudflare
```

### Example with a file:
The file has to be in a readable format (preferred `.txt`) and the websites need to be listed one below another. 

```bash
> python cloudcheck.py -f websites.txt

[!] google.de does not use cloudflare
[!] abc.xyz does not use cloudflare
[!] www.ebay.com does not use cloudflare
[*] realsite.com uses cloudflare
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Disclaimer
This repository is for research purposes only, the use of this code is your responsibility.

I take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again, ALL files available here are for EDUCATION and/or RESEARCH purposes ONLY.
