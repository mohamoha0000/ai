from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import urllib.request

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # استرداد URL من الطلب
            url = self.path
            print(f"Proxying request to: {url}")
            
            # فتح اتصال بالوجهة
            with urllib.request.urlopen(url) as response:
                self.send_response(response.getcode())
                for header, value in response.getheaders():
                    self.send_header(header, value)
                self.end_headers()
                self.wfile.write(response.read())
        except Exception as e:
            self.send_error(500, f"Error: {e}")

    def do_POST(self):
        self.send_error(405, "POST method not supported by this proxy.")

# تشغيل السيرفر
def run_proxy_server(port=5000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, ProxyHandler)
    print(f"Proxy server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_proxy_server()
