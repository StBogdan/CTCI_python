def get_system_word_list(file_path="/usr/share/dict/words"):
    with open(file_path, "r") as system_words_file:
        big_list = list(map(lambda word: word.lower(),
                            system_words_file.read().split("\n")))
    return big_list