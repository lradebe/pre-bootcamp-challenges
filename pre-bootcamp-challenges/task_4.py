a, b = input ("Try your luck: "), input ("Try again: ")
c = a + b

sub_str = "3"

if a.find (sub_str) == -1 or b.find (sub_str) == -1 and c.find (sub_str) == -1:
    print ("FALSE")
else:
    print ("TRUE!")
