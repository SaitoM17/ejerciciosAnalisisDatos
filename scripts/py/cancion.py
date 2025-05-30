import time
import sys
import random

# Texto que quieres mostrar (puedes pegar la letra de una canción aquí)
lyrics = [
    "Carry on, my wayward son",
    "There'll be peace when you are done",
    "Lay your weary head to rest",
    "Don't you cry no more"
]

# Colores ANSI seguros para la mayoría de terminales
colors = [
    "\033[1;91m",  # rojo brillante
    "\033[1;92m",  # verde brillante
    "\033[1;93m",  # amarillo brillante
    "\033[1;94m",  # azul brillante
    "\033[1;95m",  # magenta brillante
    "\033[1;96m",  # cian brillante
]
reset = "\033[0m"

# Efectos extra
# symbols = ["*", "+", "~", "@", "#", "%", "&"]
symbols = ["★", "✦", "✧", "♬", "♩", "♪", "♭", "☄", "☀", "⚡"]

def animated_print(text, color, symbol):
    print(color, end='')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print(f' {symbol}{reset}')
    time.sleep(0.5)

def main():
    for i, line in enumerate(lyrics):
        color = colors[i % len(colors)]
        symbol = random.choice(symbols)
        animated_print(line, color, symbol)
    print(f"\n{colors[0]}*** FIN ***{reset}\n")

if __name__ == "__main__":
    main()
