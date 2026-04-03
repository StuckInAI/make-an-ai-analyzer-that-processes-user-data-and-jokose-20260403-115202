#!/usr/bin/env python3
"""
AL Analyzer - Main entry point
"""

from analyzer import ALAnalyzer


def main():
 print("=" * 60)
 print(" AL Analyzer ")
 print("=" * 60)

 analyzer = ALAnalyzer()

 # Example usage
 sample_text = input("Enter text to analyze (or press Enter for demo): ").strip()

 if not sample_text:
 sample_text = "The quick brown fox jumps over the lazy dog. This is a sample sentence for analysis."
 print(f"\nUsing demo text: {sample_text}")

 print("\n" + "-" * 60)
 results = analyzer.analyze(sample_text)
 analyzer.print_report(results)


if __name__ == "__main__":
 main()
