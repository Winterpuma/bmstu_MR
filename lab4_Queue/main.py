from event_model import event_model
from step_model import step_model

from distributions import EvenDistribution, NormalDistribution


def main():
    a, b = 1, 10
    generator = EvenDistribution(a, b)

    mu, sigma = 4, 0.2  # диапазон +- [3;5]
    processor = NormalDistribution(mu, sigma)

    total_tasks = 1000
    repeat_percentage = 0
    step = 0.01

    print('event_model:', event_model(generator, processor, total_tasks, repeat_percentage))
    print('step_model:', step_model(generator, processor, total_tasks, repeat_percentage, step))


if __name__ == '__main__':
    main()
