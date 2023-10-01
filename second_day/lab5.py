def substring(str):
    current_substring = str[0]
    longest_substring = str[0]

    for i in range(1, len(str)):
        if str[i] >= str[i-1]:
            current_substring += str[i]
        else:
            current_substring = str[i]

        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring

    return longest_substring

sample = input("enter a string : ")
if isinstance(sample,str):
    print(substring(sample))
