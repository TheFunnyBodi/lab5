import locale
import re

# Українська мова для правильного сортування
locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

# Функція для сортування слів
def sort_key(word):
    lower_word = word.lower()
    if 'а' <= lower_word[0] <= 'я' or lower_word[0] in 'єґіїї':
        return (0, locale.strxfrm(lower_word))
    else:
        return (1, lower_word)

# Функція для видалення знаків пунктуації
def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

# Функція для читання файлу
def process_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Витягнення першого речення
        first_sentence = content.split('.')[0]
        print("Перше речення:")
        print(first_sentence)

        words = remove_punctuation(content).split()
        words.sort(key=sort_key)

        print("\nВідсортовані слова:")
        print(words)
        print(f"\nКількість слів: {len(words)}")

    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {str(e)}")

# Виклик функції з назвою файлу
process_file('text_file.txt')
