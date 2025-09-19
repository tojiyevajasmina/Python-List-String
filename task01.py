
from rich.console import Console

console = Console()

def main():
    fish = "Aliyev Vali G'aniyevich"
    ism_sharif = ' '.join(fish.split()[1:])
    familiya = fish.split()[0]

    console.print(f"{ism_sharif}, {familiya}", style = "bold green")

main()