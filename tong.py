import requests,os
from time import strftime,sleep
banner = """
          \033[1;36m████████╗░█████╗░████████╗
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
\033[1;32m═════════════════════════════════════════════════════════════
\033[1;36mCOPYRIGHT : Thành Chần
\033[1;36mZalo : 0335021778
\033[1;36mNhóm Xàm xí,Báo lỗi : https://zalo.me/g/drghio579
\033[1;32m═════════════════════════════════════════════════════════════"""
def key():
  try:
    ma = open("keytool.txt","x")
  except:
    pass
  ngay=int(strftime('%d'))
  key1=str(ngay*124656646+2388472%3)
  key = 'tct'+key1
  url = 'https://layskeytool.000webhostapp.com/key.html?key='+key
  ma = open("keytool.txt","r")  
  testkey = ma.read()
  if testkey != key:
    for i in range(3,-1,-1):
      print("                                               ",end = "\r")
      for j in ["",".","..","..."]:
        print(f"\033[1;36mBạn sẽ đc chuyển đến web lấy mã sau {i} giây{j}",end = "\r")
        sleep(1/4)
    print("                                                    ",end = "\r")
    os.system(f"termux-open-url {url}")
    testkey = input("\033[1;35mNhập Key : ") 
    for i in range(1,101):
      print("                              ",end = "\r")
      if(i < 10):
        print(f"\033[1;33mĐang check key {i}%",end = "\r")
        sleep(0.1)
      else:
        print(f"\033[1;33mĐang check key {i}%",end = "\r")
        sleep(0.01)
    sleep(1)    
    if testkey != key:
      print(f"\033[1;31mKey sai hãy vượt link and nhập lại đe")
      quit()
    else:
      ma = open("keytool.txt","w")
      ma.write(testkey)
      ma.close()
      print("\033[1;36mKey đúng gòi bạn sài tool vui vẻ nhé:)))")
      sleep(1)
os.system("clear")      
print(banner)      
#key()       
os.system("clear")
print(banner)
listnv = """\033[1;32m═════════════════════════════════════════════════════════════
\033[1;36m`[1]~Follow Tiktok \033[1;32m✓
\033[1;36m`[2]~Follow Instagram \033[1;31m( Vẫn đang hoàn thiện nên có khả lăng gặp lỗi:)) )
\033[0m...
\033[1;32m═════════════════════════════════════════════════════════════"""
print(listnv)
while True:
  try:
    select = int(input("\033[1;35mChọn nhiệm vụ bạn mún làm : "))
    if select not in [1,2]:
      print("\033[1;33mNhiệm vụ này không có trong danh sách!!!")
      continue
    break
  except:
    print("\033[1;31mSai định dạng!!!")
if select == 1:
  try:
    link = requests.get("https://raw.githubusercontent.com/thanhbtm1/golike/main/Goliketiktok.py").text
  except:
    print("\033[1;36mTool Đang Bảo Trì Quay Lại Sau!!!")
    quit()
  exec(link)
elif select == 2:
  try:
    link = requests.get("https://raw.githubusercontent.com/thanhbtm1/golike/main/Golikeins.py").text
  except:
    print("\033[1;36mTool Đang Bảo Trì Quay Lại Sau!!!")
    quit()
  exec(link)  
