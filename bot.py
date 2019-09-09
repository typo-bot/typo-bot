from spellchecker import SpellChecker

spell = SpellChecker()

misspelled = spell.unknown(['analyze', 'anazlye'])

for word in misspelled:
    print(spell.correction(word))
    print(spell.candidates(word))
