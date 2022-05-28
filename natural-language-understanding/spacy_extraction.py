import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("play the song magic")

# for token in doc:
    # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #       token.shape_, token.is_alpha, token.is_stop)
    # print(token.text, token.tag_)

# doc = nlp(u"#bbuzz 2016: Rafał Kuć - Running High Performance And Fault Tolerant Elasticsearch")
for entity in doc.ents:
  print(entity.label_, ' | ', entity.text)