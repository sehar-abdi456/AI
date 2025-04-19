from collections import defaultdict
import math

# Define the training data
training_data = [
    (["free", "money", "now"], "spam"),
    (["limited", "offer", "money"], "spam"),
    (["hello", "how", "are", "you"], "ham"),
    (["congratulations", "you", "win"], "spam"),
    (["meet", "me", "for", "lunch"], "ham"),
    (["free", "offer", "money"], "spam"),
    (["hello", "dear", "friend"], "ham"),
    (["money", "limited", "free"], "spam"),
    (["how", "are", "you", "today"], "ham")
]

# 3. Priors
def calculate_priors(data):
    total = len(data)
    spam = sum(1 for _, label in data if label == "spam")
    ham = total - spam
    return {
        "spam": spam / total,
        "ham": ham / total
    }


# 4. Likelihoods
# P(word|label)=count+1/totalwords+vocabsize
def calculate_likelihoods(data):
    word_counts = {"spam": defaultdict(int), "ham": defaultdict(int)}
    total_counts = {"spam": 0, "ham": 0}
    vocab = set()

    for words, label in data:
        for word in words:
            word_counts[label][word] += 1
            total_counts[label] += 1
            vocab.add(word)

    vocab_size = len(vocab)

    def likelihood(word, label):
        return (word_counts[label][word] + 1) / (total_counts[label] + vocab_size)

    return likelihood, vocab

# 5. Classify a new email
def classify(email_words, priors, likelihood_fn, vocab):
    log_probs = {}

    for label in ["spam", "ham"]:
        log_prob = math.log(priors[label])
        for word in email_words:
            log_prob += math.log(likelihood_fn(word, label))
        log_probs[label] = log_prob

    return max(log_probs, key=log_probs.get), log_probs

# 6. Run classification
priors = calculate_priors(training_data)
likelihood_fn, vocab = calculate_likelihoods(training_data)

test_email = ["free", "money", "lunch"]
result, log_probs = classify(test_email, priors, likelihood_fn, vocab)

print("Classified as:", result)
print("Log probabilities:", log_probs)

