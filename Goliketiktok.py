import requests,os,time
from time import sleep
banner = """
          \033[1;35m████████╗░█████╗░████████╗
          \033[1;34m╚══██╔══╝██╔══██╗ ╚══██╔══╝
          \033[1;35m   ██║   ██║  ╚═╝    ██║
          \033[1;36m   ██║   ██║  ██     ██║
          \033[1;32m   ██║   ╚█████╔╝    ██║
          \033[1;34m   ╚═╝    ╚════╝     ╚═╝

                      \033[1;36m████████╗  ████╗  █████╗ ██╗
                      \033[1;35m╚══██╔══╝██╔══██╗██╔══██╗██║
                      \033[1;33m   ██║   ██║  ██║██║  ██║██║
                      \033[1;32m   ██║   ██║  ██║██║  ██║██║
                      \033[1;34m   ██║   ╚█████╔╝╚█████╔╝███████╗
                      \033[1;36m   ╚═╝    ╚════╝  ╚════╝ ╚══════╝
\033[1;35m═════════════════════════════════════════════════════════════
\033[1;36m@COPYRIGHT : Thành Chần 🤡
\033[1;34mZalo : 0335021778 💍
\033[1;35mNhóm Zalo : https://zalo.me/g/drghio579
\033[1;35m═════════════════════════════════════════════════════════════"""
os.system("clear")
for x in banner:
  print(x,end = "")
  sleep(0.001)
print("")    
try:
  Authorization = open("Authorization.txt","x")
  t = open("token.txt","x")
except:
  pass
Authorization = open("Authorization.txt","r")
t = open("token.txt","r")
author = Authorization.read()
token = t.read()
if author == "":
  author = input("\033[1;36mNhập Authorization : ")
  token = input("\033[1;36mNhập T : ")
  Authorization = open("Authorization.txt","w")
  t = open("token.txt","w")
  Authorization.write(author)
  t.write(token)
else:
  select = input("\033[1;33mBạn có muốn đổi acc golike???(enter để bỏ qua,nhập Authorization acc khác để đổi) : ")
  if select != "":
    author = select
    token = input("\033[1;36mNhập T : ")
    Authorization = open("Authorization.txt","w")
    t = open("token.txt","w")
    Authorization.write(author)
    t.write(token)
Authorization.close()
t.close()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}


def chonacc():
  json_data = {}

  response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers, json=json_data).json()
  return response
def nhannv(account_id):

  params = {
    'account_id': account_id,
    'data': 'null',
  }

  json_data = {}

  response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',params=params,headers=headers,json=json_data,).json()
  return response
def hoanthanh(ads_id,account_id):
  json_data = {
    'ads_id': ads_id,
    'account_id': account_id,
    'async': True,
    'data': None,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
    headers=headers,
    json=json_data,
  ).json()
  return response
def baoloi(ads_id,object_id,account_id,loai):
  json_data1 = {
    'description': 'Tôi đã làm Job này rồi',
    'users_advertising_id': ads_id,
    'type': 'ads',
    'provider': 'tiktok',
    'fb_id': account_id,
    'error_type': 6,
  }

  response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1).json()

  json_data = {
    'ads_id': ads_id,
    'object_id': object_id,
    'account_id': account_id,
    'type': loai,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
    headers=headers,
    json=json_data,
  ).json()  
chontktiktok = chonacc()  
def dsacc():
  if(chontktiktok["status"]!=200):
    print("\033[1;34mAuthorization hoặc T sai hãy nhập lại!!!")
    quit()
  print("\033[1;33m═════════════════════════════════════════════════════════════")
  for i in range(len(chontktiktok["data"])):
    print(f'\033[1;36m`✯ {i+1} ✈ ● {chontktiktok["data"][i]["nickname"]} ●')
  print("\033[1;33m═════════════════════════════════════════════════════════════")   
dsacc() 
while True:
  try:
    luachon = int(input("\033[1;35mChọn acc để làm nhiệm vụ : "))
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách,Hãy Nhập Lại : "))
    account_id = chontktiktok["data"][luachon - 1]["id"]
    break  
  except:
    print("\033[1;35mSai định dạng!!!") 
while True:
  try:
    delay = int(input("\033[1;36mNhập thời gian làm job : "))
    break
  except:
    print("\033[1;31mSai định dạng!!!")
while True:
  try: 
    doiacc = int(input("\033[1;36mSau bao nhiêu job fail thì yêu cầu đổi acc tiktok (không muốn thì cứ nhập 1 số siêu to khổng lồ) : "))
    break
  except:
    print("\033[1;31mNhập vào 1 số!!!")    
os.system("clear")    
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""
os.system("clear")
for x in banner:
  print(x,end = "")
  sleep(0.001)
print("")
while True:
  if checkdoiacc == doiacc:
    dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
    print(f"\033[1;36mCác acc tiktok {dsaccloi} có vẻ gặp vấn đề nên đổi acc chạy đe")
    dsacc()
    while True:
      try:
        luachon = int(input("\033[1;35mChọn acc để làm nhiệm vụ : "))
        while luachon > len((chontktiktok)["data"]):
          luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách,Hãy Nhập Lại : "))
        account_id = chontktiktok["data"][luachon - 1]["id"]
        checkdoiacc = 0
        break  
      except:
        print("\033[1;35mSai định dạng!!!")
  print("                                     ",end = "\r") 
  print("\033[1;33mĐang tìm chốp:))",end = "\r")        
  while True:
    try:  
      nhanjob = nhannv(account_id)
      break
    except:
      pass
  if(nhanjob["status"] == 200):
    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    if(nhanjob["data"]["type"] != "follow"):
      baoloi(ads_id,object_id,account_id,nhanjob["data"]["type"])
      continue
    os.system(f"termux-open-url {link}")
    for i in range(delay,-1,-1):
      print('                                             ',end = '\r')
      for j in ['','.','..','...']:
        print("\033[1;36m"+f"Bạn Còn {i} Giây Để Làm Nhiệm Vụ{j}",end ='\r')
        time.sleep(1/4)
    print("                                                ",end = "\r")    
    print("\033[1;35mĐợi xíu đang nhận tiền:>",end = "\r")
    while True:    
      try:    
        nhantien = hoanthanh(ads_id,account_id)
        break
      except:
        pass
    if(nhantien["status"] == 200):
      dem += 1
      tien = nhantien["data"]["prices"]
      tong += tien
      local_time = time.localtime()
      hour = local_time.tm_hour
      minute = local_time.tm_min
      second = local_time.tm_sec
      h = hour
      m = minute
      s = second
      if(hour < 10):
        h = "0"+str(hour)
      if(minute < 10):
        m = "0"+str(minute)
      if(second < 10):
        s = "0"+str(second)
      chuoi = f"\033[1;32m✯ {dem} ✈ \033[1;33mSuccess ●\033[1;34m {nhantien['data']['type']} ●\033[1;35m {h}:{m}:{s} ● \033[1;36m[+{tien}] ₫ ✈ \033[1;32mTổng : {tong} VNĐ"  
      print("                                                    ",end = "\r")
      # for x in chuoi:
      #   print(x,end = "")
      #   sleep(0.1)
      # print("")  
      print(chuoi)    
      checkdoiacc = 0  
    else:
      #print(nhantien)
      while True:
        try:  
          baoloi(ads_id,object_id,account_id,nhanjob["data"]["type"])
          print("                                              ",end = "\r")
          print("\033[1;36mBỏ Qua Job!!!",end = "\r")
          sleep(1)
          checkdoiacc+=1
          break
        except:
          qua = 0
          pass

