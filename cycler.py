from collections import OrderedDict


def calculate_training_max(weight, repetitions):
    constant = 0.0333
    training_percentage = 0.9
    return round(((weight * repetitions * constant) +
                  weight) *
                  training_percentage)


def round_weight(weight, base=5):
    return base * round(weight / base)


def get_cycle_weights(training_weight,
                 first_set_percentage,
                 second_set_percentage,
                 third_set_percentage):
    return [round_weight(training_weight * first_set_percentage),
            round_weight(training_weight * second_set_percentage),
            round_weight(training_weight * third_set_percentage)]


def print_cycles(bench_max):
    program = {
        'warm up':
        {'first_set': {'percentage': .4, 'repetitions': '5'},
         'second_set': {'percentage': .5, 'repetitions': '5'},
         'third_set': {'percentage': .6, 'repetitions': '5'}},
        'week 1':
        {'first_set': {'percentage': .65, 'repetitions': '5'},
         'second_set': {'percentage': .75, 'repetitions': '5'},
         'third_set': {'percentage': .85, 'repetitions': '5+'}},
        'week 2':
        {'first_set': {'percentage': .7, 'repetitions': '3'},
         'second_set': {'percentage': .8, 'repetitions': '3'},
         'third_set': {'percentage': .9, 'repetitions': '3+'}},
        'week 3':
        {'first_set': {'percentage': .75, 'repetitions': '5'},
         'second_set': {'percentage': .85, 'repetitions': '35'},
         'third_set': {'percentage': .95, 'repetitions': '1+'}}}

    program = OrderedDict(sorted(program.items(), key=lambda t: t[0]))

    for key in program:
        weights = get_cycle_weights(bench_max,
                                    program[key]['first_set']['percentage'],
                                    program[key]['second_set']['percentage'],
                                    program[key]['third_set']['percentage'])
        print(key)
        for weight in weights:
            print('{} x {}'.format(weight,
                                   program[key]['first_set']['repetitions']))
        print()


def main():
    bench_max = calculate_training_max(150, 10)
    print_cycles(bench_max)

if __name__ == '__main__':
    main()
