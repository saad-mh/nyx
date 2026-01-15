def word_count(text):
    return len(text.split())

def summarize_length(text):
    return {
        "characters": len(text),
        "words": len(text.split())
    }

def reverse_text(text):
    return text[::-1]

# print("word count: ", word_count("Hello world! This is a test."))
# print("summary: ", summarize_length("Hello world! This is a test."))
# print("reversed text: ", reverse_text("Hello world! This is a test."))