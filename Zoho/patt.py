def look_and_say(n):
    if n == 1:
        return "1"
    prev_term = "1"
    for var in range(n - 1):
        new_term = ""
        count = 1
        for i in range(1, len(prev_term)):
            if prev_term[i] == prev_term[i - 1]:
                count += 1
            else:
                new_term += str(count) + prev_term[i - 1]
                count = 1
        new_term += str(count) + prev_term[-1]
        prev_term = new_term
    return prev_term

# Example usage:
terms_to_generate = int(input("Enter a number of row U want : "))
for i in range(1, terms_to_generate + 1):
    print(look_and_say(i))
