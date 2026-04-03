#!/usr/bin/env python3
"""
AL Analyzer - Core analysis logic
"""

import re
import string
from collections import Counter
from typing import Dict, List, Any


class ALAnalyzer:
 """
 AL (Automated Language) Analyzer
 Performs text analysis including:
 - Word frequency analysis
 - Sentence structure analysis
 - Readability metrics
 - Lexical diversity
 - Character statistics
 """

 def __init__(self):
 self.stop_words = self._load_stop_words()

 def _load_stop_words(self) -> set:
 """Load common English stop words."""
 return {
 "a", "an", "the", "and", "or", "but", "in", "on", "at", "to",
 "for", "of", "with", "by", "from", "up", "about", "into",
 "through", "during", "is", "are", "was", "were", "be", "been",
 "being", "have", "has", "had", "do", "does", "did", "will",
 "would", "could", "should", "may", "might", "shall", "can",
 "this", "that", "these", "those", "i", "you", "he", "she",
 "it", "we", "they", "what", "which", "who", "whom", "not",
 "no", "nor", "so", "yet", "both", "either", "neither", "each",
 "few", "more", "most", "other", "some", "such", "than", "too",
 "very", "just", "as", "if"
 }

 def tokenize(self, text: str) -> List[str]:
 """Tokenize text into words."""
 text = text.lower()
 words = re.findall(r"\b[a-z']+\b", text)
 return words

 def get_sentences(self, text: str) -> List[str]:
 """Split text into sentences."""
 sentences = re.split(r'(?<=[.!?])\s+', text.strip())
 return [s.strip() for s in sentences if s.strip()]

 def word_frequency(self, words: List[str]) -> Dict[str, int]:
 """Calculate word frequency."""
 return dict(Counter(words).most_common())

 def top_words(self, words: List[str], n: int = 10, exclude_stop_words: bool = True) -> List[tuple]:
 """Get top N most frequent words."""
 if exclude_stop_words:
 filtered = [w for w in words if w not in self.stop_words and len(w) > 1]
 else:
 filtered = words
 return Counter(filtered).most_common(n)

 def lexical_diversity(self, words: List[str]) -> float:
 """Calculate lexical diversity (type-token ratio)."""
 if not words:
 return 0.0
 unique_words = set(words)
 return round(len(unique_words) / len(words), 4)

 def average_word_length(self, words: List[str]) -> float:
 """Calculate average word length."""
 if not words:
 return 0.0
 total_length = sum(len(w) for w in words)
 return round(total_length / len(words), 2)

 def average_sentence_length(self, sentences: List[str]) -> float:
 """Calculate average sentence length in words."""
 if not sentences:
 return 0.0
 total_words = sum(len(self.tokenize(s)) for s in sentences)
 return round(total_words / len(sentences), 2)

 def flesch_reading_ease(self, text: str, words: List[str], sentences: List[str]) -> float:
 """
 Calculate Flesch Reading Ease score.
 Score interpretation:
 90-100: Very Easy
 80-90: Easy
 70-80: Fairly Easy
 60-70: Standard
 50-60: Fairly Difficult
 30-50: Difficult
 0-30: Very Confusing
 """
 if not words or not sentences:
 return 0.0

 num_words = len(words)
 num_sentences = len(sentences)
 num_syllables = sum(self._count_syllables(w) for w in words)

 if num_sentences == 0 or num_words == 0:
 return 0.0

 score = 206.835 - 1.015 * (num_words / num_sentences) - 84.6 * (num_syllables / num_words)
 return round(score, 2)

 def _count_syllables(self, word: str) -> int:
 """Estimate syllable count in a word."""
 word = word.lower().strip("'")
 if len(word) <= 3:
 return 1

 vowels = "aeiouy"
 count = 0
 prev_vowel = False

 for char in word:
 is_vowel = char in vowels
 if is_vowel and not prev_vowel:
 count += 1
 prev_vowel = is_vowel

 # Adjust for silent 'e' at end
 if word.endswith('e') and count > 1:
 count -= 1

 return max(1, count)

 def reading_ease_label(self, score: float) -> str:
 """Get human-readable label for Flesch score."""
 if score >= 90:
 return "Very Easy"
 elif score >= 80:
 return "Easy"
 elif score >= 70:
 return "Fairly Easy"
 elif score >= 60:
 return "Standard"
 elif score >= 50:
 return "Fairly Difficult"
 elif score >= 30:
 return "Difficult"
 else:
 return "Very Confusing"

 def character_stats(self, text: str) -> Dict[str, int]:
 """Analyze character composition."""
 return {
 "total_characters": len(text),
 "letters": sum(1 for c in text if c.isalpha()),
 "digits": sum(1 for c in text if c.isdigit()),
 "spaces": sum(1 for c in text if c.isspace()),
 "punctuation": sum(1 for c in text if c in string.punctuation),
 "uppercase": sum(1 for c in text if c.isupper()),
 "lowercase": sum(1 for c in text if c.islower()),
 }

 def detect_language_patterns(self, text: str) -> Dict[str, Any]:
 """Detect various language patterns."""
 patterns = {
 "has_questions": bool(re.search(r'\?', text)),
 "has_exclamations": bool(re.search(r'!', text)),
 "has_numbers": bool(re.search(r'\d', text)),
 "has_uppercase_words": bool(re.search(r'\b[A-Z]{2,}\b', text)),
 "has_quoted_text": bool(re.search(r'["\'].*?["\']', text)),
 "paragraph_count": len([p for p in text.split('\n\n') if p.strip()]),
 }
 return patterns

 def analyze(self, text: str) -> Dict[str, Any]:
 """Perform full analysis on the given text."""
 words = self.tokenize(text)
 sentences = self.get_sentences(text)
 freq = self.word_frequency(words)
 top = self.top_words(words, n=10)
 diversity = self.lexical_diversity(words)
 avg_word_len = self.average_word_length(words)
 avg_sent_len = self.average_sentence_length(sentences)
 flesch_score = self.flesch_reading_ease(text, words, sentences)
 char_stats = self.character_stats(text)
 lang_patterns = self.detect_language_patterns(text)

 return {
 "text": text,
 "word_count": len(words),
 "unique_word_count": len(set(words)),
 "sentence_count": len(sentences),
 "word_frequency": freq,
 "top_words": top,
 "lexical_diversity": diversity,
 "average_word_length": avg_word_len,
 "average_sentence_length": avg_sent_len,
 "flesch_reading_ease": flesch_score,
 "reading_ease_label": self.reading_ease_label(flesch_score),
 "character_stats": char_stats,
 "language_patterns": lang_patterns,
 }

 def print_report(self, results: Dict[str, Any]) -> None:
 """Print a formatted analysis report."""
 print("\n ANALYSIS REPORT")
 print("=" * 60)

 print("\n[TEXT STATISTICS]")
 print(f" Total Words : {results['word_count']}")
 print(f" Unique Words : {results['unique_word_count']}")
 print(f" Sentences : {results['sentence_count']}")
 print(f" Lexical Diversity : {results['lexical_diversity']} (0=low, 1=high)")
 print(f" Avg Word Length : {results['average_word_length']} chars")
 print(f" Avg Sentence Length : {results['average_sentence_length']} words")

 print("\n[READABILITY]")
 print(f" Flesch Score : {results['flesch_reading_ease']}")
 print(f" Reading Level : {results['reading_ease_label']}")

 print("\n[CHARACTER STATS]")
 cs = results["character_stats"]
 print(f" Total Characters : {cs['total_characters']}")
 print(f" Letters : {cs['letters']}")
 print(f" Digits : {cs['digits']}")
 print(f" Spaces : {cs['spaces']}")
 print(f" Punctuation : {cs['punctuation']}")
 print(f" Uppercase Letters : {cs['uppercase']}")
 print(f" Lowercase Letters : {cs['lowercase']}")

 print("\n[LANGUAGE PATTERNS]")
 lp = results["language_patterns"]
 print(f" Contains Questions : {lp['has_questions']}")
 print(f" Contains Exclamations : {lp['has_exclamations']}")
 print(f" Contains Numbers : {lp['has_numbers']}")
 print(f" Contains ALL-CAPS Words: {lp['has_uppercase_words']}")
 print(f" Contains Quoted Text : {lp['has_quoted_text']}")
 print(f" Paragraph Count : {lp['paragraph_count']}")

 print("\n[TOP 10 WORDS (excluding stop words)]")
 if results["top_words"]:
 for rank, (word, count) in enumerate(results["top_words"], 1):
 bar = "#" * count
 print(f" {rank:2}. {word:<20} {count:3}x {bar}")
 else:
 print(" No significant words found.")

 print("\n" + "=" * 60)
 print(" Analysis Complete")
 print("=" * 60)
