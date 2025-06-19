import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlencode
import ipaddress
from urllib.parse import urlparse
import ipaddress
import re
import json

# Function to get the length of the URL
def url_length(url):
    return len(url)

# Function to get the length of the hostname
def hostname_length(url):
    return len(urlparse(url).netloc)

# Function to check if the domain is an IP address
def having_ip_address(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)|'  # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}|'
        '[0-9a-fA-F]{7}', url)  # Ipv6
    if match:
        return 1
    else:
        return 0

# Function to get counts of specific characters in the URL
def get_counts(url):
    return [
        url.count('.'),      # Number of dots
        url.count('?'),      # Number of question marks
        url.count('&'),      # Number of and
        url.count('='),      # Number of equal to
        url.count('/'),      # Number of slashes
        url.count('www'),    
    
    ]
def count_com(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path + parsed_url.query + parsed_url.fragment
    
    # Exclude the first 'com' from the domain part
    domain_com_count = domain.count('com') - 1 if 'com' in domain else 0
    
    # Count 'com' occurrences in the path, query, and fragment
    path_com_count = path.count('com')
    
    # Total 'com' count excluding the first one in the domain
    total_com_count = domain_com_count + path_com_count
    
    return total_com_count

# Function to check if the URL uses a shortening service
def is_shortening_service(url):
    shortening_services = [
        "bit.ly", "goo.gl", "t.co", "tinyurl.com", "tr.im", "is.gd", "cli.gs", "yfrog.com",
        "migre.me", "ff.im", "tiny.cc", "url4.eu", "twit.ac", "su.pr", "twurl.nl", "snipurl.com",
        "short.to", "BudURL.com", "ping.fm", "post.ly", "Just.as", "bkite.com", "snipr.com",
        "fic.kr", "loopt.us", "doiop.com", "short.ie", "kl.am", "wp.me", "rubyurl.com", "om.ly",
        "to.ly", "bit.do", "t2mio.com", "lc.chat", "ouo.io", "qr.ae", "v.gd", "cutt.ly", "shorte.st",
        "x.co", "lnkd.in", "fb.me", "db.tt", "qr.net", "v.gd", "tr.im", "link.zip.net"
    ]
    hostname = urlparse(url).hostname
    return 1 if hostname in shortening_services else 0
    

# Function to extract features from a URL
def extract_features(url):
    features = []
    
    # Selected Features
    features.append(url_length(url))            # Length of URL
    features.append(hostname_length(url))       # Length of hostname
    features.append(having_ip_address(url))     # IP address usage
    
    counts = get_counts(url)
    features.extend(counts)                     # Adding counts of specific characters
    features.append(count_com(url))             #couting no.of com
    features.append(is_shortening_service(url)) # URL shortening service   
    return features

    