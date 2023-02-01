from algorithms import IsAnagram, KthLargest
import logging


def main() -> None:
    logging.basicConfig(filename='my.logs', filemode='w', encoding='utf-8', level=logging.INFO, format=logging.BASIC_FORMAT)
    obj = IsAnagram('dog', 'god')
    logging.info(f'Starting {obj.__class__.__name__} algorithm')
    obj.compute_by_hash()
    obj.compute_by_counter()
    obj.compute_by_sorting()
    obj = KthLargest([1, 2, 3], 1)
    logging.info(f'Starting {obj.__class__.__name__} algorithm')
    obj.compute_kth()


if __name__ == '__main__':
    main()
