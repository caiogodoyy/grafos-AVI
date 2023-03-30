import re


def parser(input):
    input = input.title()
    input = re.sub(
        '[^A-Za-záéíóúÁÉÍÓÚâêîôÂÊÎÔàèìòùÀÈÌÒÙãõÃÕçÇ\d\s.,]+', '', input)
    return input

def convertEdgeValuesToFloat(nodes):
    for i in range(2, len(nodes), 3):
        nodes[i] = float(nodes[i])
