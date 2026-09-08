import re
class WorkFrequencyCounter:
  def __init__(self):
    pass
  
  def preprocess_text(self, text):
    # remove special characters
    # convert to lowercase
    # split words (means tokenize)

    text1 = re.sub(r'[^a-zA-Z ]', '', text)
    text2 = text1.lower()
    text3 = text2.split(" ")
    return text3

  def compute_word_frequency(self, words):
    res = {}
    for word in words:
      if word in res:
        res[word] += 1
      else:
        res[word] = 1
    return res

  def get_most_frequent_word(self, freq_dict):
    count = 0
    word = ""
    for key, val in freq_dict.items():
      if val > count:
        count = val
        word = key
    return (word, count)

  def filter_words_by_frequency(self, freq_dict, n):
    res = {}
    for key, val in freq_dict.items():
      if val > n:
        res[key] = val
    return res
    
  

obj = WorkFrequencyCounter()
print(obj.preprocess_text("Hello, hello! How are you?"))
print(obj.compute_word_frequency(['hello', 'hello', 'how', 'are', 'you']))
print(obj.get_most_frequent_word({'hello': 2, 'how': 1, 'are': 1, 'you': 1}))
print(obj.filter_words_by_frequency({'hello': 3, 'how': 1, 'are': 2, 'you': 1}, 1))


