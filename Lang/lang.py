#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint Calcutator-Lite Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint Calcutator-Lite All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calcutator-Lite
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calcutator-Lite"""

about = "LinuxUsersLinuxMint-Calculator-Lite 2.3"
lang=input("Language: ")

if lang == "tr" or lang == "TR":
    error_dialog="Geçersiz işlem!"
    process_list = "calc> Girebileceğiniz işlemler: "
    process = "toplama\nçıkarma\nçarpma\nbölme\nyüzde hesaplama\nmod alma\nçıkış\nhakkında\n1,2,3,4,5,6,7,8"
    usr_input_n1 = "calc> 1. sayiyi giriniz: "
    usr_input_n2 = "calc> 2. sayiyi giriniz: "
    process_input = "calc> Gerçekleştirmek İstediğiniz İşlemi Giriniz: "
    div_err = "Bölme işleminde sayı 0 olamaz!"
elif lang == "en" or lang == "EN":
    error_dialog="Invalid Process!"
    process_list = "calc> Transactions you can enter: "
    process = "Addition\nSubraction\nMultiplication\nDivision\nPercentage\nMod\nexit\nabout\n1,2,3,4,5,6,7,8"
    usr_input_n1 = "calc> Enter the 1st number: "
    usr_input_n2 = "calc> Enter the 2nd number: "
    process_input = "calc> Enter the Transaction You Want to Perform: "
    div_err = "Number cannot be 0 when dividing!"
else:
    print("Invalid Language!")