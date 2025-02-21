#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint Calcutator-Lite Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint Calcutator-Lite All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calcutator-Lite
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calcutator-Lite"""

from Lang.lang import *
from Lib.Basic_Maths import *
from Lib.pyappdevkit import *

while True:
    print(process_list)
    print(process)
    n1=int(input(usr_input_n1))
    n2=int(input(usr_input_n2))
    process_inp=input(process_input)

    if process_inp == "1":
        Addition(n1,n2,"")
    elif process_inp == "2":
        Extraction(n1,n2,"")
    elif process_inp == "3":
        Multiplication(n1,n2,"")
    elif process_inp == "4":
        Division(n1,n2,"",div_err)
    elif process_inp == "5":
        Percentage(n1,n2,"")
    elif process_inp == "6":
        Mod(n1,n2,"")
    elif process_inp == "7":
        exit_program_time(10)
    elif process_inp == "8":
        print(about)
    else:
        error_msg(error_dialog,"","")