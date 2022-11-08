from escpos.printer import Serial
import time

PRINTER = object()
HACK = """ O
  S
   L
    O
     H
      A
       C
        K"""

HACKERIET_LOGO = """                                          
            .&@@@@@@@@@@@@@@@%            
         @@@@@@@@@@@@@@@@@@@@@@@@&        
      &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/     
    #@@@@#*@@@@@@@@@@@@@@@@@@@@@@@@@@@.   
   @@@@@    @@@   .@@@@@@@@@@@@@@@@@@@@%  
  @               @@@@@@@@@@@@@@@@@@@@@@% 
 /,       *%#      *,,@@@@@@@@@@@@@@@@@@@ 
 @      &@@@@@@        @@@@@      @@@@@@@/
 @        *@@       @@@@@@@@@@@@@@@@@@@@@/
 **                    .@@@@@@@@@@@@@@@@@ 
  @                     #@@@@@@@@@@@,%@@/ 
   @                    #@@,   @@@%   (/  
    *&                               @    
      /@                           @      
         #&                    ,@*        
             *@@/.       ,%@&.            """

def setup():
    PRINTER = Serial(
        devfile='/dev/ttyUSB0',
        baudrate=115200,
        bytesize=8,
        parity='N',
        stopbits=1,
        timeout=1.00,
        dsrdtr=True
    )

def reset(p):
    p.set(text_type="NORMAL", invert=False, width=1, height=1, align="left")

def hacker_logo(p):
    reset(p)
    p.text(HACKERIET_LOGO)


def print_hack(p):
    p.set(text_type="B", invert=False, width=4, height=4, align="left")
    for line in HACK.split("\n"):
        p.text(f"{line}\n")
        time.sleep(0.5)
    p.text("\n")
    time.sleep(1)

    p.set(text_type="B", invert=True, width=4, height=4, align="left")
    p.text("location:\n")
    time.sleep(1.5)
    p.set(text_type="B", invert=False, width=4, height=4, align="left")
    p.text(" Hackeriet\n")
    time.sleep(1)
    p.text(" Oslo\n")
    p.text("\n")


    p.set(text_type="B", invert=True, width=4, height=4, align="left")
    p.text("time:\n")
    time.sleep(1.5)
    p.set(text_type="B", invert=False, width=4, height=4, align="left")
    p.text(" 27th dec\n")
    time.sleep(1)
    p.text(" 28th dec\n")
    time.sleep(1)
    p.text(" 29th dec\n")
    time.sleep(1)
    p.text("\n")

    hacker_logo(p)


    p.cut()
