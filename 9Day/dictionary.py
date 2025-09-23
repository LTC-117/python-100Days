error = {
    -1: "No Error",
    0: "Reading error",
    1: "Writing error",
    2: "Memory error",
    "err": 1
}

def error_handler(err_value: int):
    if err_value not in [0, 1, 2]:
        err_value = -1

    print(error[err_value])

def wipe_dictionary():
    return {}

error_handler(1)
for thing in error:
    print(thing)
