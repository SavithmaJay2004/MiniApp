import datetime

def greet(name):
    now = datetime.datetime.now()
    return f"Hello, {name}! Current time is {now:%Y-%m-%d %H:%M:%S}"

def greet(name):
    return f"Hello, {name}! Welcome to GitHub."

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))
    print("nice to meet you!")

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))
