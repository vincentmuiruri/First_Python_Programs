# Apple class with a constructor method defined

class Apple:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor

# defining how an instance of the object will be printed when passed to the print()
        
        def __str__(self):
            return "This apple is {} and its flavor is {}".format(self.color,self.flavor)

# Defining and creating a new instance of Apple class and set color and falvor values all in go

jonagold = Apple("red","sweet")
print(jonagold.color)  
    
    
    
    
    
    
#     def __str__(self):
#         return "An apple which is {}  and {}".format(self.color, self.flavor)
    
# honeycrisp = Apple("red","sweet")
# print(honeycrisp)

# # prints "an apple which is red and sweet"