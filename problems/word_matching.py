def word_match(s, corpus):
    memo = dict()

    def match(i):
        if i > len(s):
            return None
        if i in memo:
            return memo[i]

        for j in range(i, len(s)):
            word = s[i:j+1]
            if word in corpus:
                if j + 1 == len(s):
                    memo[i] = [word]
                    return memo[i]
                if j + 1 < len(s) and match(j + 1):
                    memo[i] = [word] + memo[j + 1]
                    return memo[i]
        return None

    return match(0)


corpus = {'bed', 'bath', 'andbeyond', 'beyond'}
print(word_match('bedbathandbeyond', corpus))