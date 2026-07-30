def ask(question):
    while True:
        answer = input(question).lower()

        if answer in ("y", "n"):
            return answer

        print("Please enter y or n.")
