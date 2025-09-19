
from rich.console import Console

console = Console

def main():
    text = "Ism:Ali, Familiya:Valiyev, Yil:2002"

    l = text.split(",")

    for i in l:
     i = i.strip()  
    
    print(i.replace(":", ": ",style = "strike green"))

main()