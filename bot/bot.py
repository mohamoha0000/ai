
from func import *
import t
search_query ="https://d.apkpure.com/b/APK/com.gameloft.android.ANMP.GloftA8HM?version=latest"# request.args.get('n', default='no')
phone = "212646576115"
response = requests.get("https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&protocol=http&proxy_format=protocolipport&format=text&timeout=20000")
proxies_list = response.text.split("\n")

for x in proxies_list:
    t.co(x)
    """
    result=getsize(search_query,x)
    print(result)
    if "winudf" in str(result[1]):
        if result[0]<100:
                            send_message(phone,"ok send...")
                            sendf2(phone,result[1])
        else:
                            send_message(phone,"لايمكن تنزيل  ملف كبير اكتر من 100 ميغا")
        exit()
"""