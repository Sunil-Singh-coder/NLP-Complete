# Lecture 3: Tokenization & Basic Terminology

## What is NLP?
**Natural Language Processing (NLP)** is a branch of Artificial Intelligence (AI) that enables computers to understand, process, analyze, and generate human language. Since computers understand only numbers, NLP converts human language into a machine-readable format.

**Example:** `I am learning NLP.`

---

## Basic Terminology

### Text
A **text** is any collection of words or characters.

**Example:** `I love AI.`

### Corpus
A **corpus** is a large collection of text documents used to train or evaluate NLP models.

**Example:** 1000 news articles together form a corpus.

### Document
A **document** is a single text file inside a corpus.

**Example:** `news1.txt`

### Sentence
A **sentence** is a group of words that expresses a complete idea.

**Example:** `Python is easy.`

### Word
A **word** is the smallest meaningful unit of a sentence.

**Example:** `I`, `love`, `Python`

### Character
A **character** is the smallest unit of text.

**Example:** `P`, `y`, `t`, `h`, `o`, `n`

---

## Tokenization

**Definition:** Tokenization is the process of breaking text into smaller units called **tokens**.

**Input**
```text
I love Natural Language Processing.
```

**Output**
```text
["I", "love", "Natural", "Language", "Processing", "."]
```

### Why Tokenization?
- Makes text easier to process.
- Helps computers analyze each word separately.
- First preprocessing step in almost every NLP pipeline.

---

## Types of Tokenization

### 1. Sentence Tokenization
Splits a paragraph into individual sentences.

**Input**
```text
I love AI. Python is easy.
```

**Output**
```text
["I love AI.", "Python is easy."]
```

### 2. Word Tokenization
Splits a sentence into words.

**Input**
```text
I love Python.
```

**Output**
```text
["I", "love", "Python", "."]
```

### 3. Character Tokenization
Splits text into individual characters.

**Input**
```text
CAT
```

**Output**
```text
["C", "A", "T"]
```

### 4. Subword Tokenization
Used by modern LLMs like **GPT** and **BERT**. It splits words into meaningful subwords.

**Example**
```text
unbelievable
```

**Output**
```text
["un", "believe", "able"]
```

**Advantage:** It can understand unseen or rare words by combining known subwords.

---

## Importance of Tokenization
- Word counting
- Text preprocessing
- Feature extraction
- Sentiment analysis
- Machine learning
- Chatbots
- Large Language Models (LLMs)

---

## Challenges
- `can't` → `["can't"]` or `["can", "n't"]`
- `Mr.` should not always end a sentence.
- Different languages require different tokenization rules.

---

## Interview Questions

**Q1. What is Tokenization?**  
Tokenization is the process of splitting text into smaller units called tokens.

**Q2. What is a Corpus?**  
A corpus is a collection of text documents.

**Q3. Difference between Corpus and Document?**

| Corpus | Document |
|--------|----------|
| Collection of documents | Single document |

**Q4. Name the types of Tokenization.**
- Sentence
- Word
- Character
- Subword

---

## Quick Revision
- **Corpus:** Collection of documents
- **Document:** Single text file
- **Sentence:** Group of words
- **Word:** Meaningful unit
- **Character:** Smallest text unit
- **Tokenization:** Splitting text into tokens
- **Types:** Sentence, Word, Character, Subword
- **Modern LLMs:** Use Subword Tokenization