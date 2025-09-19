
from rich.console import Console
console = Console()

def main():
    son = input("Butun son kiriting: ")

    if son.startswith('-'):
        raqamlar = '-'.join(son[1:])  
        natija = '-' + raqamlar       
    else:
      natija = '-'.join(son)

    console.print("Natija:", natija,style = "underline magenta")

main()