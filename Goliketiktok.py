import requests,os,time
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
\033[1;36mCode by : Thành Chần
\033[1;34mZalo : 0335021778
\033[1;35mNhóm Xàm xí,Báo lỗi : https://zalo.me/g/drghio579
\033[1;35m═════════════════════════════════════════════════════════════"""
os.system("clear")
print(banner)
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
if(chontktiktok["status"]!=200):
  print("\033[1;34mAuthorization hoặc T sai hãy nhập lại!!!")
  quit()
print("\033[1;33m═════════════════════════════════════════════════════════════")
for i in range(len(chontktiktok["data"])):
  print(f'\033[1;36m`[{i+1}]~ {chontktiktok["data"][i]["nickname"]}')
print("\033[1;33m═════════════════════════════════════════════════════════════")    
while True:
  try:
    luachon = int(input("\033[1;35mChọn acc để làm nhiệm vụ : "))
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách,Hãy Nhập Lại : "))
    break  
  except:
    print("\033[1;35mSai định dạng!!!")
account_id = chontktiktok["data"][luachon - 1]["id"]    
while True:
  try:
    delay = int(input("\033[1;36mNhập thời gian làm job : "))
    break
  except:
    print("\033[1;32mSai định dạng!!!")
os.system("clear")    
dem = 0
tong = 0
os.system("clear")
print(banner)
while True:
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
      h = local_time.tm_hour
      m = local_time.tm_min
      s = local_time.tm_sec 
      print("                                                 ",end = "\r")
      print(f'\033[1;32m`[{dem}]~ \033[1;33mSuccess |\033[1;34m {nhantien["data"]["type"]} |\033[1;35m {h}:{m}:{s} | \033[1;36m[+{tien}] ₫ => \033[1;32mTổng : {tong} VNĐ')
    else:
      #print(nhantien)
      while True:
        try:  
          baoloi(ads_id,object_id,account_id,nhanjob["data"]["type"])
          print("                                              ",end = "\r")
          print("\033[1;36mBỏ Qua Job!!!",end = "\r")
          break
        except:
          pass
        
