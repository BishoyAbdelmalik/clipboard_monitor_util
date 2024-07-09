import pyperclip
import os
import time
if __name__ == "__main__":

    path = os.getenv('CLIPBOARD_PATH')
    if path==None:
        path="file"
    if not os.path.exists(path):
        with open(path, 'w'): 
            pass
    
    value=""
    pyperclip.copy(value)
    try:
        while True:
            new_val=pyperclip.paste()
            if new_val != value:
                value=new_val
                with open(path,"w") as fp:
                    fp.write(value)
            time.sleep(1)
    except KeyboardInterrupt:
        os.close(0)
