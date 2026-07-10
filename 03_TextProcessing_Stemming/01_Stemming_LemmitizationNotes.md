# Lecture 4: Stemming & Lemmatization

## Stemming

**Definition:** Stemming is the process of reducing a word to its root (stem) by removing prefixes or suffixes. The resulting stem may or may not be a valid English word.

**Purpose:** It groups similar words together so that they are treated as the same word during text processing.

**Examples**

| Original Word | Stem |
|--------------|------|
| playing | play |
| played | play |
| plays | play |
| player | player |
| studies | studi |
| studying | studi |
| history | histori |

**Input**
```text
The boys are playing and studied together.
```

**After Stemming**
```text
The boy are play and studi together.
```

**Advantages**
- Fast and simple.
- Reduces vocabulary size.
- Improves search and text matching.

**Disadvantages**
- May produce invalid words.
- Meaning of the word can be lost.
- Less accurate than lemmatization.

---

## Popular Stemming Algorithms

### Porter Stemmer
- Most widely used stemming algorithm.
- Fast and suitable for many NLP tasks.
- May produce incorrect stems.

**Example**

| Word | Porter Stem |
|------|-------------|
| connecting | connect |
| studies | studi |
| happiness | happi |

### Snowball Stemmer
- Improved version of Porter Stemmer.
- Supports multiple languages.
- Slightly more accurate.

### Lancaster Stemmer
- Very aggressive stemming algorithm.
- Removes more characters than Porter.
- Can generate overly short stems.

**Example**

| Word | Lancaster Stem |
|------|----------------|
| maximum | maxim |
| running | run |
| happiness | happy |

---

## Lemmatization

**Definition:** Lemmatization is the process of converting a word into its base dictionary form, called the **lemma**. It uses vocabulary and grammar rules to find the correct root word.

**Purpose:** It preserves the actual meaning of the word while reducing different forms to a common base.

**Examples**

| Original Word | Lemma |
|--------------|-------|
| playing | play |
| played | play |
| studies | study |
| better | good |
| am | be |
| is | be |
| are | be |
| running | run |

**Input**
```text
The children are running in the park.
```

**After Lemmatization**
```text
The child be run in the park.
```

---

## Why Lemmatization is Better

Unlike stemming, lemmatization returns meaningful dictionary words.

**Example**

| Word | Stemming | Lemmatization |
|------|----------|---------------|
| studies | studi | study |
| caring | care | care |
| better | better | good |
| am | am | be |

---

## Stemming vs Lemmatization

| Feature | Stemming | Lemmatization |
|---------|----------|---------------|
| Output | May not be a valid word | Always a valid dictionary word |
| Speed | Faster | Slower |
| Accuracy | Lower | Higher |
| Uses Grammar Rules | No | Yes |
| Uses Dictionary | No | Yes |
| Meaning Preserved | Not always | Yes |

---

## When to Use Stemming

- Search engines
- Information retrieval
- Large datasets
- Fast preprocessing

---

## When to Use Lemmatization

- Chatbots
- Machine translation
- Question answering
- Text summarization
- Sentiment analysis
- Applications where meaning is important

---

## Interview Questions

**Q1. What is Stemming?**  
Stemming is the process of removing prefixes or suffixes to obtain the root form of a word. The output may not be a valid English word.

**Q2. What is Lemmatization?**  
Lemmatization converts a word into its dictionary base form using grammar rules and vocabulary.

**Q3. Which is more accurate: Stemming or Lemmatization?**  
Lemmatization is more accurate because it returns meaningful dictionary words.

**Q4. Why is Stemming faster than Lemmatization?**  
Because stemming simply removes prefixes or suffixes without checking grammar or a dictionary.

**Q5. Give one example where stemming fails.**

| Original | Stem | Lemma |
|----------|------|-------|
| studies | studi | study |
| better | better | good |

---

## Quick Revision

- **Stemming:** Removes prefixes/suffixes to get a stem.
- **Stem:** May not be a valid English word.
- **Lemmatization:** Converts a word to its dictionary base form (lemma).
- **Lemma:** Always a meaningful dictionary word.
- **Stemming:** Fast but less accurate.
- **Lemmatization:** Slower but more accurate.
- **Porter, Snowball, Lancaster:** Popular stemming algorithms.
- **Use Stemming:** Speed is important.
- **Use Lemmatization:** Meaning and accuracy are important.