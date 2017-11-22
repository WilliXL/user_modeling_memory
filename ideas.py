import random
from NLU_wrappers import *
import pandas as pd
import os
import time # to log when things are said

# prefilled "database"


def get_sentences(sentence_type, sentence_df):
    ret_list = []
    for row in range(len(sentence_df)):
        if list(sentence_df['type'])[row] == sentence_type:
            ret_list.append(list(sentence_df['sentence'])[row])
    return ret_list

def get_user_speech():
    s = input('The user says: ')
    return s

def get_rapport_delta():
    return random.randint(-2,2)

def get_valence():
    return random.choice(["pos", "neg"])

def get_event_type(event):
    mapping = {
        "soccer game": ("play", "soccer")
    }
    return mapping[event]

def count_insertions(sentence):
    count = 0
    for c in sentence:
        if c == '^':
            count += 1
    return count

mastery = [

    [0.8,10], # KC 1
    [0.8,7],  # KC 2
    [0.7,7],  # KC 3
    [0.6,3],  # KC 4
    [0.8,4],  # KC 5
    [0.5,3],  # KC 6
    [0.6,9],  # KC 7
    [0.4,4],  # KC 8
    [0.3,3],  # KC 9
    [0.2,2],  # KC 10
    [0,5,3],  # KC 11
    [0.8,10], # KC 12
    [0.4,4],  # KC 13
    [0.3,4]   # KC 14

    ]

# reference_element = (sentiment, entity, rapport, time)

student_references = {

    "soccer": [("pos", "NONE", 2),
        ("pos", "soccer game", 1),
        ("neg", "fouling", -1)],

    "fractions": [("neg", "NONE", -3),
        ("pos", "Question 3", 0),
        ("neg", "Question 4", -1)],

    }

agent_references = {
    "soccer": [("pos", "AGREEMENT", 1)]
    # "fractions": [("pos", "DISAGREEMENT", 0)]
    }

def KC_num_str(KC):
    dictionary = {
    0:  "variables on one side",
    1:  "variables on one side",
    2:  "variables on both sides",
    3:  "variable 1st (not sure how to paraphrase)",
    4:  "variable 2nd (not sure how to paraphrase)",
    5:  "unsimplified variables",
    6:  "variables by themself",
    7:  "variables with a constant",
    8:  "variables with a negative constant",
    9:  "coefficients of one",
    10: "negative coefficients",
    11: "integer coefficients",
    12: "fraction coefficients",
    13: "variables in the denominator"
    }
    return dictionary[KC]

def RSE_base(valence, KC):
    if valence == "pos":
        sentence = random.choice(RSE_sentences_ON_pos)
        insertions = count_insertions(sentence)
    if insertions == 1:
        sentence = sentence[:sentence.index("^")] + KC_num_str(KC) + sentence[sentence.index("^")+1:]
    if insertions == 2:
        sentence = sentence[:sentence.index("^")] + "better" + sentence[sentence.index("^")+1:]
        sentence = sentence[:sentence.index("^")] + KC_num_str(KC) + sentence[sentence.index("^")+1:]
    return sentence

    if valence == "neg":
        sentence = random.choice(RSE_sentences_ON_neg)
        insertions = count_insertions(sentence)
    if insertions == 1:
        sentence = sentence[:sentence.index("^")] + KC_num_str(KC) + sentence[sentence.index("^")+1:]
    return sentence

# KC input should be spec'd as: [KC, 0, KC, 0, KC, KC, KC, 0, 0, 0]

def RSE(KCs):
    # for i in range(len(KCs) - 1, 0, -1):
    # 	if KCs[i] != 0:
    # 		KC = KC[i]
    KC = random.randint(0,9)
    valence = get_valence()
    return RSE_base(valence, KC)

def get_alignment(agent_valence, tag):
    for param in student_references[tag]:
        if param[1] == "NONE":
            if agent_valence == param[0]:
                return "AGREEMENT"
            else:
                return "DISAGREEMENT"
    return None

def SD(tag):
    agent_valence = get_valence()
    alignment = get_alignment(agent_valence,tag)
    if alignment == None:
        return None
    else:
        if alignment == "AGREEMENT":
            sentence = random.choice(SD_sentence_AGREEMENT)
        return sentence
        if alignment == "DISAGREEMENT":
            sentence = random.choice(SD_sentence_DISAGREEMENT)
        if "^" in sentence:
            sentence = sentence[:sentence.index("^")] + tag + sentence[sentence.index("^")+1:]
        return sentence
    return None


def prompt_SD(tag):
    sentence = random.choice(prompt_sentences)
    if "^" in sentence:
        sentence = sentence[:sentence.index("^")] + tag + sentence[sentence.index("^")+1:]
    return sentence


def follow_up():
    sentence = random.choice(prompt_followups)
    return sentence

def highest_salience(entity_list):
    high_val = 0
    index = 0
    for entry in range(len(entity_list)):
        if entity_list[entry][2] > high_val:
            high_val = entity_list[entry][2]
            index = entry
    if len(entity_list) > 0:
        return entity_list[index][0]

def append_to_user(entity, sentiment, delta_rapport, user_df):
    if entity in list(user_df['topic']):

    user_df.loc[len(user_df)] = [entity, sentiment, delta_rapport, time.time()]
    return user_df

def run():
    # NOT SAFE: assuming that proper csv files already exist
    sentence_df = pd.read_csv("sentences.csv")
    user_df = pd.read_csv("user.csv")
    agent_df = pd.read_csv("agent.csv")

    # we have pre-filled data, now have conversation
    
    prompt_sentences = get_sentences("prompt_sentences",sentence_df)
    prompt_sentence = random.choice(prompt_sentences)
    print(prompt_sentence)
    while True:
        user_response = get_user_speech()
        sentiment = text_sentiment(user_response)
        entity_list = text_entities(user_response)
        entity = highest_salience(entity_list)
        print(entity)
        delta_rapport = get_rapport_delta()
        user_df = append_to_user(entity, sentiment, delta_rapport, user_df)
        user_df.to_csv("user.csv")
        user_df = pd.read_csv("user.csv")
        followups = get_sentences("prompt_followups", sentence_df)
        followup = random.choice(followups)
        print(followup)
