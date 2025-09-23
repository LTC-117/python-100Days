def func_prin(user_name: str):
    print("Hello, ", user_name)

def rep_more(num: int):
    if num == 0:
        num = 1

    count: int = 0

    while count < num:
        print(f"Hello {count}")
        count += 1

user_in = input("Insert your name: ")
func_prin(user_in)
rep_more(0)
