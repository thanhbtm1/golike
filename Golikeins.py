import requests,os,time
banner = """
          \033[1;36m████████╗░█████╗░████████╗
          \033[1;34m╚══██╔══╝██╔══██╗ ╚══██╔══╝
          \033[1;35m   ██║   ██║  ╚═╝    ██║
          \033[1;36m   ██║   ██║  ██     ██║
          \033[1;32m   ██║   ╚█████╔╝    ██║
          \033[1;31m   ╚═╝    ╚════╝     ╚═╝

                      \033[1;36m████████╗  ████╗  █████╗ ██╗
                      \033[1;35m╚══██╔══╝██╔══██╗██╔══██╗██║
                      \033[1;33m   ██║   ██║  ██║██║  ██║██║
                      \033[1;32m   ██║   ██║  ██║██║  ██║██║
                      \033[1;34m   ██║   ╚█████╔╝╚█████╔╝███████╗
                      \033[1;36m   ╚═╝    ╚════╝  ╚════╝ ╚══════╝
\033[1;32m═════════════════════════════════════════════════════════════  
\033[1;36mCOPYRIGHT : Thành Chần
\033[1;36mZalo : 0335021778
\033[1;36mNhóm Xàm xí,Báo lỗi : https://t.me/tanhuwu
\033[1;32m═════════════════════════════════════════════════════════════"""
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
  
  response = requests.get('https://gateway.golike.net/api/instagram-account', headers=headers, json=json_data).json()
  return response
def nhanjob(instagram_account_id):
  params = {
    'instagram_account_id': instagram_account_id,
    'data': 'null',
  }
  
  json_data = {}
  
  response = requests.get(
      'https://gateway.golike.net/api/advertising/publishers/instagram/jobs',
      params=params,
      headers=headers,
      json=json_data,
  ).json()
  return response
def hoanthanh(instagram_users_advertising_id,instagram_account_id,):
  json_data = {
    'instagram_users_advertising_id': instagram_users_advertising_id,
    'instagram_account_id': instagram_account_id,
    'async': True,
    'data': None,
  }
  
  response = requests.post(
      'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs',
      headers=headers,
      json=json_data).json()
  return response    
def boqua(users_advertising_id,instagram_account_id,object_id,theloai):
  
  json_data1 = {
      'description': 'Tôi đã làm Job này rồi',
      'users_advertising_id': users_advertising_id,
      'type': 'ads',
      'provider': 'instagram',
      'fb_id': instagram_account_id,
      'error_type': 6,
  }
  
  response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)
  json_data2 = {
    'ads_id': users_advertising_id,
    'account_id': instagram_account_id,
    'object_id': object_id,
    'type': theloai,
   }
  
  response1 = requests.post(
      'https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs',
      headers=headers,
      json=json_data2,
  ).json()   
  return response1
def autofl(link,cookieig):
  
  headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    'dpr': '3.29834',
    'origin': 'https://www.instagram.com',
    #'referer': 'https://www.instagram.com/criticalentrepreneur/',
    'cookie': cookieig,
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'viewport-width': '891',
    'x-asbd-id': '129477',
    'x-csrftoken': cookieig.split('csrftoken=')[1].split(';')[0],
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3bdSdQiCaa22Y3QSBmUIgKdUDw-D6gt560myUWTlsFRGhd',
    'x-instagram-ajax': '1010814280',
    'x-requested-with': 'XMLHttpRequest',
  }
  id = requests.get(url = link,headers=headers).text.split("profilePage_")[1].split('"')[0]
  data = {
    'container_module': 'profile',
    'nav_chain': 'PolarisProfileNestedContentRoot:profilePage:1:via_cold_start',
    'user_id':f'{id}',
  }
  response = requests.post(
    f'https://www.instagram.com/api/v1/friendships/create/{id}/',
    headers=headers,
    data=data).json()
  return response
chontkins = chonacc()
listacc = []
for i in range(len(chontkins["data"])):
  name = chontkins["data"][i]["instagram_username"]
  listacc.append(name)
  try:
    mo = open(f"{name}.txt","x")
  except:
    pass
os.system("clear")  
print(banner)
print("\033[1;32m═════════════════════════════════════════════════════════════")
for i in range(len(listacc)):
  mo = open(f"{listacc[i]}.txt","r")
  if(mo.read() == ""):
    print(f"\033[1;31m{i} : {listacc[i]} ~ Chưa có cookie!!!")
  else:
    print((f"\033[1;36m{i} : {listacc[i]} ~ Đã có cookie \033[1;32m✓"))
print("\033[1;32m═════════════════════════════════════════════════════════════")    
while True:
  try:
    nhap = int(input("\033[1;35mNhập tài khoản muốn thêm cookie(enter để dừng nhập) : "))
    mo = open(f"{listacc[nhap]}.txt","w")
    cookieig = input(f"\033[1;34mNhập cookie cho acc {listacc[nhap]} : ")
    mo.write(cookieig)
  except:
    break    
g = 0
tien = 0
dem = 0
tong = 0
loi = 0
accloi = []
while True:
  try:
    delay = int(input("\033[1;35mNhập delay giữa các job : "))
    break
  except:
    print("\033[1;34mSai định dạng!!!")
while True:
  mo = open(f"{listacc[g]}.txt","r")
  cookieig = mo.read()
  mo.close()
  instagram_account_id = chontkins["data"][g]["id"]
  while True:
    try:
      get = nhanjob(instagram_account_id)
      print("                                       ",end = "\r")        
      print("\033[1;36mĐang nhận job và follow",end = "\r")
      idjob = get["data"]["id"]  
      link = get["data"]["link"]
      object_id = get["data"]["object_id"]        
      break
    except:
      pass
  if(get["status"]==200):  
    if(get["lock"]["type"] == "follow"):
      pass
    else:
      boqua(idjob,instagram_account_id,object_id,"like")
      continue        
    try:
      lam = autofl(link,cookieig)
      if(lam["status"] == "fail"):
        g+=1
        if(g >= len(listacc)):
          print("\033[1;34mTất cả các acc đều không làm đc job hãy kiểm tra lại!!!")
          quit()
        print(f"\033[1;36mAcc •{listacc[g]}• đã bị instagram hạn chế follow do spam")
        print(f"\033[1;32mĐang đổi sang acc •{listacc[g]}• để làm nhiệm vụ!!!")
        time.sleep(1)
        print(f"\033[1;34mĐã chuyển sang acc {listacc[g]}!!!")
        boqua(idjob,instagram_account_id,object_id,"follow")
        continue
    except:
      skip = boqua(idjob,instagram_account_id,object_id,"follow")
      print("                                  ",end = "\r")  
      print("\033[1;31mBỏ Qua Job !!!",end = "\r")        
      loi+=1 
      if(loi >= 5):
        g+=1
        if g >= len(listacc):
          print("\033[1;31m1 số acc sau đây có thể bị checkpoin nên vào xem thử nhé : ")
          for x in accloi:
            print(f"\033[1;36m{x}")
          quit()
        print(f"\033[1;31mAcc •{listacc[g-1]}• Có lẽ đã xảy ra vấn đề nên khuyên bạn vào xem thử nhé!!!")
        accloi.append(listacc[g-1])
        print(f"\033[1;35mĐã đổi sang acc •{listacc[g]}• để làm nhiệm vụ!!!")
        boqua(idjob,instagram_account_id,object_id,"follow")
        continue
      continue          
    loi = 0  
    nhantien = hoanthanh(idjob,instagram_account_id)
    if nhantien["status"] == 200:
      dem+=1
      tien = nhantien["data"]["prices"]
      tong+=tien
      local_time = time.localtime()
      h = local_time.tm_hour
      m = local_time.tm_min
      s = local_time.tm_sec 
      print("                                                 ",end = "\r")
      print(f"\033[1;36m`[{dem}]~\033[1;35m| FOLLOW |\033[1;31m SUCCESS |\033[1;33m {listacc[g]} |\033[1;32m {h}:{m}:{s} |\033[1;31m [+{tien}đ] =>\033[1;32m Tổng : {tong} VNĐ")
      for i in range(delay,-1,-1):
        print("                                                 ",end = "\r")
        for j in ["",".","..","..."]:
          print(f"\033[1;32mĐang delay giữa các job [{i}]{j}",end = "\r")
          time.sleep(1/4)
    else:
      while True:
        try:
          boqua(idjob,instagram_account_id,object_id,"follow")
          print("                                  ",end = "\r")  
          print("\033[1;31mBỏ Qua Job!!!",end = "\r")        
          break
        except:
          pass
  else:
    g+=1 
    if(g >= len(listacc)):
      print("\033[1;36mHết job rùi quay lại sau nhé :))")
      quit()
    print(print(f"\033[1;35mAcc •{listacc[g-1]}• đã hết job hoặc gặp lỗi khi nhận job nên chuyển sang acc {listacc[g]}!!!"))  
    
