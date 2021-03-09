class  student:
    def __init__(self,n,a,h):
        self.full_name = n
        self.age = a 
        self.hobby = h
    def get_age(self):
        return self.age
    def hobby(self):
        return self.hobby
    
f = student("Tiara Maulida Putri", 19,"traveling")
print(f.full_name)
print(f.get_age())
print(f.hobby)