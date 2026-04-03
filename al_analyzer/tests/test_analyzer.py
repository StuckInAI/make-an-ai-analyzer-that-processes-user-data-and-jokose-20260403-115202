#!/usr/bin/env python3
"""
Unit tests for ALAnalyzer
"""

import sys
import os
import unittest

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analyzer import ALAnalyzer


class TestALAnalyzer(unittest.TestCase):

 def setUp(self):
 self.analyzer = ALAnalyzer()
 self.sample_text = (
 "The quick brown fox jumps over the lazy dog. "
 "This is a sample sentence for analysis. "
 "Can you analyze this text effectively?"
 )

 # -------------------------
 # Tokenization Tests
 # -------------------------

 def test_tokenize_basic(self):
 words = self.analyzer.tokenize("Hello World")
 self.assertEqual(words, ["hello", "world"])

 def test_tokenize_punctuation(self):
 words = self.analyzer.tokenize("Hello, World!")
 self.assertEqual(words, ["hello", "world"])

 def test_tokenize_empty(self):
 words = self.analyzer.tokenize("")
 self.assertEqual(words, [])

 def test_tokenize_numbers(self):
 words = self.analyzer.tokenize("I have 3 cats")
 self.assertEqual(words, ["i", "have", "cats"])

 # -------------------------
 # Sentence Tests
 # -------------------------

 def test_get_sentences_basic(self):
 sentences = self.analyzer.get_sentences("Hello. World.")
 self.assertEqual(len(sentences), 2)

 def test_get_sentences_question(self):
 sentences = self.analyzer.get_sentences("How are you? I am fine.")
 self.assertEqual(len(sentences), 2)

 def test_get_sentences_empty(self):
 sentences = self.analyzer.get_sentences("")
 self.assertEqual(sentences, [])

 # -------------------------
 # Word Frequency Tests
 # -------------------------

 def test_word_frequency(self):
 words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
 freq = self.analyzer.word_frequency(words)
 self.assertEqual(freq["apple"], 3)
 self.assertEqual(freq["banana"], 2)
 self.assertEqual(freq["cherry"], 1)

 def test_word_frequency_empty(self):
 freq = self.analyzer.word_frequency([])
 self.assertEqual(freq, {})

 # -------------------------
 # Lexical Diversity Tests
 # -------------------------

 def test_lexical_diversity_all_unique(self):
 words = ["apple", "banana", "cherry"]
 diversity = self.analyzer.lexical_diversity(words)
 self.assertEqual(diversity, 1.0)

 def test_lexical_diversity_all_same(self):
 words = ["apple", "apple", "apple"]
 diversity = self.analyzer.lexical_diversity(words)
 self.assertAlmostEqual(diversity, 0.3333, places=3)

 def test_lexical_diversity_empty(self):
 diversity = self.analyzer.lexical_diversity([])
 self.assertEqual(diversity, 0.0)

 # -------------------------
 # Average Word Length Tests
 # -------------------------

 def test_average_word_length(self):
 words = ["hi", "hello", "hey"]
 avg = self.analyzer.average_word_length(words)
 # (2 + 5 + 3) / 3 = 3.33
 self.assertAlmostEqual(avg, 3.33, places=2)

 def test_average_word_length_empty(self):
 avg = self.analyzer.average_word_length([])
 self.assertEqual(avg, 0.0)

 # -------------------------
 # Syllable Count Tests
 # -------------------------

 def test_count_syllables_simple(self):
 self.assertEqual(self.analyzer._count_syllables("cat"), 1)
 self.assertEqual(self.analyzer._count_syllables("apple"), 2)
 self.assertEqual(self.analyzer._count_syllables("beautiful"), 3)

 def test_count_syllables_short_word(self):
 # Words <= 3 chars return 1
 self.assertEqual(self.analyzer._count_syllables("a"), 1)
 self.assertEqual(self.analyzer._count_syllables("the"), 1)

 # -------------------------
 # Flesch Reading Ease Tests
 # -------------------------

 def test_flesch_score_range(self):
 words = self.analyzer.tokenize(self.sample_text)
 sentences = self.analyzer.get_sentences(self.sample_text)
 score = self.analyzer.flesch_reading_ease(self.sample_text, words, sentences)
 # Score should be a reasonable float
 self.assertIsInstance(score, float)
 self.assertGreater(score, -100)
 self.assertLess(score, 200)

 def test_flesch_empty(self):
 score = self.analyzer.flesch_reading_ease("", [], [])
 self.assertEqual(score, 0.0)

 # -------------------------
 # Reading Ease Label Tests
 # -------------------------

 def test_reading_ease_labels(self):
 self.assertEqual(self.analyzer.reading_ease_label(95), "Very Easy")
 self.assertEqual(self.analyzer.reading_ease_label(85), "Easy")
 self.assertEqual(self.analyzer.reading_ease_label(75), "Fairly Easy")
 self.assertEqual(self.analyzer.reading_ease_label(65), "Standard")
 self.assertEqual(self.analyzer.reading_ease_label(55), "Fairly Difficult")
 self.assertEqual(self.analyzer.reading_ease_label(40), "Difficult")
 self.assertEqual(self.analyzer.reading_ease_label(10), "Very Confusing")

 # -------------------------
 # Character Stats Tests
 # -------------------------

 def test_character_stats(self):
 stats = self.analyzer.character_stats("Hello World!")
 self.assertEqual(stats["total_characters"], 12)
 self.assertEqual(stats["letters"], 10)
 self.assertEqual(stats["spaces"], 1)
 self.assertEqual(stats["punctuation"], 1)
 self.assertEqual(stats["uppercase"], 2)
 self.assertEqual(stats["lowercase"], 8)
 self.assertEqual(stats["digits"], 0)

 def test_character_stats_empty(self):
 stats = self.analyzer.character_stats("")
 for key in stats:
 self.assertEqual(stats[key], 0)

 # -------------------------
 # Language Pattern Tests
 # -------------------------

 def test_detect_questions(self):
 patterns = self.analyzer.detect_language_patterns("Is this a question?")
 self.assertTrue(patterns["has_questions"])

 def test_detect_exclamations(self):
 patterns = self.analyzer.detect_language_patterns("Wow!")
 self.assertTrue(patterns["has_exclamations"])

 def test_detect_numbers(self):
 patterns = self.analyzer.detect_language_patterns("I have 5 apples.")
 self.assertTrue(patterns["has_numbers"])

 def test_detect_no_numbers(self):
 patterns = self.analyzer.detect_language_patterns("No numbers here.")
 self.assertFalse(patterns["has_numbers"])

 def test_detect_uppercase_words(self):
 patterns = self.analyzer.detect_language_patterns("This is NASA.")
 self.assertTrue(patterns["has_uppercase_words"])

 def test_detect_quoted_text(self):
 patterns = self.analyzer.detect_language_patterns('He said "hello".') 
 self.assertTrue(patterns["has_quoted_text"])

 # -------------------------
 # Full Analysis Tests
 # -------------------------

 def test_analyze_returns_all_keys(self):
 results = self.analyzer.analyze(self.sample_text)
 expected_keys = [
 "text", "word_count", "unique_word_count", "sentence_count",
 "word_frequency", "top_words", "lexical_diversity",
 "average_word_length", "average_sentence_length",
 "flesch_reading_ease", "reading_ease_label",
 "character_stats", "language_patterns"
 ]
 for key in expected_keys:
 self.assertIn(key, results, f"Missing key: {key}")

 def test_analyze_word_count(self):
 results = self.analyzer.analyze("Hello world how are you")
 self.assertEqual(results["word_count"], 5)

 def test_analyze_sentence_count(self):
 results = self.analyzer.analyze("Hello. World. Goodbye.")
 self.assertEqual(results["sentence_count"], 3)

 def test_analyze_empty_text(self):
 results = self.analyzer.analyze("")
 self.assertEqual(results["word_count"], 0)
 self.assertEqual(results["sentence_count"], 0)
 self.assertEqual(results["lexical_diversity"], 0.0)


if __name__ == "__main__":
 unittest.main(verbose=2)
