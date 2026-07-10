# Lecture 7: Bag of Words (BoW)

## What is Bag of Words (BoW)?

**Definition:** Bag of Words (BoW) is a text vectorization technique that converts text into numerical vectors by counting the frequency of each word. It ignores grammar and word order and only focuses on how many times a word appears.

**Purpose:** Convert text into numbers so Machine Learning algorithms can understand it.

---

## NLP Pipeline Before Applying BoW

Raw Text
↓
Text Cleaning
↓
Lowercase Conversion
↓
Tokenization
↓
Stop Words Removal
↓
Stemming/Lemmatization
↓
Bag of Words
↓
Machine Learning Model

**Note:** BoW is applied **after text preprocessing**, not directly on raw text.

---

## Example

### Raw Sentences

```text
I am playing cricket.
I play cricket every day.
```

### After Text Preprocessing

```text
play cricket
play cricket every day
```

### Create Vocabulary

| Word |
|------|
| play |
| cricket |
| every |
| day |

### Create Feature Vectors

| Sentence | play | cricket | every | day |
|----------|-----:|--------:|------:|----:|
| play cricket | 1 | 1 | 0 | 0 |
| play cricket every day | 1 | 1 | 1 | 1 |

Each row represents one sentence as a numerical vector.

---

## How BoW Works

1. Collect all documents.
2. Clean the text.
3. Create a vocabulary of unique words.
4. Count the frequency of each word.
5. Generate a feature vector for every document.

---

## Advantages

- Simple and easy to implement.
- Easy to understand.
- Works well for small datasets.
- Good baseline for text classification.

---

## Disadvantages

- Ignores word order.
- Ignores word meaning.
- Produces sparse vectors.
- Vocabulary becomes very large for big datasets.

---

## Python Library

```python
from sklearn.feature_extraction.text import CountVectorizer
```

**Library:** `scikit-learn`

**Class:** `CountVectorizer`

---

## Quick Revision

- BoW = Count the frequency of words.
- Apply BoW after text preprocessing.
- Uses CountVectorizer.
- Ignores grammar and word order.
- Output is a numerical feature vector.