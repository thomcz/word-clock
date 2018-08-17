import subprocess as sp
from time import sleep

extProc = sp.Popen(['python','main.py'])
sleep(4)

sp.Popen.terminate(extProc)
  
 
     
       
