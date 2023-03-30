import re

INPUT_ERROR = "Desculpe, não entendi o que você quis dizer. Por favor, tente novamente de outra forma.\n"


def parser(input):
    input = input.title()
    input = re.sub(
        '[^A-Za-záéíóúÁÉÍÓÚâêîôÂÊÎÔàèìòùÀÈÌÒÙãõÃÕçÇ\d\s.,]+', '', input)
    return input


def convertEdgeValuesToFloat(nodes):
    for i in range(2, len(nodes), 3):
        nodes[i] = float(nodes[i])


def getInput(type, message):
    while (True):
        try:
            if (type == "str"):
                userInput = str(input(message))
            if (type == "int"):
                userInput = int(input(message))
            if (type == "float"):
                userInput = float(input(message))
            return userInput
        except:
            print(INPUT_ERROR)
