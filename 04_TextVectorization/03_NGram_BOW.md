# Lecture 8: N-Grams

## What are N-Grams?

**Definition:** An N-Gram is a sequence of **N consecutive words** from a sentence. It is used to capture the relationship between nearby words.

**Purpose:** Unlike Bag of Words, N-Grams preserve some word order, making the text representation more meaningful.

---

## Types of N-Grams

### 1. Unigram (N = 1)

One word at a time.

**Sentence**
```text
I love NLP
```

**Output**
```text
["I", "love", "NLP"]
```

---

### 2. Bigram (N = 2)

Two consecutive words.

**Sentence**
```text
I love NLP
```

**Output**
```text
["I love", "love NLP"]
```

---

### 3. Trigram (N = 3)

Three consecutive words.

**Sentence**
```text
I love learning NLP
```

**Output**
```text
["I love learning", "love learning NLP"]
```

---

## Example

**Sentence**
```text
Machine Learning is awesome
```

| N-Gram | Output |
|--------|--------|
| Unigram | Machine, Learning, is, awesome |
| Bigram | Machine Learning, Learning is, is awesome |
| Trigram | Machine Learning is, Learning is awesome |

---

## Advantages

- Preserves word order.
- Captures nearby word relationships.
- Better than Bag of Words for understanding phrases.

---

## Disadvantages

- Vocabulary size increases quickly.
- Requires more memory.
- Higher values of N create sparse vectors.

---

## Python Library

```python
from sklearn.feature_extraction.text import CountVectorizer
```

**Example**
```python
CountVectorizer(ngram_range=(2,2))   # Bigram
CountVectorizer(ngram_range=(3,3))   # Trigram
CountVectorizer(ngram_range=(1,2))   # Unigram + Bigram
```

---

## Interview Questions

**Q1. What is an N-Gram?**  
A sequence of N consecutive words in a sentence.

**Q2. What is the difference between Unigram and Bigram?**  
- Unigram contains one word.
- Bigram contains two consecutive words.

**Q3. Why are N-Grams better than Bag of Words?**  
Because they preserve some word order and capture relationships between neighboring words.

---

## Quick Revision

- **Unigram = 1 Word**
- **Bigram = 2 Consecutive Words**
- **Trigram = 3 Consecutive Words**
- Preserves word order.
- Better than BoW for phrases.
- Implemented using **CountVectorizer** with `ngram_range`.