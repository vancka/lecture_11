import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as json_file:
        seq = json.load(json_file)

    return seq[field]

def linear_search(seq, num):
    indices = list()
    count = 0

    idx = 0
    while idx < len(seq):
        if seq[idx] == num:
            indices.append(idx)
            count = count + 1
        idx = idx + 1
    return {"position": indices, "count": count}


def main():
    seq = read_data("sequential.json", "unordered_numbers")
    print(seq)
    result = linear_search(seq, num=5)
    print(result)


if __name__ == '__main__':
    main()