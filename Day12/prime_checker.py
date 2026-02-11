def is_prime(num):
    div_numbs = []
    for i in range(1, num + 1):
        if num%i == 0:
            div_numbs.append(i)
        else:
            continue
    
    if len(div_numbs) == 2:
        return True
    return False

print(is_prime(2))