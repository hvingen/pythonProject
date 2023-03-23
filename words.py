from urllib.request import urlopen

# Hiermee worden de woorden opgehaald en als lijst geretourneerd.
def fetch_words():
	with urlopen('http://sixty-north.com/c/t.txt') as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
	return story_words


# Hiermee wordt een lijst woorden afgedrukt.
def print_words(story_words):
	for word in story_words:
		print(word)


def main():
	words = fetch_words()
	print_words(words)

if __name__=='__name_-':
	main()
