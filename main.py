import time

start_time = time.time()


# num1 and num2 are strings with numbers and letters
# returns possible solution by adding num1 and num2
# not numeric sum is always "-"
# carrying from every not numeric sum is 0
def find_possible_sum(n1, n2):
    sum_result = list()
    carry = 0
    
    for d1, d2 in zip(reversed(n1), reversed(n2)):
        if not (d1.isnumeric() and d2.isnumeric()):
            sum_result.append('-')
            carry = 0
            continue
        
        sum_result.append(str(int(d1)+int(d2)+carry)[-1])
        carry = 0 if int(d1)+int(d2) < 10 else 1
    
    first_element = [str(carry)] if sum_result[-1] != '-' else ['-']
    return ''.join(first_element + list(reversed(sum_result)))


# replaces letters in the word with existing numbers in the numbered_letters
def substitute_letters(word, nl):
    return ''.join([nl[c] if c in nl else '-' for c in word])


# returns numbers that we haven't used yet in the numbered_letters
def not_used_numbers(nl):
    return [i for i in map(lambda x: str(x), range(10)) if i not in nl.values()]


# nl is numbered_letters
def check_result(nl):
    word1_replaced = substitute_letters(word1, nl)
    word2_replaced = substitute_letters(word2, nl)
    result_replaced = substitute_letters(result, nl)

    words_sum = find_possible_sum(word1_replaced, word2_replaced)

    for c1, c2 in zip(result_replaced, words_sum):
        if c1.isnumeric() and c2.isnumeric() and c1 != c2 and int(c1) != int(c2)+1:
            return False
    return True


# returns all possible values for a specific character c (which are satisfying following condition: word1+word2=result)
def possible_numbers(letter, nl):
    numbers = list()
    tmp_nl = nl.copy()

    for e in not_used_numbers(nl):
        tmp_nl[letter] = e
        if check_result(tmp_nl):
            numbers.append(e)
    
    return numbers


# returns the best letter to be replaced with a number (has the least possible values)
def best_letter(nl):
    possibilities = dict()

    for letter in letters:
        if letter not in nl:
            possibilities[letter] = possible_numbers(letter, nl)
    best_key = sorted(possibilities, key=lambda x: len(possibilities[x]))[0]
    
    return best_key, possibilities[best_key]


def smm_solve(nl):
    if len(letters) == len(nl):
        return nl
    if not check_result(nl):
        return False

    tmp_nl = nl.copy()
    letter, values = best_letter(nl)

    for e in values:
        tmp_nl[letter] = e
        solved_nl = smm_solve(tmp_nl)
        if solved_nl:
            nl = solved_nl
            return solved_nl


if __name__ == '__main__':
    word1 = 'SEND'
    word2 = 'MORE'
    result = 'MONEY'
    letters = list(set(word1 + word2 + result))

    print(smm_solve(dict()))

print(f'Executing time: {round(time.time()-start_time, 5)} seconds')