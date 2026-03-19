import random
from datetime import datetime

# Data
categories = {
    "sports": {
        "subjects": ["Virat Kohli", "Rohit Sharma", "MS Dhoni"],
        "actions": ["smashes", "celebrates with", "argues with"],
        "places": ["during IPL match", "in stadium", "after winning trophy"]
    },
    "politics": {
        "subjects": ["Narendra Modi", "Nirmala Sitharaman"],
        "actions": ["announces", "cancels", "discusses"],
        "places": ["in parliament", "at Red Fort", "during press conference"]
    },
    "entertainment": {
        "subjects": ["Shah Rukh Khan", "Allu Arjun"],
        "actions": ["launches", "dances with", "celebrates with"],
        "places": ["at movie set", "in Mumbai", "during award show"]
    }
}

templates = [
    "BREAKING: {s} {a} {p}",
    "SHOCKING: {s} suddenly {a} {p}",
    "EXCLUSIVE: {s} caught while {a} {p}"
]

history = []

# Functions
def generate_headline():
    print("\nChoose Category: sports / politics / entertainment")
    category = input("Enter category: ").lower()

    if category not in categories:
        print("Invalid category!")
        return

    data = categories[category]

    headline = random.choice(templates).format(
        s=random.choice(data["subjects"]),
        a=random.choice(data["actions"]),
        p=random.choice(data["places"])
    )

    history.append(headline)
    print("\n📰 " + headline)


def show_history():
    if not history:
        print("\nNo headlines generated yet!")
    else:
        print("\nLast Headlines:")
        for h in history[-5:]:
            print("-", h)


def save_to_file():
    with open("headlines.txt", "a") as f:
        for h in history:
            f.write(f"{datetime.now()} - {h}\n")
    print("\nSaved to headlines.txt successfully!")


# Main Menu
while True:
    print("\n===== Fake News Generator =====")
    print("1. Generate Headline")
    print("2. View History")
    print("3. Save to File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_headline()
    elif choice == "2":
        show_history()
    elif choice == "3":
        save_to_file()
    elif choice == "4":
        print("\nThanks for using the generator 😄")
        break
    else:
        print("Invalid choice! Try again.")