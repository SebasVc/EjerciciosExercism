class Garden:
    def __init__(self, diagram,students=['Alice', 'Bob', 'Charlie', 'David','Eve', 'Fred', 'Ginny', 'Harriet','Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.dig=diagram.split("\n")
        students.sort()
        self.st={students[i] : i+1 for i in range(len(students))}
        self.pl={'G':'Grass','C': 'Clover','R': 'Radishes','V': 'Violets'}
    def plants(self,name):
        ui=[]
        for l in range(2):
            for k in range(2):
                ui.append(self.pl[self.dig[l][(self.st[name]-1)*2+k]])
        return ui