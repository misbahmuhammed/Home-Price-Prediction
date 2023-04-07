class Father:
    fathername = ''
    def father(self,fname):

        print(self.fathername)
class Mother:
    mothername = ""
    def mother(self,mname):

        print(self.mothername)
class Son(Father,Mother):
    def parents(self):
        print("father is {}".format(self.fathername))
        print("mother is {}".format(self.mothername))

obj = Son()
obj.fathername="hameed"
obj.mothername = "sainaba"
obj.parents()