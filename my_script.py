import os
import time
import sys
from colorama import Fore, Style

# تحديد الألوان
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE

# التحقق من وجود مكتبة colorama وتثبيتها إذا لزم الأمر
try:
    import colorama
except ModuleNotFoundError:
    print("colorama is not installed.")
    os.system("pip install colorama")

logo = f"""
{C}
XPHANTOM PH4N70M
"""

def main():
    os.system('clear')
    print(logo)
    print()
    
    # تعيين القيم الثابتة
    cncode = 967  # رمز البلد
    num = 775180627  # الرقم
    crash = 25  # عدد مرات التحطيم
    
    combnum = f"{775180627}{967}"
    print()
    
    Finalcall = input(f'{Y}[؟]{W} هل تريد تغيير الرقم؟ {W}{combnum} {R}(Y/N)\n\n{C}=> ')
    if Finalcall == 'Y' or Finalcall == 'y':
        main()
    elif Finalcall == 'N' or Finalcall == 'n':
        os.system('clear')
        print(f"{G}[{Y}+{G}]{Y} جاري تحطيم واتساب على الرقم: +{967775180627} ...")
        time.sleep(5)
        link = fhttps://wa.me/967775180627?text=%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%20%D9%87%D8%B0%D8%A7%20%D8%A7%D8%AE%D8%AA%D8%A8%D8%A7%D8%B1%20%D8%AA%D8%AC%D8%B1%D8%A8%D9%8A

if __name__ == "__main__":
    main()
