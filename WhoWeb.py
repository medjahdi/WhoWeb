import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import time
import sys

# Typing animation function
def type_with_animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)  
    print()

# Banner
banner = r'''
.-.
     .'   `.           --------------------------------
     :g g   :           | WhoWeB - Scanner - Scan Any web |
     : o     `.         |       @CODE BY @medjahdi             |
     :         ``.       --------------------------------
     :           `.
     :   :       .   `.
     :   :       ` . `.
      `.. :         `. ``;
         `:;         `:'
             :           `.
             `.           `.       .
               `'`'`'`---..,___`;.-'
'''

# Function to scan a website
def scan_website(url):
    try:
        # Send a GET request to the URL with a custom User-Agent and timeout
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract information from the website
            links = soup.find_all('a')
            type_with_animation(Fore.GREEN + f"Scanning {url}...")
            type_with_animation(Fore.WHITE + f"Links found: {len(links)}")
            for link in links:
                href = link.get('href')
                if href:  # Check if href is not None
                    type_with_animation(href)

            # Check for cookies
            cookies = response.cookies
            type_with_animation(Fore.CYAN + f"Cookies found: {len(cookies)}")  # Show number of cookies
            type_with_animation(Fore.CYAN + f"Cookies found: {cookies}")  # Show number of cookies

            # Get website IP and country
            ip_address = requests.get('https://api64.ipify.org').text
            type_with_animation(Fore.YELLOW + f"IP Address: {ip_address}")
            ip_info = requests.get(f'https://ipinfo.io/{ip_address}/json').json()
            type_with_animation(Fore.YELLOW + f"Country: {ip_info.get('country')}")

            # Find email addresses
            email_addresses = soup.find_all('a', href=lambda href: href and 'mailto:' in href)
            type_with_animation(Fore.MAGENTA + f"Email addresses found: {len(email_addresses)}")
            for email in email_addresses:
                type_with_animation(email.get('href').replace('mailto:', ''))

            # Check for Apache server
            server_header = response.headers.get('Server')
            if server_header and 'Apache' in server_header:
                type_with_animation(Fore.GREEN + "Apache server detected")
                
            # Check for PHP type
            if 'PHP' in response.text:
                type_with_animation(Fore.CYAN + "PHP detected")

            # Check for Google Analytics
            if 'Google Analytics' in response.text:
                type_with_animation(Fore.BLUE + "Google Analytics detected")


            # Check for frames
            frames = soup.find_all('frame')
            if frames:
                type_with_animation(Fore.MAGENTA + f"Frames found: {len(frames)}")

            # Check for uncommon headers
            uncommon_headers = [header for header in response.headers if 'X-' in header]
            if uncommon_headers:
                type_with_animation(Fore.YELLOW + "Uncommon headers found:")
                for header in uncommon_headers:
                    type_with_animation(f"{header}: {response.headers[header]}")  # Show header value

            # Extract and display additional information
            title = soup.title.string if soup.title else "No title found"
            type_with_animation(Fore.WHITE + f"Page Title: {title}")

            meta_tags = soup.find_all('meta')
            type_with_animation(Fore.WHITE + f"Meta tags found: {len(meta_tags)}")

             

        else:
            type_with_animation(Fore.RED + f"Failed to scan {url}. Status code: {response.status_code}")
    except requests.Timeout:
        type_with_animation(Fore.RED + "Request timed out.")
    except requests.ConnectionError:
        type_with_animation(Fore.RED + "Connection error occurred.")
    except Exception as e:
        type_with_animation(Fore.RED + f"An error occurred: {e}")

# Input from the user
if __name__ == "__main__":
    # Show banner
    print(banner)

    # Get the website URL from the user or command-line argument
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
    else:
        target_url = input("Enter the website URL to scan: ")

    # Ensure the URL has the correct scheme
    if not target_url.startswith(('http://', 'https://')):
        type_with_animation(Fore.RED + "URL must start with 'http://' or 'https://'.")
    else:
        # Show information message
        print(Fore.RED + "\n============ SHOW INFORMATION HERE =============")
        scan_website(target_url)
        type_with_animation(Fore.GREEN + "\n============ THANKS FOR USING MY TOOL =============")
