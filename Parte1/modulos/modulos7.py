import sys


def fetch_words(file):
    with open(file, 'r') as story:
        story_words = []
        for line in story:
            line_words = line.split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main():
    file = sys.argv[1]
    words = fetch_words(file)
    print_items(words)


if __name__ == '__main__':
    main()