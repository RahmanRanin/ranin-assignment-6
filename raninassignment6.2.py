unique_hosts = set()

with open('mbox.txt', 'r') as file:
    for line in file:
        if line.startswith('From:'):
            email = line.split()[1]
            _, host = email.split('@')
            print(host)
            unique_hosts.add(host)

print(f"Number of unique hosts: {len(unique_hosts)}")
