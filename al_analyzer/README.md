# AL Analyzer

A Python-based **Automated Language (AL) Analyzer** that performs comprehensive text analysis including readability metrics, word frequency analysis, lexical diversity, and more.

---

## Features

- **Word Frequency Analysis** - Count and rank word occurrences
- **Top Words** - Identify most frequent meaningful words (stop words excluded)
- **Lexical Diversity** - Type-Token Ratio (TTR) score
- **Readability Metrics** - Flesch Reading Ease score with human-readable labels
- **Sentence Analysis** - Sentence count and average sentence length
- **Character Statistics** - Breakdown of letters, digits, punctuation, spaces, case
- **Language Pattern Detection** - Detect questions, exclamations, numbers, quoted text, ALL-CAPS words

---

## Project Structure

```
al_analyzer/
├── main.py # Entry point / CLI
├── analyzer.py # Core ALAnalyzer class
├── tests/
│ └── test_analyzer.py # Unit tests
└── README.md # This file
```

---

## Requirements

- Python 3.7+
- No external dependencies (uses standard library only)

---

## Usage

### Run the Analyzer

```bash
cd al_analyzer
python main.py
```

You will be prompted to enter text. If you press Enter, a demo text will be used.

### Example Output

```
============================================================
 AL Analyzer
============================================================

Enter text to analyze (or press Enter for demo):

Using demo text: The quick brown fox jumps over the lazy dog. This is a sample sentence for analysis.

------------------------------------------------------------

 ANALYSIS REPORT
============================================================

[TEXT STATISTICS]
 Total Words : 16
 Unique Words : 16
 Sentences : 2
 Lexical Diversity : 1.0 (0=low, 1=high)
 Avg Word Length : 4.06 chars
 Avg Sentence Length : 8.0 words

[READABILITY]
 Flesch Score : 74.31
 Reading Level : Fairly Easy

[CHARACTER STATS]
 Total Characters : 84
 Letters : 67
 Digits : 0
 Spaces : 15
 Punctuation : 2
 Uppercase Letters : 2
 Lowercase Letters : 65

[LANGUAGE PATTERNS]
 Contains Questions : False
 Contains Exclamations : False
 Contains Numbers : False
 Contains ALL-CAPS Words: False
 Contains Quoted Text : False
 Paragraph Count : 1

[TOP 10 WORDS (excluding stop words)]
 1. quick 1x #
 2. brown 1x #
 3. fox 1x #
 4. jumps 1x #
 5. lazy 1x #
 6. dog 1x #
 7. sample 1x #
 8. sentence 1x #
 9. analysis 1x #

============================================================
 Analysis Complete
============================================================
```

---

## Running Tests

```bash
cd al_analyzer
python -m pytest tests/ -v
```

Or directly:

```bash
python tests/test_analyzer.py
```

---

## API Reference

### `ALAnalyzer`

| Method | Description |
|---|---|
| `analyze(text)` | Run full analysis, returns dict of results |
| `tokenize(text)` | Tokenize text into lowercase word list |
| `get_sentences(text)` | Split text into sentences |
| `word_frequency(words)` | Count word occurrences |
| `top_words(words, n, exclude_stop_words)` | Get top N words |
| `lexical_diversity(words)` | Compute TTR score (0.0 - 1.0) |
| `average_word_length(words)` | Average number of chars per word |
| `average_sentence_length(sentences)` | Average words per sentence |
| `flesch_reading_ease(text, words, sentences)` | Compute Flesch readability score |
| `reading_ease_label(score)` | Human-readable label for Flesch score |
| `character_stats(text)` | Character-level statistics |
| `detect_language_patterns(text)` | Detect language patterns |
| `print_report(results)` | Pretty-print analysis results |

---

## Readability Score Guide

| Score | Level |
|---|---|
| 90 - 100 | Very Easy |
| 80 - 90 | Easy |
| 70 - 80 | Fairly Easy |
| 60 - 70 | Standard |
| 50 - 60 | Fairly Difficult |
| 30 - 50 | Difficult |
| 0 - 30 | Very Confusing |

---

## License

MIT License
