# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

def text_sentiment(text):
    document = types.Document(
        content = text,
        type = enums.Document.Type.PLAIN_TEXT
        )
    sentiment = client.analyze_sentiment(document = document).document_sentiment
    return sentiment.score

def text_entities(text):
    """Detects entities in the text."""

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')
    entity_list = dict()

    for entity in entities:
        entity_list[entity.name] = (entity_type[entity.type], entity.salience)
    return entity_list
