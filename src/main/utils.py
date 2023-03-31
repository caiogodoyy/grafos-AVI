import re

INPUT_ERROR = "Desculpe, não entendi o que você quis dizer. Por favor, tente novamente de outra forma.\n"
INPUT_FORMAT_ERROR = "Ops! Formato inválido. Por favor, verifique e tente novamente.\n"


def parser(input):
    input = input.title()
    input = re.sub(
        '[^A-Za-záéíóúÁÉÍÓÚâêîôÂÊÎÔàèìòùÀÈÌÒÙãõÃÕçÇ\d\s.,]+', '', input)
    return input


def convertEdgeValuesToFloat(nodes):
    try:
        for i in range(2, len(nodes), 3):
            nodes[i] = float(nodes[i])
        return True
    except:
        print(INPUT_FORMAT_ERROR)
        return False


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


def validateEdges(edges, state):
    if (state["isValued"]):
        if (len(edges) % 3 == 0):
            return True
        print(INPUT_FORMAT_ERROR)
        return False
    else:
        if (len(edges) % 2 == 0):
            return True
        print(INPUT_FORMAT_ERROR)
        return False
