import random
import string
import subprocess
import os
import time

from ping3 import ping

def generate_random_domain(length):
    chars = string.ascii_lowercase + string.digits
    domain = ''.join(random.choice(chars) for _ in range(length))
    return domain

def is_pingable(domain):
    return ping(domain) is not None

def main():
    min_length = 3
    max_length = 20
    num_domains = 100  # You can adjust this number as needed

    print("Generating and testing domains...")
    valid_domains = []
    for i in range(num_domains):
        domain_length = random.randint(min_length, max_length)
        domain = generate_random_domain(domain_length) + ".com"
        
        print(f"Testing domain {i + 1}/{num_domains}: {domain}")
        if is_pingable(domain):
            valid_domains.append(domain)

        # Add a short delay between tests to avoid rate limiting (optional)
        time.sleep(0.2)

    with open("website.txt", "w") as file:
        for domain in valid_domains:
            file.write(domain + "\n")

    print(f"\n{len(valid_domains)} pingable domain(s) exported to 'website.txt'.")

if __name__ == "__main__":
    main()

