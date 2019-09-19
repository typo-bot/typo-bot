from dotenv import load_dotenv
import os
import textrazor

load_dotenv()
textrazor.api_key = os.getenv('TEXTRAZOR_KEY')

client = textrazor.TextRazor(extractors=["entities", "topics"])
response = client.analyze_url("https://github.com/typo-bot/typos")

for entity in response.entities():
    print (entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types)