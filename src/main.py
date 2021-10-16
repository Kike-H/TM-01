from modules.turing_machine.TuringMachine import TuringMachine

input_str = input("Give a string: ")

tm = TuringMachine(input_str)

if(tm.isAccepted()):
    print(tm.green+"\n Accepted")
else:
    print(tm.red+"\n Rejected")

