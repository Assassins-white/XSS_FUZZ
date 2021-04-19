# coding:utf-8
import requests
import sys
from colorama import Fore, init


def main():
    init(autoreset=True)
    if len(sys.argv) <= 1:
        print("请设置", Fore.RED + "XSSFUZZ",
              "关键字" "\n例如: python3 xss.py https://www.baidu.com/?s=" + Fore.RED + "XSSFUZZ")
    else:
        # cookie = '''PHPSESSID=a37begqef46ehtmmm7g94lr56b;security=low'''  # 设置cookie

        header = {
            # 'Cookie': cookie, # 设置cookie
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
        }

        with open(r'xss.txt', 'r') as f:  # xss payload
            for xss in f.readlines():
                if 'XSSFUZZ' in sys.argv[1]:
                    xss_payload = sys.argv[1].replace('XSSFUZZ', xss.strip())  # 把XSSFUZZ替换成payload
                    request = requests.get(url=xss_payload, headers=header)
                    if xss.strip() in request.text:
                        print(Fore.GREEN + '[+]成功  --> ' + request.url)
                    else:
                        print(Fore.RED + '[-]失败  --> ' + request.url)

                else:
                    print("请设置", Fore.RED + "XSSFUZZ",
                          "关键字" "\n例如: python3 xss.py https://www.baidu.com/?s=" + Fore.RED + "XSSFUZZ")
                    break


if __name__ == '__main__':
    main()
