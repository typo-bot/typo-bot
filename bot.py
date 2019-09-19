from dotenv import load_dotenv
import os
import subprocess
from spellchecker import SpellChecker
from pprint import pprint
import markdown

# Fetch env variables
load_dotenv()


def clone_repo(url):
    subprocess.run(["git", "clone", url, "repository"])


def clean_repo():
    subprocess.run(["rm", "-rf", "repository"])


def scan_repo(path):
    for i in os.scandir(path):
        if i.is_file() and (i.path.endswith('.md') or i.path.endswith('.rst')):
            read_file(i.path, i.path.endswith('.md'))
        elif i.is_dir():
            scan_repo(i.path)


def read_file(path, ismarkdown):
    file = open(path)
    text = file.read()

    if ismarkdown:
        print('MD')
        html = markdown.markdown(text)
        text = remove_html_tags(html)
        print(text)
    else:
        print('RST')


def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def check_words(words):
    spell = SpellChecker()

    misspelled = spell.unknown(words)

    for word in misspelled:
        print(spell.correction(word))
        print(spell.candidates(word))


# scan_repo("repository")
# clean_repo()
# clone_repo('https://github.com/typo-bot/typos')
# check_words(['analyze', 'anazlye'])

def try_text_razor():
    print(os.getenv('TEXTRAZOR_KEY'))


try_text_razor()
