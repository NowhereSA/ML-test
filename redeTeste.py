import math

input = -1
output_desire = 1
input_weight = 0.5
learning_rate = 0.01


def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

print(f'Entrada {input}, Desejado {output_desire}')

iteration = 0

bias = 1
bias_weight = 0.5

error = math.inf
while not error == 0:

    iteration += 1
    print(iteration)
    sum = (input * input_weight) + (bias * bias_weight)
    print(f'Peso {input_weight}')

    output = activation(sum)
    print(f'Saída {output}')

    error = output_desire - output
    print(f'O erro foi {error}')

    if not error == 0:
        input_weight += (learning_rate * input * error)
        bias_weight += (learning_rate * bias * error)

print(f'Saída {output}, Desejado {output_desire}')
