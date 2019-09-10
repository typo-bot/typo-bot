from dotenv import load_dotenv
import os
import subprocess
from spellchecker import SpellChecker
from pprint import pprint


# Fetch env variables
# load_dotenv()
# print(os.getenv('GITHUB_TOKEN'))

def clonerepo(url):
    subprocess.run(["git", "clone", url, "repository"])


def cleanrepo():
    subprocess.run(["rm", "-rf", "repository"])


def scanrepo(path):
    for i in os.scandir(path):
        if i.is_file() and (i.path.endswith('.md') or i.path.endswith('.rst')):
            readfile(i.path)
        elif i.is_dir():
            scanrepo(i.path)


def readfile(path):
    file = open(path)
    text = file.read()
    pprint(text)


def checkwords(words):
    spell = SpellChecker()

    misspelled = spell.unknown(words)

    for word in misspelled:
        print(spell.correction(word))
        print(spell.candidates(word))


scanrepo("repository")
# scleanrepo()
# clonerepo('https://github.com/laravel/laravel')
# checkwords(['analyze', 'anazlye'])
