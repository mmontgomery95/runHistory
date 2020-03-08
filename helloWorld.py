import helper
import random

# print(f"Starting {__file__}")


x = random.randint(0, 10)

if x < 5:
    helper.add_file()
    helper.record_success()
    print("Hello World!")
else:
    helper.add_file()
    helper.record_fail()
    print("Goodbye")
