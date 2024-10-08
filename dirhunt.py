#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :: dirhunt/dirhunt.py (https://github.com/Luunarr/dirhunt) ::
# :: by Lunar           (https://github.com/Luunarr)         ::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #

import requests
import time
import argparse
import logging
import socket
import os

# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #

from colorama import *
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #


# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #

init(autoreset=True)

# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #


# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #

black = Fore.BLACK
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
magenta = Fore.MAGENTA
cyan = Fore.CYAN
white = Fore.WHITE
gray = Fore.LIGHTBLACK_EX
lightyellow = Fore.LIGHTYELLOW_EX

# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #

reset = Style.RESET_ALL
bright = Style.BRIGHT

# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #

resu = f"{reset}{bright}{lightyellow}[{white}*{lightyellow}]{reset}"
tilde = f"{reset}{bright}{yellow}[{white}~{yellow}]{reset}"
plus = f"{reset}{bright}{green}[{white}+{green}]{reset}"
excla = f"{reset}{bright}{red}[{white}!{red}]{reset}"
info = f"{reset}{bright}{cyan}[{white}?{cyan}]{reset}"
inputt = f"{reset}{bright}{cyan}[{white}>{cyan}]{reset}"
s = f"{reset}{bright}{blue}[{white}/{blue}]{reset}"
ver = f"{reset}{bright}{red}[{white}dirhunt{gray}#{white}1.3{red}]{reset}"

# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #


# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #

asciiart = [
f"{bright}   {red}___{white}      _             {red}_  _{white}                     _    {reset}",
f"{bright}  {red}|   \ {white}   (_)      _ _  {red}| || |{white}   _  _    _ _     | |_  {reset}",
f"{bright}  {red}| |) |{white}   | |     | '_| {red}| __ |{white}  | {red}+{white}| |  | ' \    |  _|   {ver}{reset}",
f"{bright}  {red}|___/{white}   _|_|_   _|_|_  {red}|_||_|{white}   \_,_|  |_||_|   _\__|   {white}https://github.com/Luunarr/dirhunt{reset}",
f'{bright}{white}_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|{reset}',
f"""{bright}{white}"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'{reset}""",
f""
]

# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #


# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #

defpaths = [
    'admin/', 'login/', 'dashboard/', 'config/', 'db/', 'backup/',
    'robots.txt', '.env', '.git/', 'wp-admin/', 'phpinfo.php', 'index.php',
    'admin1/', 'admin2/', 'admin3/', 'administrator/', 'config.php',
    'wp-login.php', 'wp-content/', 'wp-includes/', 'server-status',
    'configurations/', 'settings/', 'private/', 'data/', 'uploads/',
    'cgi-bin/', 'backup.sql', 'test/', 'demo/', 'user/', 'access.log',
    'error.log', 'docs/', 'manual/', 'readme.txt', 'license.txt', 'change.log',
    'install.php', 'install/', 'maintenance/', 'sitemap.xml', 'temp/',
    'cache/', 'tmp/', 'log/', 'scripts/', 'images/', 'videos/', 'downloads/', 
    'source/', 'archive/', 'public/', 'admin_area/', 'admin-panel/',
    'admin-dashboard/', 'admin-settings/', 'admin-tools/', 'admin-console/',
    'database/', 'db-backup/', 'backup-files/', 'backup-folder/', 'logs/',
    'webmaster-tools/', 'tools/', 'support/', 'help/', 'faq/', 'contact/',
    'about/', 'terms/', 'privacy/', 'policy/', 'user-manual/', 'user-guide/',
    'user-docs/', 'user-help/', 'support-tickets/', 'support-docs/',
    'api/', 'api-docs/', 'api-v1/', 'api-v2/', 'api-testing/', 'api-support/',
    'app/', 'application/', 'site/', 'web/', 'frontend/', 'backend/',
    'public_html/', 'public-files/', 'site-files/', 'site-data/',
    'files/', 'system/', 'system-logs/', 'system-config/', 'system-backup/',
    'update/', 'updates/', 'update-files/', 'patch/', 'patches/',
    'version/', 'versions/', 'upgrade/', 'upgrade-files/', 'upgrade-tools/',
    'admin/login/', 'admin/config/', 'admin/settings/', 'admin/dashboard/',
    'login.php', 'config.inc.php', 'settings.php', 'settings.inc.php',
    'app/config/', 'app/settings/', 'app/data/', 'app/uploads/',
    'app/cache/', 'app/temp/', 'app/logs/', 'app/files/',
    'vendor/', 'node_modules/', 'public/assets/', 'public/uploads/',
    'public/cache/', 'public/temp/', 'public/logs/', 'public/files/',
    'private/config/', 'private/settings/', 'private/data/', 'private/uploads/',
    'private/cache/', 'private/temp/', 'private/logs/', 'private/files/',
    'tmpfiles/', 'tmp-data/', 'temporary/', 'interim/', 'processing/',
    'archives/', 'old/', 'previous/', 'history/', 'backups/',
    'assets/', 'resources/', 'storage/', 'media/', 'docs/api/',
    'docs/user/', 'docs/technical/', 'docs/developer/', 'docs/admin/',
    'media/images/', 'media/videos/', 'media/audio/', 'media/docs/',
    'files/private/', 'files/shared/', 'files/public/', 'tmp_files/',
    'cache_files/', 'data_files/', 'data/private/', 'data/shared/', 
    'data/public/', 'logs/system/', 'logs/error/', 'logs/access/', 
    'logs/debug/', 'logfiles/', 'system/configs/', 'system/files/', 
    'system/backups/', 'system/updates/', 'system/logs/', 'admin/backup/',
    'admin/archive/', 'admin/data/', 'admin/files/', 'admin/configs/',
    'admin/logs/', 'admin/temp/', 'admin/cache/', 'admin/uploads/',
    'api/staging/', 'api/production/', 'api/development/', 'api/documents/',
    'backend/config/', 'backend/logs/', 'backend/data/', 'backend/cache/',
    'backend/files/', 'backend/uploads/', 'backend/temp/', 'backend/backup/',
    'frontend/assets/', 'frontend/styles/', 'frontend/scripts/', 'frontend/images/',
    'frontend/videos/', 'frontend/docs/', 'frontend/data/', 'frontend/cache/',
    'frontend/temp/', 'frontend/logs/', 'uploads/temp/', 'uploads/private/',
    'uploads/public/', 'uploads/shared/', 'static/', 'static/assets/',
    'static/images/', 'static/videos/', 'static/docs/', 'static/data/',
    'temp_files/', 'logs/debug/', 'private/temp/', 'public_html/assets/',
    'public_html/cache/', 'public_html/logs/', 'app/backups/', 'system/maintenance/',
    'admin/maintenance/', 'uploads/temporary/', 'uploads/private/', 
    'uploads/public/', 'uploads/shared/', 'system/temp/', 'system/cache/',
    'docs/updates/', 'docs/api/v1/', 'docs/api/v2/', 'docs/user-guide/',
    'docs/technical/', 'media/audio/', 'media/pictures/', 'media/docs/',
    'media/videos/', 'media/images/', 'static/images/', 'static/videos/',
    'static/audio/', 'static/docs/', 'data/archives/', 'data/history/',
    'data/backups/', 'files/backups/', 'files/temp/', 'files/archive/',
    'files/cache/', 'backend/archives/', 'backend/temp/', 'backend/history/',
    'frontend/updates/', 'frontend/archives/', 'frontend/temp/',
    'uploads/archive/', 'uploads/cache/', 'uploads/data/', 'uploads/private/'
]



# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #


# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #

def slogging(logfile):
    script = os.path.dirname(os.path.abspath(__file__))
    logfilep = os.path.join(script, logfile)
    logging.basicConfig(filename=logfilep, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Logging started")
    
# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #


# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #

def scan(url, paths, threads=10, color=True, user_agent=None, retries=3, live=False):

    domain = url.split("//")[-1].split("/")[0]
    
    try:
        ip = socket.gethostbyname(domain)
        print(f"{resu} {bright}{white}Domain: {domain} | IP Address: {ip}{reset}")
    except socket.gaierror:
        print(f"{excla} {bright}{red}Unable to resolve domain: {domain}{reset}")
        ip = None

    logging.info(f"Scanning domain: {domain} | IP Address: {ip}")

    if user_agent:
        headers = {'User-Agent': user_agent}
    else:
        headers = {}

    print(f"{resu} {bright}{white}Starting directory scan on URL: {url}{reset}")
    
    
    logging.info(f"Starting directory scan on URL: {url}")

    statuscounts = {}

    def cpath(path):
        fullurl = urljoin(url, path)
        attempt = 1
        while attempt <= retries:
            try:
                response = requests.get(fullurl, headers=headers, timeout=10)
                code = response.status_code
                if code in statuscounts:
                    statuscounts[code] += 1
                else:
                    statuscounts[code] = 1

                if response.status_code == 200:
                    return (fullurl, response.status_code, response.elapsed.total_seconds())
            except requests.RequestException as e:
                logging.error(f"Request exception for {fullurl}: {e}")
            attempt += 1
        return None

    starttime = time.time()
    results = []

    totalpaths = len(paths)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(cpath, path): path for path in paths}

        if live:
            print(f"\n{s} {bright}{white}Discovered URLs:{reset}")
            for future in futures:
                result = future.result()
                if result:
                    results.append(result)
                    print(f"{plus} {bright}{white}{result[0]} ")  
                    logging.info(f"Discovered URL: {result[0]}")
        else:
            for future in tqdm(futures, total=totalpaths, desc=f"{inputt} {bright}{white}Scanning{reset}", unit=f" {bright}{cyan}directory{reset}", colour="cyan"):
                result = future.result()
                if result:
                    results.append(result)

    etime = time.time()
    ttime = etime - starttime
    urlspersec = len(paths) / ttime if ttime > 0 else 0

    if not live: 
        print(f"\n{s} {bright}{white}Discovered URLs:{reset}")
        for result in results:
            print(f"{plus} {bright}{white}{result[0]} ")
            logging.info(f"Discovered URL: {result[0]}")

    print(f"\n{resu} {bright}{white}Scan completed in {ttime:.2f} seconds.{reset}")
    print(f"{resu} {bright}{white}URLs tested per second: {urlspersec:.2f}{reset}")
    print(f"{resu} {bright}{white}Total URLs found: {len(results)}{reset}\n")

    print(f"{resu} {bright}{white}HTTP status codes summary:{reset}")
    for code, count in sorted(statuscounts.items(), key=lambda item: item[1], reverse=True):
        print(f"{plus} {bright}{white}Status Code {code}: {count} times{reset}") 
    
# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #


# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in asciiart:
        print(line)
        time.sleep(0.02)
        
# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #


# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #

def main():
    parser = argparse.ArgumentParser(
        description=f"{info} {bright}Powerful Directory Scanner - A tool to scan directories{reset}",
    )

    parser.add_argument(
        "url", 
        help=f"The base URL to scan. Example: {white}http://example.com{reset}"
    )

    parser.add_argument(
        "-p", "--paths", 
        help=f"Path to a custom file that contains a list of paths to test.{reset}",
        type=str
    )

    parser.add_argument(
        "-t", "--threads", 
        help=f"Number of threads to use for scanning. Default is {white}10.{reset}",
        type=int, 
        default=10
    )

    parser.add_argument(
        "-m", "--mode", 
        help=f"Specify the scan mode. Choose between {white}'default'{reset} or {white}'custom'{yellow}.{reset}", 
        choices=['default', 'custom'], 
        default='default'
    )

    parser.add_argument(
        "--clear", 
        help=f"Clear the screen before displaying the scan results.{reset}", 
        action="store_true"
    )

    parser.add_argument(
        "--user-agent", 
        help=f"Specify a custom {white}User-Agent{reset} header for requests.{reset}", 
        type=str
    )

    parser.add_argument(
        "--retries", 
        help=f"Number of retry attempts for failed requests. Default is {white}3{reset}.{reset}",
        type=int, 
        default=3
    )

    parser.add_argument(
        "--logfile", 
        help=f"File to log the scan results. Default is {white}scan.log{reset}.{reset}", 
        type=str, 
        default='scan.log'
    )

    parser.add_argument(
        "--live", 
        help=f"Enable live mode to display valid URLs as they are found.{reset}", 
        action="store_true"
    )

    for line in asciiart:
        print(line)
        time.sleep(0.02)

    args = parser.parse_args()

    if args.clear:
        clear()

    slogging(args.logfile)

    if args.mode == 'custom' and args.paths:
        try:
            with open(args.paths, 'r') as f:
                paths = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"{excla} {bright}{red}File {args.paths} not found.{reset}")
            return
    else:
        paths = defpaths

    scan(args.url, paths, threads=args.threads, user_agent=args.user_agent, retries=args.retries, live=args.live)
    
# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #


# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #

if __name__ == "__main__":
    main()
    
# ~ _________________________________ https://github.com/Luunarr/dirhunt _________________________________ ~ #
