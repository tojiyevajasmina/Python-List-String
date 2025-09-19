
from rich.console import Console
console = Console()

def main():
    gap = "olol radar makka non"
    sozlar = gap.split()  
    palindromlar = []

    for soz in sozlar:
     if soz == soz[::-1]: 
        palindromlar.append(soz)

    console.print(palindromlar,style = "bold red")

main()
