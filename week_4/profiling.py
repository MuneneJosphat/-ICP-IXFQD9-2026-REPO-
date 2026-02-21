import cProfile
import pstats
import io
import sys
import os

# Allow imports from repo root
sys.path.insert(0, os.path.abspath("."))

from week_4.model import SpamClassifier

DATA_PATH = "week_2/data/SMSSpamCollection"

def run():
    clf = SpamClassifier()
    clf.train(DATA_PATH)

    # Simulate 100 predictions
    test_messages = [
        "Free entry in 2 a weekly comp to win cash!",
        "Hey, are we meeting tomorrow?",
        "WINNER! You have been selected for a prize.",
        "Can you call me back later?",
    ] * 25  # 100 total

    for msg in test_messages:
        clf.predict(msg)

if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    run()
    pr.disable()

    stream = io.StringIO()
    ps = pstats.Stats(pr, stream=stream).sort_stats("cumulative")
    ps.print_stats(15)  # top 15 slowest calls

    print(stream.getvalue())
    print("Profiling done. See above for top 15 slowest calls.")
