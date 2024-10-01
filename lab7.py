phonebook = {
    "Іванов": "111-211-782",
    "Петров": "231-566-897",
    "Сидоров": "344-666-777",
    "Зеленський": "486-456-755",
    "Шевченко": "33-222-444",
    "Кучма": "322-911-228",
    "Захарченко": "786-432-951",
    "Литвиненко": "274-785-578",
    "Ланістер": "356-234-567",
    "Бондарь": "888-335-678"
}


def print_phonebook(phonebook):
    for surname, phone in phonebook.items():
        print(f"{surname}: {phone}")

def add_record(phonebook):
    surname = input("Введіть прізвище: ")
    phone = input("Введіть номер телефону: ")
    phonebook[surname] = phone
    print(f"Запис додано: {surname} -> {phone}")

def delete_record(phonebook):
    surname = input("Введіть прізвище, яке потрібно видалити: ")
    if surname in phonebook:
        del phonebook[surname]
        print(f"Запис видалено: {surname}")
    else:
        print(f"Запис з прізвищем {surname} не знайдено.")

def print_sorted_phonebook(phonebook):
    for surname in sorted(phonebook.keys()):
        print(f"{surname}: {phonebook[surname]}")

def find_phone_by_surname(phonebook):
    surname = input("Введіть прізвище для пошуку номера телефону: ")
    phone = phonebook.get(surname)
    if phone:
        print(f"Номер телефону для {surname}: {phone}")
    else:
        print(f"{surname} не знайдено у телефонній книзі.")

def find_surname_by_phone(phonebook):
    phone = input("Введіть номер телефону для пошуку прізвища: ")
    for surname, number in phonebook.items():
        if number == phone:
            print(f"Номер телефону {phone} належить {surname}")
            return
    print(f"Номер телефону {phone} не знайдено у телефонній книзі.")

def menu():
    while True:
        print("\nМеню:")
        print("1. Вивести всі записи")
        print("2. Додати новий запис")
        print("3. Видалити запис")
        print("4. Вивести записи за відсортованими прізвищами")
        print("5. Знайти номер телефону за прізвищем")
        print("6. Знайти прізвище за номером телефону")
        print("7. Вийти")

        choice = input("Виберіть дію (1-7): ")

        if choice == "1":
            print_phonebook(phonebook)
        elif choice == "2":
            add_record(phonebook)
        elif choice == "3":
            delete_record(phonebook)
        elif choice == "4":
            print_sorted_phonebook(phonebook)
        elif choice == "5":
            find_phone_by_surname(phonebook)
        elif choice == "6":
            find_surname_by_phone(phonebook)
        elif choice == "7":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")

menu()