introduction = 'The tarot is a pack of playing cards, used from at least the mid-15th century in various parts of Europe to play games such as Italian tarocchini, French tarot and Austrian Königrufen, many of which are still played today. You can read more about Tarot cards on this website: "https://www.tarot.com/tarot/cards"'

instructions_1 = "To start with, you will choose your questions among these fives:"
question_1 = "[1] How is my current relationship with my partner?"
question_2 = "[2] How will my love life in general in the next 6 months is going to go?"
question_3 = "[3] How is my job prospect in the next few years?"
instructions_2 = "Then, think about the question that you just chose very carefully. Shuffle the tarot deck and then fan it out in a fan shape, similar to playing poker. Choose three cards from the cards that you just fanned out. Let your heart decides the cards to choose. After choosing each card, put them separate from the pile of cards, but DO NOT change the order of the cards that you just picked. This is very important for an accurate tarot reading."
instructions_3 = "Developer note: We have only implemented readings for the major arcana currently. Please only choose from the major arcana of your tarot deck."
major_arcana_to_symbols = """
    The Major Arcana:
    
    The Fool = 0
    The Magician = I
    The High Priestess = II
    The Empress = III
    The Emperor = IV
    The Hierophant = V
    The Lovers = VI
    The Chariot = VII
    Strength = VIII
    The Hermit = IX
    Wheel of Fortune = X
    Justice = XI
    The Hanged Man = XII
    Death = XIII
    Temperance = XIV
    The Devil = XV
    The Tower = XVI
    The Star = XVII
    The Moon = XVIII
    The Sun - XIX
    Judgement = XX
    The World = XXI
"""

wands_to_symbols = """
    The Wands:
    
    Ace of Wands = 1_wands
    Two of Wands = 2_wands
    Three of Wands = 3_wands
    Four of Wands = 4_wands
    Five of Wands = 5_wands
    Six of Wands = 6_wands
    Seven of Wands = 7_wands
    Eight of Wands = 8_wands
    Nine of Wands = 9_wands
    Ten of Wands = 10_wands
    Page of Wands = page_wands
    Knight of Wands = knight_wands
    Queen of Wands = queen_wands
    King of Wands = king_wands
"""

cups_to_symbols = """
    The Cups:
    
    Ace of Cups = 1_cups
    Two of Cups = 2_cups
    Three of Cups = 3_cups
    Four of Cups = 4_cups
    Five of Cups = 5_cups
    Six of Cups = 6_cups
    Seven of Cups = 7_cups
    Eight of Cups = 8_cups
    Nine of Cups = 9_cups
    Ten of Cups = 10_cups
    Page of Cups = page_cups
    Knight of Cups = knight_cups
    Queen of Cups = queen_cups
    King of Cups = king_cups
"""

swords_to_symbols = """
    The Swords:
    
    Ace of Swords = 1_swords
    Two of Swords = 2_swords
    Three of Swords = 3_swords
    Four of Swords = 4_swords
    Five of Swords = 5_swords
    Six of Swords = 6_swords
    Seven of Swords = 7_swords
    Eight of Swords = 8_swords
    Nine of Swords = 9_swords
    Ten of Swords = 10_swords
    Page of Swords = page_swords
    Knight of Swords = knight_swords
    Queen of Swords = queen_swords
    King of Swords = king_swords
"""

pentacles_to_symbols = """
    The Pentacles:
    
    Ace of Pentacles = 1_pentacles
    Two of Pentacles = 2_pentacles
    Three of Pentacles = 3_pentacles
    Four of Pentacles = 4_pentacles
    Five of Pentacles = 5_pentacles
    Six of Pentacles = 6_pentacles
    Seven of Pentacles = 7_pentacles
    Eight of Pentacles = 8_pentacles
    Nine of Pentacles = 9_pentacles
    Ten of Pentacles = 10_pentacles
    Page of Pentacles = page_pentacles
    Knight of Pentacles = knight_pentacles
    Queen of Pentacles = queen_pentacles
    King of Pentacles = king_pentacles
"""

cards_positions_to_meaning = {
    "0_0": "You are stepping the first few steps into this relationship, everything is still very new for you. You want to explore more even though many things are still unclear and up in the air. The sensation and chemistry between you too make it even more tempting to explore and develop this relationship.",
    "0_1": "This is only the first stage of your current relationship, there are still more things for you and your partner to enjoy and explore. Both of you need time to figure things out, don\'t walk too fast as the name of love might sound tempting but one small mistake can cause much trouble. The fool also indicates that this relationship is not ready to become a serious one, it needs more time and effort from both of you to maintain and develop.",
    "I_0": "This relationship gives you a lot of opportunities to experience yourself on the road of love. You are energized to focus on developing this relationship and taking the first steps towards that goal. You are enthusiastic, and creative and take the initiative to develop the relationship as if nothing can stand in your way.",
    "I_1": "This relationship allows you to experience the aftertaste of love, you are all on the same page, unleash your creativity without being constrained in the relationship itself. The two of you are like two burning flames, intense in the moments spent together, freely expressing love without fear of external agents. However, up to now, this relationship is still only at the experience level, not a strong and long-term relationship.",
    "II_0": "It seems that you in this relationship still have a lot of worries and thoughts, you have not really opened your heart to share all the secrets with the other person. You are careful, and wary of taking things passively, developing an intense, emotional love relationship is not an option for you right now. Maybe it's because this is the first time you've tasted love, or maybe you've had some stumbles in the past, but now you're more careful, more alert when opening your heart.",
    "II_1": "The relationship between the two of you has spiritual connections, beyond the present tangible world. You spend time with each other, use intuition to understand each other better and feel deep and sincere love from the heart. Gradually, secrets about each other will be revealed and you will have the opportunity to understand more about each other, both advantages and disadvantages of separate personalities.",
    "III_0": "You feel nurtured and pampered in this relationship or you play the role of protecting, nurturing, and sending love to the relationship between the two of you. Either way, this relationship is still giving you abundantly, intense emotions. You feel cherished and appreciated and have great faith in the future of the relationship.",
    "III_1": "This relationship is in the stage of blooming the first flowers of love, you spend more time together and with every minute you spend together, the chemical reactions between you two become more intense. , the more romantic. The two of you enjoy traveling together, dating, caring, and chatting together. Hugs, kisses, and holding hands are like a rich spice for the relationship between two people.",
    "IV_0": "You are a very disciplined person in communication and behavior, whether for work or love relationships. You play a leading and guiding role in this relationship, a solid pillar for the other person to rely on. Emotions, romance, or unexpected surprises in a relationship are probably not something you love or care about. You value reason more than emotion, and you are a clear public-private person, so sometimes you are quite rigid in expressing your love for the other person.",
    "IV_1": "This relationship seems to be pretty much one-sided and lacks the romance and unexpected chemistry between the two. One or both of them are still quite preoccupied with work, so the development of this relationship is somewhat stagnant and slower. Although the nature of the relationship is not a crosswalk, the lack of emotions and time spent together has made the two of you a bit rigid in the development of love. Perhaps patience, persistence, and sincerity, wholeheartedly developing the relationship will be the best solution to help you be sublimated in love.",
    "V_0": "You value tradition in developing love relationships and do not like concepts that are out of the way or too new. In addition to love, the development of an academic and career path is still an important thing in your life. You want to keep the good values ​​of a sincere, romantic, and warm love, you also hope to find the same beliefs from the other side.",
    "V_1": "The two of you met or fell in love in a highly academic environment, be it school, work, or company, or were introduced through friends, colleagues, and people you are close to. Both of them have similar beliefs on many topics in life, be it religious beliefs or any other outlook on life. For some people who have drawn this card, your relationship may be about to move to a new stage of greater commitment. For example, from the stage of getting to know each other to the stage of developing an intimate love relationship, couples who have known each other for a while, you can prepare to get engaged or get married. even hold a wedding, get married.",
    "VI_0": "Your love language is intimate, intimate gestures, from sweet words to warm hugs, kisses, and holding hands. You become more open, and more attractive when falling in love, and this relationship also helps you to be more confident, and to value your own values ​​more. You want to satisfy your partner's intense desires for love that you may have never experienced before.",
    "VI_1": 'This relationship is in a very rapid promotion, the emotions and feelings between the two people seem to be unleashed, sublimated, and flying. The two friends are closer to each other, the more intense and romantic the feelings are when they are ripe, the more they want to experience more things together. However, you should be very careful with the "forbidden fruits" in love, the temptations that this relationship brings so as not to easily make unnecessary mistakes.',
    "VII_0": "You are brave in the face of love, ready to defy all, and overcome all challenges to develop this relationship. The ego in your love is also very sure, straightforward, and dignified. If you are intending to express your feelings to your partner, this is a great opportunity for you to do so.",
    "VII_1": 'You are becoming the master of your own "game", the results you have achieved in this relationship so far may be challenged by the universe, be brave, and speak frankly. Talk to each other about things you don\'t like. Controlling your ego and keeping a peaceful, cautious attitude in the relationship is also very important to help the two of you go further in love.',
    "VIII_0": "In love, you are solid and reliable, being strong spiritual support for the other person. The patience and compassion in you nurture and develop this relationship, you also always burn a fire of enthusiasm and precious sincerity for the person you love. It seems that whatever mistakes the other person made in the past, you are willing to forgive them, accept to learn how to understand and tolerate them.",
    "VIII_1": "The bond between the two of you is getting stronger and stronger, you understand, tolerate, and love each other. Although you always want to spend time together, you are still very patient, waiting and giving each other space. Compassion and forgiveness have made the relationship between two people very strong, reducing heated arguments or unreasonable jealousy.",
    "IX_0": "You are looking for quiet, separate spaces for yourself. You alone turn back, dig deep into the roots of this relationship, about what you want and need in the relationship. At this stage, you are a bit lost and tend to develop a more personal inner self, close your heart and share with the other person.",
    "IX_1": "The two of you seem to have separate plans in life, you are standing at different crossroads in life. The time spent together is getting less and less, perhaps because you still have problems and doubts in your heart that you want to dig deep to find out for yourself. This stage is a stage toward personal development from the depths of the soul, so the relationship between the two will slow down a bit.",
    "X_0": """You seem to feel a lot of new changes, joys, and good news coming to you. This was a transformation that was purely fateful, swift, and intense. If you are waiting for an agreement, an answer, or a confession, this is the perfect time to receive it.
Any surprises from meetings with the other party, handshakes, and greetings to the end are all arranged by fate. Open your heart and accept the gifts from the universe!""",
    "X_1": 'This relationship is facing powerful changes of fate, there will be a lot of things happening to you, including joy, sadness, and luck. There is an old saying: "In misfortune, there is luck", all these gifts are the pre-preparedness of the universe for you. It can test the courage and patience of love or it can also be an existential solution to get your relationship out of troubles and difficulties.',
    "XI_0": "This is the right time for you to pursue clear decisions, and cut off the tangles that you have had to go through in love. The Justice card upholds fairness and decisiveness, reclaiming and protecting your rights. It could be the end of a toxic relationship, the decision to dedicate yourself fully to the relationship, or the period when you accept the consequences of your decisions and actions in the past.",
    "XI_1": "This relationship is demanding clarity from both sides. The balance of responsibilities and development roles should be balanced between the two sides, you should openly and honestly express your views to each other, and don't let out-of-the-way gossip affect the development of the relationship. relationship. If you are looking forward to a new stage of development such as marriage, engagement, etc., then you need to make a clear plan right now.",
    "XII_0": "You are quite passive in developing this relationship, you seem to want to let love be nurtured and blossomed most naturally. You want to take a step back to accept, see the relationship between two people from different angles, more slowly, more carefully than before. Maybe you sacrificed your own interests for the other person, accepting the reality and putting the other person first.",
    "XII_1": "This relationship is in a somewhat unbalanced period when one side is slow and passive, the other is active and bustling, the other side makes silent sacrifices, and the other side is self-reliant and independent. Perhaps at this stage, you want the feelings of both of you to be born naturally and honestly, not under the pressure of anyone but let fate arrange it.",
    "XIII_0": "You are probably thinking of an end and release for both of you. You feel a part of your inner self that is crying out for the transformation and rebirth of a new you, perhaps the relationship itself being a hindrance to that stage of incarnation. You want to get out of the stuffy, secretive phase of the relationship and onto a new path, a newer direction.",
    "XIII_1": "This relationship may no longer bring you the same joy, happiness, and benefits as the original. Both people want to find their own paths, and the cessation of change is necessary for both sides. Maybe this is not the right time for you to continue this relationship.",
    "XIV_0": "You appreciate the balance between all problems in life, conflicts and arguments are things you avoid, control and control during this period as they will upset your order of life. You want to gently heal your soul, connect with your partner with all your heart, and reconcile your differences.",
    "XIV_1": "This relationship is in a very peaceful and harmonious period, you respect each other, and live in harmony and peace. The balance of all factors in life is also what you value first because even though it is developing a love relationship, money, finance, and health are still important foundations for maintaining a relationship.",
    "XV_0": "You are feeling constrained, trapped in this very toxic relationship. The other party may be too controlling and take over every action and decision you make. If you let this situation go on for longer, your mental and physical health will become more and more damaged.",
    "XV_1": "This relationship is developing in a rather toxic and unbalanced direction. The physical and mental constraints will weigh even more on your shoulders. You feel trapped, tired, and feel like you're being taken advantage of in your own relationship."
    # "XVI_0": 
}

instructions_major = 'Type "help_major" to know the Major Arcana syntax'
instructions_wands = 'Type "help_wands" to know the Wands syntax'
instructions_cups = 'Type "help_cups" to know the Cups syntax'
instructions_swords = 'Type "help_swords" to know the Swords syntax'
instructions_pentacles = 'Type "help_pentacles" to know the Pentacles syntax'

possible_answers = ["0", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI"]
# print(cards_positions_to_meaning["X_0"])