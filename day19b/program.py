from program_lib import calculate

# result = calculate("data.txt", 129)
# print(result)

# 0: 8 11
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31

# 0: 42*n 31*m ; n > m ; n > 2 and m > 1

def is_match(message, options42, options31):
    if len(message) % 8 != 0:
        return False

    count42 = 0
    count31 = 0
    while message:
        if message[0:8] in options42:
            count42 += 1
            message = message[8:]
        else:
            break
    while message:
        if message[0:8] in options31:
            count31 += 1
            message = message[8:]
            if count42 <= count31:
                return False
        else:
            return False
    if count42 < 2 or count31 < 1:
        return False

    return True


file_name = "data.txt"
n = 129

fo = open(file_name, "r+")
lines = fo.readlines()
received_messages = [line.strip() for line in lines[n+1:]]

options42 = {'abbbbbba', 'abbbabba', 'abbbaaba', 'abbaabba', 'abbabbba', 'abaabbba', 'abaababa', 'abaaabba', 'abaaaaba', 'ababaaba', 'abaaaaaa', 'abbbaaaa', 'abbaaaaa', 'abbbbaaa', 'ababbaaa', 'abaabaaa', 'abababaa', 'ababbbaa', 'abaabbaa', 'abbaabaa', 'abbbabaa', 'abbbaaab', 'abbaabab', 'abbbbbab', 'abaabbab', 'abababbb', 'abaabbbb', 'abbbaabb', 'ababaabb', 'ababbabb', 'aaaabbbb', 'aaaababb', 'aaaabaab', 'aaaaabbb', 'aaaaaabb', 'aaaaaaab', 'aaabbaab', 'aaababbb', 'aaababaa', 'aaabbbaa', 'aaababba', 'aaabbbba', 'aaabaaba', 'aaabbaba', 'aaaababa', 'aabbabba', 'aabbaaba', 'aabbaaaa', 'aabbbaaa', 'aabbbbab', 'aabbbaab', 'aabbabab', 'aabbaaab', 'aabbaabb', 'aabbbabb', 'aababbbb', 'aababbab', 'aababbaa', 'aababaab', 'aabababb', 'aabaabbb', 'aabaabaa', 'aabaabba', 'bbbbbbbb', 'bbbababb', 'bbbabbbb', 'bbbaabbb', 'bbaaabbb', 'bbabbbbb', 'bbababbb', 'bbaaaabb', 'bbabaabb', 'babbbabb', 'babababb', 'babaaabb', 'baabbabb', 'baaababb', 'baaaaabb', 'babaabbb', 'babbabbb', 'baababbb', 'babbbbbb', 'baaabbab', 'baaaaaab', 'babbbbab', 'babbbaab', 'babbabab', 'babbaaab', 'bababbab', 'bababaab', 'babaabab', 'babaaaab', 'bbbabbab', 'bbbbbbab', 'bbbbabab', 'bbaaaaab', 'bbbaaaab', 'bbbbbaab', 'baababaa', 'baaabbaa', 'baaaaaaa', 'baabbaaa', 'baabaaaa', 'babbbaaa', 'bababbaa', 'bababaaa', 'babaabaa', 'babaaaaa', 'bbabaaaa', 'bbbbaaaa', 'bbbabaaa', 'bbaabbaa', 'bbabbbaa', 'bbbabbaa', 'bbbababa', 'bbbabbba', 'bbbaabba', 'bbbbbaba', 'bbbbabba', 'bbaaaaba', 'bbabaaba', 'bbaaabba', 'baaaabba', 'baababba', 'baabaaba', 'babbbaba', 'babababa', 'bababbba'}
options31 = {'abaaabaa', 'ababaaaa', 'abababba', 'ababbbba', 'ababbaba', 'abbbbbaa', 'abbabaaa', 'abbabbaa', 'abbbbaba', 'abbaaaba', 'abbababa', 'abaababb', 'abbbbabb', 'abbababb', 'abaaaabb', 'abbaaabb', 'abbabbbb', 'abbbbbbb', 'ababbbbb', 'abaaabbb', 'abbbabbb', 'abbaabbb', 'abbbbaab', 'abbabaab', 'abbaaaab', 'ababbaab', 'ababaaab', 'abaabaab', 'abaaaaab', 'abaaabab', 'ababbbab', 'abababab', 'abbbabab', 'abbabbab', 'aabbbbaa', 'aabbbbba', 'aabbbaba', 'aabbbbbb', 'aabbabbb', 'aabbabaa', 'aabaaabb', 'aabaabab', 'aabaaaab', 'aabaaaba', 'aababbba', 'aabababa', 'aabaaaaa', 'aababaaa', 'aaaabaaa', 'aaaabbba', 'aaaabbaa', 'aaaaabba', 'aaaaabaa', 'aaaaaaba', 'aaaaaaaa', 'aaabbaaa', 'aaabaaaa', 'aaabbbbb', 'aaabaabb', 'aaabbabb', 'aaabbbab', 'aaababab', 'aaabaaab', 'aaaaabab', 'aaaabbab', 'baabbaba', 'baabbbba', 'baabbbaa', 'baaabbba', 'baaababa', 'baaabaaa', 'baaaabaa', 'baaaaaba', 'baaabaab', 'baaaabab', 'baabbbab', 'baabbaab', 'baababab', 'baabaaab', 'baabbbbb', 'baabaabb', 'baaaabbb', 'baaabbbb', 'babbaabb', 'bababbbb', 'babaabba', 'babbbbba', 'babbabba', 'babaaaba', 'babbaaba', 'babbabaa', 'babbbbaa', 'babbaaaa', 'bbaaabaa', 'bbababaa', 'bbabbaaa', 'bbaabaaa', 'bbaaaaaa', 'bbbbbaaa', 'bbbaaaaa', 'bbbaabaa', 'bbbbbbaa', 'bbbbabaa', 'bbabbaba', 'bbabbbba', 'bbababba', 'bbaababa', 'bbaabbba', 'bbbaaaba', 'bbbbaaba', 'bbbbbbba', 'bbbbabbb', 'bbbaaabb', 'bbbbbabb', 'bbbbaabb', 'bbabbabb', 'bbaababb', 'bbaabbbb', 'bbabaaab', 'bbabbaab', 'bbaabaab', 'bbbbaaab', 'bbbabaab', 'bbabbbab', 'bbababab', 'bbaabbab', 'bbaaabab', 'bbbaabab'}

total = 0
for message in received_messages:
    if is_match(message, options42, options31):
        total += 1

print(total)