from urllib.parse import urlparse
import http.client

url = "https://d.apkpure.com/b/APK/com.gameloft.android.ANMP.GloftA8HM?version=latest"
proxy_host = '178.48.68.61'
proxy_port = '18080'

# Parse the URL to extract components
parsed_url = urlparse(url)

# Establish the connection using the proxy
conn = http.client.HTTPSConnection(proxy_host, proxy_port)  # استخدم HTTPS إذا كان البروكسي يدعم ذلك
conn.set_tunnel(parsed_url.netloc)

headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv) 7; Android 9; Nokia C2 Build/N398J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.7981.0.4881.42 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

try:
    # Send the request
    conn.request('HEAD', parsed_url.path + '?' + parsed_url.query, headers=headers)
    response = conn.getresponse()

    # Check for 302 status
    if response.status == 302:
        new_location = response.getheader('Location')
        print("Redirected to:", new_location)
except Exception as e:
    print("An error occurred:", e)
finally:
    conn.close()
