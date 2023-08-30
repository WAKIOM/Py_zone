class string_:
    """
    A string-like class with methods
    """

    def __init__(self, in_put):
        self.in_put = in_put
        self.out_put = ""

    def upper_(self):
        for char in self.in_put:
            ascii_value = ord(char)
            if 97 <= ascii_value <= 122: 
                self.out_put += chr(ascii_value - 32)  # Convert lowercase to uppercase
            else:
                self.out_put += char  #leave them as they are

    def lower_(self):
        for char in self.in_put:
            ascii_value = ord(char)
            if 65 <= ascii_value <= 90:
                self.out_put += chr(ascii_value + 32)  # Convert uppercase to lowercase
            else:
                self.out_put += char  #leave them as they are

take = input("Type anything in either lowercase or uppercase: ")
give = string_(take)

is_upper = True
is_lower = True

for char in give.in_put:
    ascii_value = ord(char)
    if not (65 <= ascii_value <= 90):
        is_upper = False
    if not (97 <= ascii_value <= 122):
        is_lower = False

if is_upper:
    give.lower_()
    print(give.out_put)
elif is_lower:
    give.upper_()
    print(give.out_put)
else:
    print("The input should be in all uppercase or all lowercase.")