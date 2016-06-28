# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 16:24:04 2014

@author: davidp
"""

from nltk.corpus import wordnet as wn

def get_synonyms(word):
    """Gets wordnet synonyms for the given word"""
    synsets = [];
    syns = wn.synsets(word)
    for ss in syns:
        lemmas = []
        for l in ss.lemmas():
            lemma = { "name": l.name(), "related_forms": [] }
            for x in l.derivationally_related_forms():
                lemma['related_forms'].append(x.name())
            lemmas.append(lemma)
        synsets.append({
            "lemmas": lemmas,
            "d": ss.definition(),
            "pos": ss.pos(),
            "id": ss.name()
        })
    return synsets

def get_hypernyms(word):
    """Gets parent synonyms for a specific lemma from wordnet"""
    syn = wn.synsets(word)
    hnyms = []
    for h in syn[0].hypernyms():
        hnyms.append({
            "lemmas": h.lemma_names(),
            "d": h.definition(),
            "pos": h.pos(),
            "id": h.name()
        })
    return hnyms

def get_hyponyms(word):
    """Gets child synonyms from wordnet"""
    syn = wn.synsets(word)
    hnyms = []
    for h in syn[0].hyponyms():
        print h
        hnyms.append({
            "lemmas": h.lemma_names(),
            "d": h.definition(),
            "pos": h.pos(),
            "id": h.name()
        })
    return hnyms
