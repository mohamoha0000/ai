import requests
from urllib.parse import urlparse
import http.client
import time
import socket
def test_proxy(url, proxy_host, proxy_port):
    # Parse the URL to extract components
    parsed_url = urlparse(url)
    
    try:
        # Create an HTTP connection using the proxy
        conn = http.client.HTTPSConnection(proxy_host, proxy_port)
        conn.set_tunnel(parsed_url.netloc)
        
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv) 7; Android 9; Nokia C2 Build/N398J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.7981.0.4881.42 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }

        # Send the request (HEAD request to check for redirects)
        conn.request('HEAD', parsed_url.path + '?' + parsed_url.query, headers=headers)
        response = conn.getresponse()

        # Check for redirection
        if response.status == 302:
            new_location = response.getheader('Location')
            print("Redirected to:", new_location)
            return True  # Proxy works, we detected a redirection
        elif response.status == 200:
            print("Successfully accessed:", url)
            return True  # Proxy works, request successful
        else:
            print(f"Unexpected response: {response.status}")
            return False  # Proxy works but with non-200 response
    except Exception as e:
        print(f"Error with proxy {proxy_host}:{proxy_port} - {e}")
        return False  # Proxy failed

    finally:
        conn.close()

# Test a list of proxies
def test_proxies(url, proxies_list):
    working_proxies = []

    for proxy in proxies_list:
        proxy_parts = proxy.split("://")[-1].split(":")
        if len(proxy_parts) == 2:
            proxy_host, proxy_port = proxy_parts
            proxy_port = int(proxy_port)  # Ensure port is an integer

            print(f"Testing proxy {proxy_host}:{proxy_port}...")
            success = test_proxy(url, proxy_host, proxy_port)
            
            if success:
                print(f"Proxy {proxy_host}:{proxy_port} works!")
                working_proxies.append((proxy_host, proxy_port))
            else:
                print(f"Proxy {proxy_host}:{proxy_port} failed.")

            time.sleep(1)  # Add delay between requests to avoid rate-limiting

    return working_proxies

# Example usage
if __name__ == "__main__":
    socket.setdefaulttimeout(3)
    search_url = "https://d.apkpure.com/b/APK/com.gameloft.android.ANMP.GloftA8HM?version=latest"
    
    # Get list of proxies (replace this with actual proxy list from your source)
    response = requests.get("https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&protocol=http&proxy_format=protocolipport&format=text&timeout=20000")
    proxies_list = response.text.split("\n")

    working_proxies = test_proxies(search_url, proxies_list)
    print(f"Working proxies: {working_proxies}")
