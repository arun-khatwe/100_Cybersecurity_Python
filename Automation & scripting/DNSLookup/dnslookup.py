import dns.resolver

def get_dns_records(domain):
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
    
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"\n[+] {record} Records:")
            for rdata in answers:
                print(f"    {rdata.to_text()}")
        except Exception as e:
            print(f"[-] {record} lookup failed: {e}")

if __name__ == "__main__":
    domain = input("Enter domain name: ")
    get_dns_records(domain)
