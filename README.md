# User Modeling and Memory

## Major Milestones
|Milestone|Planning|In-Progress|Finished|
|:--------|:------:|:---------:|:------:|
|Lit Review                               |/| | | |
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

### Research Questions
__1. When to collect user data?__
- Personality recognition, especially in the five major categories are best collected during the first interaction. Especially when there is anxiety and stress [1,2].
  
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

__6. When to use the information?__

__7. How to use the information?__
- Ranking Advisor [7]
  

## Logistics
- Individual meeting with Michael on Wednesdays at 4:15PM
- Group meeting on Wednesdays at 5PM.

## General To-Do List for User Modeling and Memory

### Priority 1
- Read papers
- Think of large research questions

### Priority 2
- Start making an outline for lit review
