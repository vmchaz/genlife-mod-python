from instructions import *
from assembler import Assembler

def main():
    a = Assembler()
    r = a.AssembleInstruction("mov_ri r15, 200 a:1, 2, F d:0")
    print(r)
    

if __name__ == "__main__":
    main()
