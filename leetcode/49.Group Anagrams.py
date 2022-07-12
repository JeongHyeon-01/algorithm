import collections
strs = ["eat","tea","tan","ate","nat","bat"]

# anagrams = collections.defaultdict(list)
# print(anagrams)
#
#
# for word in strs:
#     print(sorted(word))
#     anagrams[''.join(sorted(word))].append(word)
#     print(anagrams)
# print(list(anagrams.values()))


answer = collections.defaultdict(list)
print(answer)

for word in strs:
    answer[''.join(sorted(word))].append(word)
