from typing import Dict


def count_letter_a(s: str) -> int:
    freq_table: Dict[str, int] = {
        "a": 0,
    }

    for char in s:
        if char.lower() != "a":
            continue
        freq_table["a"] += 1

    return freq_table["a"]


if __name__ == "__main__":

    user_input = input("Digite uma string: ")
    count = count_letter_a(user_input)

    if count > 0:
        print(f"A letra 'a' aparece {count} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")
