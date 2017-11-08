import random
from NLU_wrappers import *

# prefilled "database"


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

RSE_sentences_ON_pos = [
	"Wow, you've gotten a lot ^ at ^!",
	"Remember when you were ^ at ^?",
	"You've really improved at ^.",
	"You really understand ^ now, huh?"
]

RSE_sentences_ON_neg = [
	"I know you can do better.",
	"You still don't understand?",
	"You understood ^ last time."
]
prompt_sentences = [
	"So how was ^?",
	"What'd you do after last session?"
]

prompt_followups = [
	"How'd it go?",
	"Did you have fun?",
	"I wish I could've been there!"
]

SD_sentence_AGREEMENT = [
	"I like it too!",
	"I agree.",
	"Yeah! Me too!"
]

SD_sentence_DISAGREEMENT = [
	"Darn, I like ^.",
	"I'm the opposite, I actually like ^."
]

# assuming there are 10 KC's

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
	[0.2,2]   # KC 10

]

# reference_element = (valence, context, rapport)

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
		0: "basic algebra",
		1: "regular equations",
		2: "fractions",
		3: "exponents",
		3: "weird coefficients",
		4: "hard stuff",
		5: "fraction coefficients",
		6: "multi-step problems",
		7: "multi-variable questions",
		8: "hard questions",
		9: "expert problems",
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
	if mastery[KC][0] / mastery[KC][1] >= 0.1:
		valence = "pos"
	else: valence = "neg"
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
