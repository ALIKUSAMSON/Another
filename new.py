def greet_user(names):
    for name in names:
        print("whatsap Team " + name)

username =['norbert','daniel','fred']
greet_user(username)

#def make_invserse(invserse_dict):
   # for f in list(invserse_dict):
  #      invserse_dict[invserse_dict[f]]=f
 #   return invserse_dict
#inverse = make_invserse({sin:asin,cos:acos,tan:atan,log:exp})

def f(x,y=None):
    if y is None: y=[]
    y.append(x)
    return y, id(y)
print(f(23))
print(f(42))

class Name:
    def create(self,name):
        self.name = name
    def display(self):
        return self.name
    def saying(self):
        return "hello " + self.name
first = Name()
first.create('samson')
first.display()