class Dictionary:
    def __init__(self):
        self.random = []
 
        rfile = open('random.txt', 'r', encoding = 'utf_8')

        r_lines = rfile.readlines()
        rfile.close()

        self.random = []
        for line in r_lines:
            str = line.rstrip('\n')
            if (str!=''):
                self.random.append(str)


        pfile = open('pattern.txt', 'r', encoding = 'utf_8')

        p_lines = pfile.readlines()
        pfile.close()

        self.new_lines = []
        for line in p_lines:
            str = line.rstrip('\n')
            if (str!=''):
                self.new_lines.append(str)
        
        self.pattern = {}

        for line in self.new_lines:
            ptn, prs = line.split('\t')
            self.pattern.setdefault('pattern', []).append(ptn)
            self.pattern.setdefault('phrases', []).append(prs)
            
