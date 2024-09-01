def single_root_words(root_word, *other_words):
    same_words = []  # Создаем список для хранения подходящих слов
    root_word_lower = root_word.lower()  # Приводим корневое слово к нижнему регистру

    # Перебираем все слова в other_words
    for word in other_words:
        word_lower = word.lower()  # Приводим текущее слово к нижнему регистру
        # Проверяем, содержится ли одно слово в другом
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)  # Добавляем слово в список, если условие выполнено

    return same_words  # Возвращаем список подходящих слов

# Вызовы функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результата на экран
print(result1)
print(result2)