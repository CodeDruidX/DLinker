import pip
pip.main(["install","easygui"])
import easygui
import os
from pathlib import Path
os.system("color E")
os.system("cls")
print("""
██████╗░██╗░░░░░██╗███╗░░██╗██╗░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██║████╗░██║██║░██╔╝██╔════╝██╔══██╗
██║░░██║██║░░░░░██║██╔██╗██║█████═╝░█████╗░░██████╔╝
██║░░██║██║░░░░░██║██║╚████║██╔═██╗░██╔══╝░░██╔══██╗
██████╔╝███████╗██║██║░╚███║██║░╚██╗███████╗██║░░██║
╚═════╝░╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
""")
print("Готов к работе.")
print("Droids Linker работает так, что сохранения игры хранятся на Google-drive, а в AppData сохранения заменяются на синхронизирующиеся ссылки.")
while 1:
    print()
    print("Выберите сценарий:")
    print("1. Выгрузить сохранение из компьютера на диск")
    print("2. Создать ссылку-синхронизатор")
    tsk=input(">")
    if not tsk in ["1","2"]:continue
    elif tsk=="2":
        try:
            dest=Path(easygui.diropenbox(msg="Выберите папку c папкой с данными игры (например AppData/Roaming)"))
            src=Path(easygui.diropenbox(msg="Выберите облачные данные игры (например G:.../Saves/Factorio)"))

            assert not bool(os.system(f"mklink /D \"{os.path.join(dest,Path(os.path.basename(src)))}\" \"{src}\""))
            os.system("color A")
            break
        except:
            os.system("color 4")
            input("Smth went wrong ... Press Enter to exit")
            break
    elif tsk=="1":
        try:
            dest=Path(easygui.diropenbox(msg="Выберите папку игры в AppData (например Roaming/Factorio)"))
            src=Path(easygui.diropenbox(msg="Выберите место облачного сохранения игры (например G:.../Saves)"))

            assert not bool(os.system(f"xcopy /h /i /c /k /e /r /y \"{dest}\" \"{os.path.join(src,Path(os.path.basename(dest)))}\""))
            assert not bool(os.system(f"RMDIR \"{dest}\" /S /Q"))
            os.system("color A")
            break
        except:
            os.system("color 4")
            input("Smth went wrong ... Press Enter to exit")
            break