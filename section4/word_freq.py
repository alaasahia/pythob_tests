def most_frequent_word(text: str) -> str:
    from collections import defaultdict

    # Normalize the string(not mentioned in the exercise to not to do so)
    text = text.lower()
    
    words = text.split()
    
  
    word_count = defaultdict(int)
    
    first_appearance = {}
    
    # Count the frequencies of each word
    for index, word in enumerate(words):
        if word not in first_appearance:
            first_appearance[word] = index
        word_count[word] += 1
    
    # Find the most frequent word
    max_frequency = 0
    most_frequent = None
    
    for word in word_count:
        if (word_count[word] > max_frequency) or (word_count[word] == max_frequency and first_appearance[word] < first_appearance[most_frequent]):
            max_frequency = word_count[word]
            most_frequent = word
    
    return most_frequent

