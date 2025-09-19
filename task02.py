
from rich.console import Console

console = Console()

def main():
    input_str = "Dasturlash, Sun'iy intellekt, Web dizayn"
    fields = [s.strip().lower().replace(' ', '_') for s in input_str.split(',')]
    output = '_'.join(fields)

    console.print(output ,style ="italic red")

main()
