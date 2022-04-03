from lexar import Lexar
from parser import Parser

def main():
    filename = 'hello.gpl'
    file = open(filename, 'r')
    lexar = Lexar(file)
    parser = Parser(lexar.tokens)

    lexar.tokenizer()
    print("TOKENS:")
    print(lexar.tokens, "\n")

    parser.build_AST()
    print("AST:")
    print(parser.AST)

if __name__ == "__main__":
    main()