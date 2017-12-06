from prototype import *
import random

def run_student_new():
    # make sure that these CSV files already exist!!
    # else these operations are unsafe and will crash the program
    sentence_df = pd.read_csv('sentences.csv')
    user_df = pd.read_csv('student_off.csv')
    agent_df = pd.read_csv('agent_off.csv')

    memo = set()
    entity = ""
    while True:
        prompt_sentences = get_sentences('prompt_sentences_new', sentence_df)
        prompt_sentence = random.choice(prompt_sentences)
        while prompt_sentence in memo:
            prompt_sentence = random.choice(prompt_sentences)
        memo.add(prompt_sentence)

        print(prompt_sentence)
        user_response = get_user_speech()
        sentiment = text_sentiment(user_response)
        entity_list = text_entities(user_response)
        entity = highest_salience(entity_list)
        delta_rapport = get_rapport_delta()
        user_df = append_student_off(entity, sentiment, delta_rapport)
        dict_to_csv()
        
        turns = get_turns()
        for followup_turns in range(turns):
            followups = get_sentences('prompt_followups_new', sentence_df)
            followup = random.choice(followups)
            delta_rapport = get_rapport_delta()
            followup = insert_entity(followup, entity)
            while followup in memo:
                followup = random.choice(followups)
                followup = insert_entity(followup, entity)
            memo.add(followup)
            print(followup)
            user_response = get_user_speech()
            sentiment = text_sentiment(user_response)
            delta_rapport = get_rapport_delta()
            user_df = append_student_off(entity, sentiment, delta_rapport)
            dict_to_csv()
        entity = ""
    


def run_student_returning():
    # make sure that these CSV files already exist!!
    # else these operations are unsafe and will crash the program
    sentence_df = pd.read_csv('sentences.csv')
    user_df = pd.read_csv('student_off.csv')
    agent_df = pd.read_csv('agent_off.csv')

    memo = set()
    entity = get_topic(user_df)
    while True:
        prompt_sentences = get_sentences('prompt_sentences', sentence_df)
        prompt_sentence = random.choice(prompt_sentences)
        
        if '^' in prompt_sentence:
            print(entity)
            prompt_sentence = insert_entity(prompt_sentence, entity)
            while prompt_sentence in memo:
                prompt_sentence = random.choice(prompt_sentences)
                prompt_sentence = insert_entity(prompt_sentence, entity)
            memo.add(prompt_sentence)
            print(prompt_sentence)
            user_response = get_user_speech()
            sentiment = text_sentiment(user_response)
            delta_rapport = get_rapport_delta()
            user_df = append_student_off(entity, sentiment, delta_rapport)
            dict_to_csv()
        else:
            while prompt_sentence in memo:
                prompt_sentence = random.choice(prompt_sentences)
            memo.add(prompt_sentence)
            print(prompt_sentence)
            user_response = get_user_speech()
            sentiment = text_sentiment(user_response)
            entity_list = text_entities(user_response)
            entity = highest_salience(entity_list)
            delta_rapport = get_rapport_delta()
            user_df = append_student_off(entity, sentiment, delta_rapport)
            dict_to_csv()

def run_recall_hint():
    # make sure that these CSV files already exist!!
    # else these operations are unsafe and will crash the program
    sentence_df = pd.read_csv('sentences.csv')
    user_df = pd.read_csv('student_on.csv')
    agent_df = pd.read_csv('agent_on.csv')

    
