#Task 1
def oops():
    raise IndexError("Raise an IndexError!")
def catch_oops():
    try:
        oops()
    except IndexError as e:  # ловимо IndexError
        print("Hey: ", e)

catch_oops()







