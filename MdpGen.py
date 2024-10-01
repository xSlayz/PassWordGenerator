import random
import time
from pystyle import Colorate, Colors, System, Center, Write, Anime

latter = "abcdefghijklmnopqrstuvwxyz"
maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "123456789"
symbols = "@%#$*?!§/\;."

banner = r'''

__________                        __      __                .___
\______   \_____    ______ ______/  \    /  \___________  __| _/
 |     ___/\__  \  /  ___//  ___/\   \/\/   /  _ \_  __ \/ __ | 
 |    |     / __ \_\___ \ \___ \  \        (  <_> )  | \/ /_/ | 
 |____|    (____  /____  >____  >  \__/\  / \____/|__|  \____ | 
                \/     \/     \/        \/                   \/ 
                                           © By xSlayz - v1.0
'''[1:]

System.Clear()
System.Size(150, 50)
System.Title("PassWord")

def main():
  System.Clear()
  print("\n"*2)
  print(Colorate.Diagonal(Colors.red_to_blue, Center.XCenter(banner)))
  print("\n"*5)

  scale = Write.Input("Choisi la taille de ton mot de passe (min: 8 | max: 50) -> ", Colors.white, interval=0.005)
  
  try:
    scale = int(scale)
  except:
    print()
    print(Colorate.Error(Colors.red + "[Error] La taille doit être un entier !"))
    return

  if scale < 8 or scale > 50:
    print(Colorate.Error(Colors.red + "[Error] Le mot de passe choisi ne correspond pas au critère !"))
    return  

  
  print()
  Write.Print("Merci de patienter...\n", Colors.white, interval=0.005)
  time.sleep(2)
  Write.Print("\nRéussi !\nLe mot de passe a été généré !", Colors.green_to_yellow, interval=0.005)
  passeword = "".join(random.sample(latter + maj + number + symbols, scale))
  print("\n"*2)
  Write.Print(" "*10 + passeword, Colors.white_to_green, interval=0.005)
  print("\n"*5)

  regen = Write.Input("Voulez vous générer un nouveau mot de passe ? [y/n] -> ", Colors.white, interval=0.005)

  if regen == "y":
    main()
    return
    
  return exit()
        


if __name__ == '__main__':
    while True:
        main()

