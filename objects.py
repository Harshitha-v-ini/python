class fan:
    def __init__(self,name,wings,color):
        self.name=name
        self.wings=wings
        self.color=color
        
    def details(self):
        print("Name:{},wings:{},color{}".format(self.name,self.wings,self.color))
        
while (1):
    v=input("enter the input to continue or else type exit")
    if(v==exit):
        break
    else:
        name=input("Enter the name")
        wings=input("Enter the wings")
        color=input("Enter the color")
        fan1=fan(name,wings,color)
        fan1.details() 
