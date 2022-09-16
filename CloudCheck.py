import requests, ipaddress, dns.resolver

def get_cloudflare_ranges():
    try:
        r = requests.get('https://www.cloudflare.com/ips-v4')
        return r.text.split('\n')
    except requests.exceptions.RequestException:
        print('Failed to retrieve Cloudflare IP ranges - using a default (possibly outdated) list')
        fallback = [
        "103.21.244.0/22",
        "103.22.200.0/22",
        "103.31.4.0/22",
        "104.16.0.0/12",
        "108.162.192.0/18",
        "131.0.72.0/22",
        "141.101.64.0/18",
        "162.158.0.0/15",
        "172.64.0.0/13",
        "173.245.48.0/20",
        "188.114.96.0/20",
        "190.93.240.0/20",
        "197.234.240.0/22",
        "198.41.128.0/17"
        ]
        return [fallback]

cloudflare_subnets = [ipaddress.ip_network(ip_range) for ip_range in get_cloudflare_ranges()]

def is_cloudflare_ip(ip):
    for cloudflare_subnet in cloudflare_subnets:
        if cloudflare_subnet.overlaps(ipaddress.ip_network(ip)):
            return True
    return False

def is_valid_domain(domain):
    try:
        dns.resolver.resolve(domain, 'A')
        return True
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        return False

def uses_cloudflare(domain):
    if is_valid_domain(domain):
        answers = dns.resolver.resolve(domain, 'A')

        for answer in answers:
            if is_cloudflare_ip(answer):
                return True
        return False
    else:
        return 'Invalid domain' 

print(uses_cloudflare('redditthrowaway.xyz'))