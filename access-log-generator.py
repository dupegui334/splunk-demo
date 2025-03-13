import random
import time
import os
from faker import Faker

fake = Faker()

def load_ip_addresses(filename='ips.txt'):
    try:
        with open(filename, 'r') as f:
            return [ip.strip() for ip in f.readlines() if ip.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please create it with IP addresses.")
        exit(1)

ip_addresses = load_ip_addresses()

def generate_log_entry():
    ip_address = random.choice(ip_addresses)
    timestamp = time.strftime('%d/%b/%Y:%H:%M:%S +0000', time.gmtime(random.randint(1609459200, 1672444800)))
    method = random.choice(['GET', 'POST', 'PUT', 'DELETE'])
    endpoint = f"/api/v1/{random.choice(['users', 'products', 'orders'])}"
    status_code = random.choice([200, 201, 400, 401, 404, 500])
    response_size = random.randint(100, 5000)
    user_agent = fake.user_agent()

    log_entry = f'{ip_address} - - [{timestamp}] "{method} {endpoint} HTTP/1.1" {status_code} {response_size} "-" "{user_agent}"\n'
    return log_entry

def generate_log_file(file_name, num_entries=100):
    # Create directory if it doesn't exist
    directory = os.path.dirname(file_name)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        
    with open(file_name, 'w') as f:
        for _ in range(num_entries):
            f.write(generate_log_entry())

# Generate a log file with 2000 entries
generate_log_file('host1/access.log', 2000)
generate_log_file('host2/access.log', 2000)