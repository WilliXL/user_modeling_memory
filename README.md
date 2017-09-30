# User Modeling and Memory

## Major Milestones
|Milestone|Planning|In-Progress|Finished|
|:--------|:------:|:---------:|:------:|
|[Lit Review](https://cmu.box.com/s/v9noffkys5u9ub7r70inrnjpspc2sj2x) |/| | | |
|Method Planning                          | | | | |
|Data Analysis                            | | | | |
|Final Report                             | | | | |

## Breakdown
### Lit Review
Papers:
- [1] Mairesse, F., & Walker, M. (2000). Words Mark the Nerds: Computational Models of Personality Recognition through Language. 28th Annual Conference of the Cognitive Science Society, (May), 543–548.
  > Spoken language is easier to model than written (which is good for us!) We can be constantly updating personality trait values through these decision trees.
- [2] Mairesse, F., Walker, M. A., Mehl, M. R., & Moore, R. K. (2007). Using linguistic cues for the automatic recognition of personality in conversation and text. Journal of Artificial Intelligence Research, 30, 457–500.
- [3] Schulman, D., & Bickmore, T. (2012). Changes in verbal and nonverbal conversational behavior in long-term interaction. Proceedings of the 14th ACM International Conference on Multimodal Interaction - ICMI ’12, 11.
  > Looks at how nonverbal behavior changes as a function of time/rapport.
Would be interesting to combine with Rishabh to create changing animations in the virtual agent.
- [4] Komatani, K., Ueno, S., Kawahara, T., & Okuno, H. G. (2003). Flexible Guidance Generation using User Model in Spoken Dialogue Systems, (July), 256–263.
  > Looks at the dimensions of what to collect about a user. In this case it's a virtual, dialogue-based assistant for navigating Kyoto's bus system.
- [5] van Beek, P. (1987). A model for generating better explanations. Proceedings of the 25th Annual Meeting on Association for Computational Linguistics -, 215–220.
  > Looks at how to use the goal and plans (in the long term) of the user should influence the explanation that a system output. Could be interesting collaboration with on-the-fly dialogue generation. But how would goals be inferred/stored?
- [6] Baker, R., Corbett, a., Koedinger, K., & Roll, I. (2005). Detecting when students game the system, across tutor subjects and classroom cohorts. User Modeling 2005, 150–150.
  > Students who don't actually want to learn and want to "game the system" could be dealt with differently in terms of what their goal is.
- [7] Carberry, S., Chu-Carroll, J., & Elzer, S. (1999). Constructing and Utilizing a Model of User Preferences in Collaborative Consultation Dialogues. Computational Intelligence, 15(3), 185–217.
  > Similar to using goals and plans [5] except that users not conscious of their preferences, unlike their goals. Could be stored the same way as goals. Dialogue affected by goals/plans as well as preferences seem like they will take on similar external features. Expands upon van Beek [5] with weights for preferences as well.
- [8] Kass, R., & Finin, T. (1988). MODELING THE USER IN NATURAL LANGUAGE SYSTEMS Robert Kass and Tim Finin, 14(3).
  > Good base knowledge and specs for what a "user model" should be.
- [9] Kobsa, A., & Wahlster, W. (1989). User Models in Dialog Systems.
- [10] Kobsa, A. (1990). User modeling in dialog systems: Potentials and hazards. AI & Society, 4(3), 214–231.
- [11] Iio, T., Shiomi, M., Shinozawa, K., Shimohara, K., Miki, M., & Hagita, N. (2015). Lexical Entrainment in Human Robot Interaction: Do Humans Use Their Vocabulary to Robots? International Journal of Social Robotics, 7(2), 253–263.
- [12] Kanashiro, I., Kobayashi, K., & Kitamura, Y. (2009). Entrainment in human-agent text communication. Lecture Notes in Computer Science (Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 5044 LNAI, 268–277.

### Base Questions
__0. What is a "User Model"?__
- "A user model is the knowledge about the user, either explicitly or implicitly encoded, that is used by the system to improve the interaction" [8].
  - "This definition is at once too strong and too weak. The definition is too strong in that it limits the range of modeling a natural language system might do to the user of the system only. Many situations require a natural language system to deal with several models concur- rently, as will be demonstrated later in this paper. The definition is too weak since it endows every interactive system with some kind of user model, usually of the implicit variety. The following paragraphs clarify these issues, and in so doing restrict the class of models to be considered" [8].

__1. When to collect user data?__
- Personality recognition, especially in the five major categories are best collected during the first interaction. Especially when there is anxiety and stress [1,2].
- After self-disclosure prompts littered throughout trial.
  
__2. What to collect?__
- Potential dimensions of what to store?
  - Skill level to the system =?= confidence in the system, knowledge of the target domain (algebra), ~degree of hastiness~, rapport (?) [4].
  - The five major personality categories: Extraversion, Neuroticism, Agreeableness, Conscientiousness, Openness to Experience [1,2].
  - Goals and plans of the user [5]. As well as preferences [7].

__3. Can "skill level in system" be an analogue to "confidence in system"?__
- Talk to Rae about this.

__4. How to collect?__
- Goals and plans
  - Could be inferred simply from the task at hand in terms of simply what algebra concept the student is trying to learn. But could also incorporate whether or not the student actually wants to learn or not, which can be inferred from how often and much they are trying to Game-HURT the system [6].
  - At a more granular, the goal would be to solve the problem. And the agent could explain why solving the problem a certain way or why the incorrect method is a direct influence on the user's higher domain goal (ie. learn algebra) [5,6].
  - Another goal could be attaining higher rapport ratings, up until a certain threshold maybe? (ie. if beginning_rapport < max_rapport / 2)
- Preferences [7]
  - Volunteered-background
  - Volunteered
  - Q&A

__5. How to store all of the information?__
- From the highest level down, definitely there should be a distinction between user goals/preferences/personality and responses generated from algebra problem solving aspect.

__6. When to use the information?__

__7. How to use the information?__
- Ranking Advisor [7]

### Research Questions
-	How often should the RAPT user model be updated and how quickly show the influences of those changes propagate through the system for the most increase in rapport and maintain rapport longitudinally across trials?
  

## Logistics
- Individual meeting with Michael on Wednesdays at 4:15PM
- Group meeting on Wednesdays at 5PM.

## General To-Do List for User Modeling and Memory

### Priority 1
- Read papers
- Think of large research questions

### Priority 2
- Start making an outline for lit review
