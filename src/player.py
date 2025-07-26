import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.max_health = 100
        self.mana = 50
        self.max_mana = 50
        self.experience = 0
        self.experience_to_next_level = 100
        
        # Combat stats
        self.strength = 10
        self.defense = 8
        self.agility = 7
        self.luck = 5
        
        # Game progress
        self.gold = 25
        self.dungeon_level = 1
        self.rooms_explored = 0
        self.enemies_defeated = 0
        
        # Equipment
        self.weapon = None
        self.armor = None
        self.accessory = None
        
        self.inventory = None
    
    def display_stats(self):
        """Display player stats in a table"""
        table = Table(title=f"[bold yellow]{self.name}'s Character Sheet[/bold yellow]")
        table.add_column("Attribute", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")
        
        table.add_row("Level", str(self.level))
        table.add_row("Health", f"{self.health}/{self.max_health}")
        table.add_row("Mana", f"{self.mana}/{self.max_mana}")
        table.add_row("Experience", f"{self.experience}/{self.experience_to_next_level}")
        table.add_row("Gold", f"{self.gold} 🪙")
        table.add_row("", "")  # Spacer
        table.add_row("Strength", str(self.strength))
        table.add_row("Defense", str(self.defense))
        table.add_row("Agility", str(self.agility))
        table.add_row("Luck", str(self.luck))
        table.add_row("", "")  # Spacer
        table.add_row("Dungeon Level", str(self.dungeon_level))
        table.add_row("Rooms Explored", str(self.rooms_explored))
        table.add_row("Enemies Defeated", str(self.enemies_defeated))
        
        console.print(table)
    
    def take_damage(self, damage):
        """Player takes damage"""
        actual_damage = max(1, damage - (self.defense // 2))
        self.health -= actual_damage
        self.health = max(0, self.health)
        
        if actual_damage > 0:
            console.print(f"[red]{self.name} takes {actual_damage} damage![/red]")
        else:
            console.print(f"[green]{self.name} blocks the attack![/green]")
        
        return actual_damage
    
    def heal(self, amount):
        """Heal the player"""
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        healed = self.health - old_health
        
        if healed > 0:
            console.print(f"[green]{self.name} heals for {healed} health![/green]")
        else:
            console.print(f"[yellow]{self.name} is already at full health![/yellow]")
        
        return healed
    
    def gain_experience(self, exp):
        """Gain experience and check for level up"""
        self.experience += exp
        console.print(f"[cyan]{self.name} gains {exp} experience![/cyan]")
        
        if self.experience >= self.experience_to_next_level:
            self.level_up()
    
    def level_up(self):
        """Level up the player"""
        self.level += 1
        self.experience -= self.experience_to_next_level
        self.experience_to_next_level = int(self.experience_to_next_level * 1.5)
        
        # Increase stats
        health_increase = random.randint(8, 15)
        mana_increase = random.randint(3, 8)
        
        self.max_health += health_increase
        self.health = self.max_health  # Full heal on level up
        self.max_mana += mana_increase
        self.mana = self.max_mana
        
        # Random stat increases
        stat_points = 3
        for _ in range(stat_points):
            stat_choice = random.choice(['strength', 'defense', 'agility', 'luck'])
            setattr(self, stat_choice, getattr(self, stat_choice) + 1)
        
        console.print(Panel.fit(
            f"[bold yellow]🎉 LEVEL UP! 🎉[/bold yellow]\n"
            f"[green]{self.name} is now level {self.level}![/green]\n"
            f"[cyan]Health: +{health_increase} | Mana: +{mana_increase}[/cyan]\n"
            f"[magenta]Stats increased randomly![/magenta]",
            style="bold green"
        ))
    
    def gain_gold(self, amount):
        """Gain gold"""
        self.gold += amount
        console.print(f"[yellow]{self.name} gains {amount} gold! 🪙[/yellow]")
    
    def spend_gold(self, amount):
        """Spend gold if player has enough"""
        if self.gold >= amount:
            self.gold -= amount
            return True
        else:
            console.print(f"[red]Not enough gold! Need {amount}, have {self.gold}[/red]")
            return False
    
    def is_alive(self):
        """Check if player is alive"""
        return self.health > 0
    
    def get_attack_power(self):
        """Calculate attack power based on stats and weapon"""
        base_attack = self.strength + random.randint(1, 6)
        weapon_bonus = 0
        
        if self.weapon:
            weapon_bonus = self.weapon.get('damage', 0)
        
        return base_attack + weapon_bonus
    
    def get_defense_value(self):
        """Calculate defense value based on stats and armor"""
        base_defense = self.defense
        armor_bonus = 0
        
        if self.armor:
            armor_bonus = self.armor.get('defense', 0)
        
        return base_defense + armor_bonus
    
    def rest(self):
        """Rest to recover health and mana"""
        health_recovery = random.randint(10, 20)
        mana_recovery = random.randint(15, 25)
        
        self.heal(health_recovery)
        old_mana = self.mana
        self.mana = min(self.max_mana, self.mana + mana_recovery)
        mana_gained = self.mana - old_mana
        
        if mana_gained > 0:
            console.print(f"[blue]{self.name} recovers {mana_gained} mana![/blue]")
        
        console.print(f"[green]{self.name} feels refreshed after resting![/green]")
    
    def __str__(self):
        """String representation of player"""
        return f"{self.name} (Level {self.level}) - HP: {self.health}/{self.max_health}"