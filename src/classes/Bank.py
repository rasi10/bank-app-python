class Bank:
    def __init__(self, name):        
        self.name = name

    def _load(self, input_file):
        f = open(input_file,'r')
        print(f.read())
