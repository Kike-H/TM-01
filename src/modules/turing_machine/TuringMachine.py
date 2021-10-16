class TuringMachine(object):

    def __init__(self, input_string:str):
        self.input_string = list(input_string)
        self.initial_state = 'q0'
        self.final_state = 'q4'
        self.actual_state = 'q0'
        self.position = 0
        self.flag = True
        self.red = '\u001b[31m'
        self.green = '\u001b[32m'
        self.blue = '\u001b[34m'
        self.yellow = '\u001b[33m'
        self.white = '\u001b[37m'
        self.purple = '\u001b[35m'

    def q0(self, symbol:str):
        if (symbol == '0'):
            self.input_string[self.position] = 'X'
            self.actual_state = 'q1'
            self.position = self.position+1

        elif (symbol == '1'):
            self.input_string[self.position] = 'X'
            self.actual_state = 'q3'
            self.position = self.position+1

        elif (symbol == 'X'):
            self.flag = False
        
        elif (symbol == 'Y'):
            self.input_string[self.position] = 'Y'
            self.actual_state = 'q0'
            self.position = self.position+1

        elif (symbol == ''):
            self.actual_state = 'q4'

        else:
            self.flag = False

    def q1(self, symbol:str):
        if (symbol == '0'):
            self.input_string[self.position] = '0'
            self.actual_state = 'q1'
            self.position = self.position+1

        elif (symbol == '1'):
            self.input_string[self.position] = 'Y'
            self.actual_state = 'q2'
            self.position = self.position-1

        elif (symbol == 'X'):
            self.flag = False
        
        elif (symbol == 'Y'):
            self.input_string[self.position] = 'Y'
            self.actual_state = 'q1'
            self.position = self.position+1

        elif (symbol == ''):
            self.flag = False
        
        else:
            self.flag = False

    def q2(self, symbol:str):
        if (symbol == '0'):
            self.input_string[self.position] = '0'
            self.actual_state = 'q2'
            self.position = self.position-1

        elif (symbol == '1'):
            self.input_string[self.position] = '1'
            self.actual_state = 'q2'
            self.position = self.position-1

        elif (symbol == 'X'):
            self.input_string[self.position] = 'X'
            self.actual_state = 'q0'
            self.position = self.position+1
        
        elif (symbol == 'Y'):
            self.input_string[self.position] = 'Y'
            self.actual_state = 'q2'
            self.position = self.position-1

        elif (symbol == ''):
            self.flag = False

        else:
            self.flag = False

    def q3(self, symbol:str):
        if (symbol == '0'):
            self.input_string[self.position] = 'Y'
            self.actual_state = 'q2'
            self.position = self.position-1

        elif (symbol == '1'):
            self.input_string[self.position] = '1'
            self.actual_state = 'q3'
            self.position = self.position+1

        elif (symbol == 'X'):
            self.flag = False
        
        elif (symbol == 'Y'):
            self.input_string[self.position] = 'Y'
            self.actual_state = 'q3'
            self.position = self.position+1

        elif (symbol == ''):
            self.flag = False

        else:
            self.flag = False

    def isAccepted(self):
        print('\n')
        while(self.actual_state != 'q4' and self.flag):
            self.print_step()
            symbol = ''
            try:
                symbol = self.input_string[self.position]
            except Exception as e:
                symbol = ''

            if (self.actual_state == 'q0'):
                self.q0(symbol)
            elif (self.actual_state == 'q1'):
                self.q1(symbol)
            elif (self.actual_state == 'q2'):
                self.q2(symbol)
            elif (self.actual_state == 'q3'):
                self.q3(symbol)

        return self.flag

    def print_step(self):
        print("| ", end="")
        i = 0
        for c in self.input_string:
            if(i == self.position):
                print(self.purple+c+self.white+" |", end=" ")
            else:
                if(c == 'X'):
                    print(self.red+c+self.white+" |", end=" ")
                elif(c == 'Y'):
                    print(self.blue+c+self.white+" |", end=" ")
                elif(c == '0'):
                    print(self.green+c+self.white+" |", end=" ")
                elif(c == '1'):
                    print(self.yellow+c+self.white+" |", end=" ")
            i = i+1
        print(" "+self.actual_state)    
