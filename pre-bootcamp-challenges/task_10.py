#defining a function that takes a parameter
#and returns the vowels in it
def vowels (Words):

#assigning capital and small letter vowels to their variable
  vowels = "AEIOUaeiou"

#print
#character for characrer in parameter if character is found in
#variable vowels

  print ([char for char in Words if char in vowels])

#calling out function
vowels ('JCOle VS. KendrIck LamAr')
