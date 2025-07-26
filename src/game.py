import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import colorama
from colorama import Fore, Style
from player import Player
# from combat import Combat
# from inventory import Inventory
# from utils import roll_dice, clear_screen

colorama.init()
console = Console()

def main():
    """Main game function for Dungeon Dice"""
    console.print(Panel.fit("🎲 Welcome to Dungeon Dice! 🎲", style="bold green"))
    
    player_name = input("Enter your character's name: ")
    player = Player(player_name)
    
    # dice_roll = roll_dice(6)
    # console.print(f"You rolled a: {dice_roll}", style="bold cyan")
    
    # Display player info
    console.print(f"Welcome, {player.name}!", style="bold yellow")
    
    print(f"{Fore.YELLOW}Game is working{Style.RESET_ALL}")

if __name__ == "__main__":
    main()