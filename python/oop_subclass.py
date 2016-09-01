class SchookMember:
    '''Represents any school member.'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print '(Initialized SchoolMember: {})'.format(self.name)
    def tell(self):
        'Tell my detail.'
        print 'Name: "{}" Age: "{}"'.format(self.name,self.age)
class Teacher(SchookMember):
    'Represents a teacher.'
    def __init__(self,name,age,salary):
        SchookMember.__init__(self,name,age)
        self.salary=salary
        print '(Initialized Teacher: {})'.format(self.name)
    def tell(self):
        SchookMember.tell(self)
        print 'Salary: "{:d}"'.format(self.salary)
class Student (SchookMember):
    'Represents a student.'
    def __init__(self,name,age,marks):
        SchookMember.__init__(self,name,age)
        self.marks=marks
        print '(Initialized Student: {})'.format(self.name)
    def tell(self):
            SchookMember.tell(self)
            print 'Marks: "{:d}"'.format(self.marks)
t=Teacher('Mrs. Nguyen',4,30000)
s=Student('Sam',25,75)
print
members=[t,s]
for member in members:
    member.tell()
print 'Done'

