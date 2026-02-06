def calculate_love_score(name1, name2):
    names_lst = list(name1 + name2)
    checkers = ["true", "love"]
    total = ""
    
    for word in checkers:
        word_total = 0
        for letter in word:
            word_count = names_lst.count(letter.lower())
            # if word_count == 1:
            #     print(f"{letter.upper()} ocurrs {word_count} time")
            # else:
            #     # print(f"{letter.upper()} ocurrs {word_count} times")
            word_total += word_count
        
        total += str(word_total)
        # print(f"Total = {word_total}")

    print(int(total))