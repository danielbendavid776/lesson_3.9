

try:
    data = int(input("Enter: "))

# 1
# except ValueError as e:
#     print(f"Input error: {e}")
#
# except TypeError as e:
#     print(f"Input error: {e}")

# 2 -- shortcut
except (ValueError , TypeError) as e:
    print(f"Input error: {e}")