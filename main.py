from interpreter import Interpreter
from interpreter import Parser
import interpreter

if __name__ == "__main__":
    parcer = Parser()
    tree = parcer.parse("2 * (2 + 3)")
    interpreter = Interpreter()
    print(interpreter.interpret(tree))
    tree = parcer.parse("2 * 2 + 3")
    print(interpreter.interpret(tree))
    