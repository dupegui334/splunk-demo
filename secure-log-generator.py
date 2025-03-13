import random
import time
import os
from faker import Faker

fake = Faker()

# Predefined lists of users and IP addresses to repeat between them
usernames = [
    "admin", "alice", "david_lopez", "guest", "root", 
    "david_upegui", "bob_smith", "bob_dylan", "george_harrison", "david_lee", 
    "mary_white", "travis_pastrana", "susan_clark", "clark_kent", "lucy_walker"
]

# Possible events and severity levels
events = ["Failed Login", "Successful Login", "File Access Denied", "Permission Change"]
severities = ["INFO", "WARNING", "CRITICAL"]


def read_ips_from_file(filename="ips.txt"):
    with open(filename, 'r') as file:
        ips = file.readlines()
    # Remove any extra newlines or spaces
    ips = [ip.strip() for ip in ips]
    return ips

# Load IP addresses from the file
ip_addresses = read_ips_from_file()

# Possible events and severity levels
events = ["Failed Login", "Successful Login", "Privilege Escalation", "File Access Denied", "Permission Change"]
severities = ["INFO", "WARNING", "CRITICAL"]

def generate_secure_log_entry():
    # Random timestamp for 2025
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(random.randint(1672531200, 1735689600)))  # Unix timestamps for 2025
    
    # Randomly pick a user and IP from predefined lists (repeatable)
    user = random.choice(usernames)
    ip_address = random.choice(ip_addresses)
    
    event_type = random.choice(events)  # Random event
    # Event-specific information
    if event_type == "Failed Login":
        reason = random.choice(["Incorrect password", "Account locked", "Too many attempts"])
        additional_info = f"Reason: {reason}"
        severity = "WARNING"
    elif event_type == "Privilege Escalation":
        new_role = random.choice(["root", "admin", "superuser"])
        additional_info = f"New Role: {new_role}"
        severity = "CRITICAL"
    elif event_type == "Successful Login":
        additional_info = f"User-Agent: {fake.user_agent()}"
        severity = "INFO"
    elif event_type == "File Access Denied":
        file = random.choice(["/etc/passwd", "/etc/shadow", "/home/user/data.txt"])
        additional_info = f"File: {file}"
        severity = "WARNING"
    elif event_type == "Permission Change":
        permission = random.choice(["read", "write", "execute"])
        additional_info = f"Permission: {permission}"
        severity = "CRITICAL"

    # Format log entry
    log_entry = f'{timestamp} - {event_type} - User: {user} - Source IP: {ip_address} - {additional_info} - Severity: {severity}\n'
    return log_entry

def generate_secure_log_file(file_name, num_entries=100):
    # Create directory if it doesn't exist
    directory = os.path.dirname(file_name)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_name, 'w') as f:
        for _ in range(num_entries):
            f.write(generate_secure_log_entry())

# Generate a secure log file with 2000 entries
generate_secure_log_file('host1/secure.log', 2000)
generate_secure_log_file('host2/secure.log', 2000)