# Byron Garcia
# 3/10/24
# Write

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

    def task_readyness(self, task_name, items_needed, debuff_block):
        print(f"Checking task: {task_name}")

        if all(item in self.weapons for item in items_needed):
            print("Required items collected")
        else:
            print("You are missing necessary items")

        if debuff_block in self.weaknesses:
            print("You have debuffs, can't continue")
        else:
            print("No debuffs found")


player1 = character('', '', '')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("debuff: ", debuff)

Tasks = {
    "Climb a mountain": (["rope", "coat", "first aid kit"], "slow"),
    "Cook a meal": (["pan", "groceries"], "small"),
    "Write a book": (["pen", "paper", "idea"], "confusion")
}

for task_name, (items_needed, debuff_block) in Tasks.items():
    player1.task_readyness(task_name, items_needed, debuff_block)
