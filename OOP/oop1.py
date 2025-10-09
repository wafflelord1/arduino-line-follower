class cat:
    def __init__(selfless,name,age):
        selfless.name = name
        selfless.age = age   
    def get_name(selfless): 
        return selfless.name
    def get_age(selfless):
        return selfless.age
    def set_age(selfless,age):
        selfless.age = age
c = cat("waffy", 19)
c.set_age(20)
print(c.get_age())
