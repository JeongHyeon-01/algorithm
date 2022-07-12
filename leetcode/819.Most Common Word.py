import re, collections
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']

words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
print(words)
counts = collections.Counter(words)
print(collections.Counter(words))
print(counts.most_common(1)[0][0])