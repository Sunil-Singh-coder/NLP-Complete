# Lecture 6: One-Hot Encoding

## What is One-Hot Encoding?

**Definition:** One-Hot Encoding (OHE) is a vectorization technique that converts words into binary vectors (0s and 1s). Each unique word in the vocabulary is represented by a unique vector.

**Purpose:** It converts text into a numerical format so that machine learning models can understand it.

---

## How One-Hot Encoding Works

### Step 1: Create a Vocabulary

```text
I love NLP
```

**Vocabulary**

| Word | Index |
|------|------:|
| I | 0 |
| love | 1 |
| NLP | 2 |

Vocabulary Size = **3**

---

### Step 2: Create Binary Vectors

| Word | Vector |
|------|---------------|
| I | [1, 0, 0] |
| love | [0, 1, 0] |
| NLP | [0, 0, 1] |

Each vector contains **only one '1'**, while the remaining values are **0**.

---

## Example

**Sentence**
```text
I love NLP
```

**One-Hot Vectors**
```text
I     → [1, 0, 0]
love  → [0, 1, 0]
NLP   → [0, 0, 1]
```

---

## Why is One-Hot Encoding Needed?

Machine learning algorithms cannot understand text directly. They only work with numbers. One-Hot Encoding converts words into numerical vectors.

---

## Advantages

- Simple and easy to implement.
- Easy to understand.
- No mathematical calculations are required.
- Works well for small vocabularies.

---

## Disadvantages

- Creates very large vectors for large vocabularies.
- Sparse vectors (mostly 0s).
- Does not capture the meaning of words.
- Cannot show relationships between similar words.

**Example**

```text
King → [1,0,0]
Queen → [0,1,0]
```

Although **King** and **Queen** are related in meaning, One-Hot Encoding treats them as completely different.

---

## Real-Life Limitation

If a dataset contains **10,000 unique words**, each word will have a vector of length **10,000**. This increases memory usage and computation time.

---

## Interview Questions

**Q1. What is One-Hot Encoding?**  
One-Hot Encoding is a technique that converts words into binary vectors containing one '1' and the remaining values as '0'.

**Q2. Why do we use One-Hot Encoding?**  
To convert text into numbers so machine learning models can process it.

**Q3. What is the biggest disadvantage of One-Hot Encoding?**  
It creates high-dimensional sparse vectors and cannot capture semantic meaning.

---

## Quick Revision

- **One-Hot Encoding = Text → Binary Vector**
- Each word gets a unique vector.
- Vector contains only one **1**.
- Simple and easy to use.
- Works well for small datasets.
- Poor for large vocabularies.
- Cannot understand word meaning or similarity.