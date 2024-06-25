# Handling error using Exception block

"""
try:
    data = {"A": 1, "B": 2}
    print(data["A"])
    print(10/10)
except KeyError:
    print("There is no such key in dict, pls check the 'Key'")
except ZeroDivisionError:
    print("We shouldn't do division with zero")
except:
    print("")
finally:
    print("Successfully Processed")
"""