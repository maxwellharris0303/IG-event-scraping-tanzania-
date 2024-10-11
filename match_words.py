def find_matching_words(str1, str2):
    # Convert both strings to lowercase and split them into words
    words1 = set(str1.lower().split())
    words2 = set(str2.lower().split())

    # Find the intersection of both sets and convert it to a list
    matching_words = list(words1.intersection(words2))

    return matching_words

# # Example usage
# str1 = "Wheelchair accessible parking lot"
# str2 = "Car"

# matches = find_matching_words(str1, str2)
# print("Matching words:", matches)
