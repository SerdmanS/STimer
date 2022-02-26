# STimer for Linux ver: 1.0
# made by Serdar a.k.a. LAZARE
# Aslında C# form uygulaması yapacaktım ama VS19 kullanırken yaptığım şeyi VS22 ile yapamayınca sinirlenip daha az satırla python kullanarak yapmak istedim

import time, os, sys
cmd = ""
flag = False
def help():
    print("\n[*] Program isminden sonra çalışmasını istediğiniz komutu girin\n\n\tÖrnek: python STimer.py tasklist\n\t-s veya --shutdown : Sistemi kapatır\n\t-r veya --restart : Sistemi yeniden başlatır\n")
    sys.exit(1)
    return
def clock():
    comd = cmd
    H = int(input("Saat girin : "))
    M = int(input("Dakika girin : "))
    S = int(input("Saniye girin : "))
    os.system("clear")

    while True:
        print(f"{H}:{M}:{S}")
        time.sleep(1)
        os.system("clear")

        if H == 0 and M == 0 and S == 0:
            print("\n[*] Süre doldu!\n")
            time.sleep(1)
            if flag == True:
                print(f"[*] Komut işlendi : {comd}")
                os.system(comd)
            if len(sys.argv)>1:
                for i in range(1,len(sys.argv)):
                    comd = comd+sys.argv[i]+" "
                print(f"[*] Komut işlendi : {comd}")
                os.system(comd)
            break

        if S==0 and M>0:
            M-=1
            S=59

        if S==0 and M==0 and H>0:
            H-=1
            M=59
            S=59
        S-=1
try:
    if len(sys.argv)<2: help()
    if len(sys.argv)>1:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help': help()
        if sys.argv[1] == '-s' or sys.argv[1] == '--shutdown':
            flag = True
            cmd = "shutdown -t 0 now"
            clock()
        if sys.argv[1] == '-r' or sys.argv[1] == '--restart':
            flag = True
            cmd = "shutdown -r 0 now"
            clock()
        else :
            clock()
except KeyboardInterrupt:
    print("\n[*] Program kullanıcı tarafından sonlandırıldı!\n")
