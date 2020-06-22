string=input("Enter any string:")
def most_frequent(string):
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d


def frequency(string):
    frequencies = most_frequent(string)
    frequency_list = [(freq, letter) for (letter, freq) in frequencies.items()]
    frequency_list.sort(reverse=True)
    print(frequencies)
    print("After sorting it in decreasing order of frequency:")
    print(frequency_list)
    return [letter for freq, letter in frequency_list]

print(frequency(string))
