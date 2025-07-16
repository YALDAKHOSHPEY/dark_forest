import random
import time

player = {
    "name": "",
    "health": 100,
    "energy": 100,
    "inventory": []
}

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def intro():
    slow_print("🌲 You wake up in a dark forest. The air is cold. You have no memory of how you got here.")
    player["name"] = input("What's your name, survivor? ").strip().capitalize()
    slow_print(f"\n🧍 Welcome, {player['name']}... Your journey begins now.\n")
    time.sleep(1)

def show_status():
    print(f"\n❤️ Health: {player['health']} | ⚡ Energy: {player['energy']} | 🎒 Inventory: {player['inventory']}\n")

def encounter():
    event = random.choice(["snake", "berries", "bear", "river", "cabin", "nothing"])
    if event == "snake":
        slow_print("🐍 A venomous snake bites you!")
        player["health"] -= random.randint(10, 25)
    elif event == "berries":
        slow_print("🍓 You find wild berries. They look tasty.")
        choice = input("Do you eat them? (yes/no): ").lower()
        if choice == "yes":
            if random.random() > 0.3:
                slow_print("😋 They are delicious! You gain energy.")
                player["energy"] += 15
            else:
                slow_print("🤢 Uh oh... they were poisonous.")
                player["health"] -= 20
        else:
            slow_print("You decide to leave them.")
    elif event == "bear":
        slow_print("🐻 A bear appears! You must choose quickly:")
        action = input("Do you (run) or (fight)? ").lower()
        if action == "run":
            slow_print("🏃‍♂️ You barely escape, but you lose energy.")
            player["energy"] -= 20
        elif action == "fight":
            slow_print("💥 You try to fight the bear...")
            if "knife" in player["inventory"]:
                slow_print("🗡️ You stab the bear and survive, but you're hurt.")
                player["health"] -= 20
            else:
                slow_print("😱 You have no weapon. The bear injures you badly.")
                player["health"] -= 50
    elif event == "river":
        slow_print("🌊 You find a river. Do you drink water?")
        if input("Drink? (yes/no): ").lower() == "yes":
            slow_print("💧 You feel refreshed.")
            player["energy"] += 10
        else:
            slow_print("You stay thirsty.")
    elif event == "cabin":
        slow_print("🏚️ You discover a hidden cabin.")
        if "key" in player["inventory"]:
            slow_print("🔑 You unlock the door and find food and a knife!")
            player["inventory"].append("knife")
            player["energy"] += 30
        else:
            slow_print("It's locked... but you find a key nearby.")
            player["inventory"].append("key")
    else:
        slow_print("🌫️ Nothing happens. The forest is silent...")

    player["energy"] -= random.randint(5, 15)

def check_status():
    if player["health"] <= 0:
        slow_print("💀 You died from injuries.")
        return False
    if player["energy"] <= 0:
        slow_print("🥵 You collapsed from exhaustion.")
        return False
    return True

def game_loop():
    intro()
    round_num = 1
    while True:
        slow_print(f"\n🔄 Round {round_num}:")
        show_status()
        encounter()
        if not check_status():
            break
        cont = input("👉 Continue exploring? (yes/no): ").lower()
        if cont != "yes":
            slow_print("🌅 You found a way out of the forest. You survive.")
            break
        round_num += 1

    slow_print(f"\n🧾 Final Status: Health: {player['health']} | Energy: {player['energy']} | Inventory: {player['inventory']}")
    slow_print(f"🪦 Game Over, {player['name']}. Thanks for playing!")

if __name__ == "__main__":
    game_loop()
