
from rich.console import Console
console = Console()

def main():
    matn = "Salom|Qalesiz?|Yaxshi o'tdimi bugun?"
    xabarlar = matn.split("|")  

    for xabar in xabarlar:
     console.print(xabar,style ="italic cyan")

main()
