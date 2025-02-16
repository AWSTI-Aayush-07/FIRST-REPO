import random
from lifeline import *
r=random.randrange(0,15)

def qno1():
    questions = [
     ["Who was the first Prime Minister of India?", "A) Lal Bahadur Shastri", "B) Jawaharlal Nehru", "C) Indira Gandhi", "D) Mahatma Gandhi", "b"],
     ["Which is the national bird of India?", "A) Peacock", "B) Sparrow", "C) Pigeon", "D) Parrot", "a"],
     ["Which planet is known as the Red Planet?", "A) Earth", "B) Jupiter", "C) Mars", "D) Venus", "c"],
     ["Which is the largest animal on Earth?", "A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Great White Shark", "b"],
     ["What is the capital of India?", "A) Mumbai", "B) Chennai", "C) New Delhi", "D) Kolkata", "c"],
     ["Which organ pumps blood in the human body?", "A) Brain", "B) Lungs", "C) Heart", "D) Stomach", "c"],
     ["What is the currency of the United States?", "A) Dollar", "B) Euro", "C) Pound", "D) Yen", "a"],
     ["Which is the smallest continent?", "A) Asia", "B) Europe", "C) Australia", "D) Antarctica", "c"],
     ["Which festival is known as the festival of lights in India?", "A) Holi", "B) Diwali", "C) Eid", "D) Christmas", "b"],
     ["Which sport is known as the 'Gentleman’s Game'?", "A) Football", "B) Tennis", "C) Cricket", "D) Chess", "c"],
     ["What do we call the person who flies an airplane?", "A) Driver", "B) Captain", "C) Pilot", "D) Navigator", "c"],
     ["What is the chemical symbol for water?", "A) H2", "B) O2", "C) H2O", "D) CO2", "c"],
     ["Who wrote the national anthem of India?", "A) Rabindranath Tagore", "B) Bankim Chandra Chatterjee", "C) Subhash Chandra Bose", "D) Mahatma Gandhi", "a"],
     ["How many legs does a spider have?", "A) 6", "B) 8", "C) 10", "D) 12", "b"],
     ["What is the primary source of energy for Earth?", "A) Moon", "B) Sun", "C) Wind", "D) Water", "b"]
    ]
    j=questions[r]
    ans="".join(j[-1:])
    
    a=int(0)
    b=int(1)

    z="".join(j[1:2])
    q="".join(j[3:4])
    zlen=len("".join(j[1:2]))
    qlen=len("".join(j[3:4]))
    
   
    if zlen>qlen:
     for i in range(0,100):
       q=q+" "
       if len(q)==len(z):
         break
    else:
      for i in range(0,100):
         if len(q)==len(z):
            break
         z=z+" "
         

    print(f"""
{j[0:1]}

                |{z}|                              |{j[2:3]}|

                |{q}|                              |{j[4:5]}|

     """)
    user=input("LOCK YOU ANSWER (ENTER ""LIFELINE"" IF YOU NEED A LIFELINE):  ")


    print("------------------------------------------------------------------------------------------------\n")
    if user==ans.lower():
       print(f""" YOU LOCKED YOUR ANSWER AS ({user.upper()}) AND IT IS THE :
       """)
       a=input("HIT ENTER TO CONTINUE : ")
       while a!="":
       
          input("HIT ENTER TO CONTINUE : ")==""
       print(f"""\n\n\n\n\n!  
               ********************************************************
               *     KEEP GOING TO WIN THE GRAND PRIZE! 🏆🎯          *
               ******************************************************""")
    elif user.upper()=="LIFELINE":
       lifeline(j)
    else:
        print(f""" YOU LOCKED YOUR ANSWER AS {user} AND IT IS A.>
       """)
        a=input("HIT ENTER TO CONTINUE : ")
        while a!="":
       
          input("HIT ENTER TO CONTINUE : ")==""
         
        exit(f"""\n\n\n\n\n
                          ___________________________________________________________________________       
                          |      WRONG__ANSWER - BETTER - LUCK - NEXT - TIME                         |
                          |--------------------------------------------------------------------------|""")



r=random.randrange(0,15)

def qno2():
    questions_1_5 = [
     ["Which is the smallest ocean in the world?", "A) Arctic", "B) Indian", "C) Atlantic", "D) Southern", "a"],
     ["Which Mughal emperor built the Taj Mahal?", "A) Akbar", "B) Shah Jahan", "C) Humayun", "D) Aurangzeb", "b"],
     ["What is the boiling point of water at sea level in Celsius?", "A) 90°C", "B) 100°C", "C) 110°C", "D) 120°C", "b"],
     ["Which planet has the most moons?", "A) Mars", "B) Jupiter", "C) Saturn", "D) Uranus", "c"],
     ["What is the official language of Brazil?", "A) Spanish", "B) French", "C) Portuguese", "D) English", "c"],
     ["Who discovered penicillin?", "A) Alexander Fleming", "B) Marie Curie", "C) Louis Pasteur", "D) Joseph Lister", "a"],
     ["Which is the highest mountain in Africa?", "A) Mount Kenya", "B) Mount Kilimanjaro", "C) Mount Everest", "D) Mount Elgon", "b"],
     ["What is the hardest natural substance on Earth?", "A) Gold", "B) Iron", "C) Diamond", "D) Quartz", "c"],
     ["Which vitamin is produced by the body when exposed to sunlight?", "A) Vitamin A", "B) Vitamin B12", "C) Vitamin D", "D) Vitamin C", "c"],
     ["Which city is known as the 'City of Love'?", "A) Rome", "B) Venice", "C) Paris", "D) Barcelona", "c"],
     ["What is the national flower of Japan?", "A) Tulip", "B) Lotus", "C) Cherry Blossom", "D) Rose", "c"],
     ["Which gas is commonly known as laughing gas?", "A) Oxygen", "B) Nitrous Oxide", "C) Carbon Monoxide", "D) Hydrogen Sulfide", "b"],
     ["Which instrument is used to measure atmospheric pressure?", "A) Thermometer", "B) Hygrometer", "C) Barometer", "D) Anemometer", "c"],
     ["Who is the author of 'The Adventures of Sherlock Holmes'?", "A) Mark Twain", "B) J.K. Rowling", "C) Arthur Conan Doyle", "D) Agatha Christie", "c"],
     ["Which blood group is known as the universal donor?", "A) AB+", "B) O-", "C) B+", "D) A-", "b"]
     ]
    j=questions_1_5[r]
    ans="".join(j[-1:])
    
    a=int(0)
    b=int(1)

    z="".join(j[1:2])
    q="".join(j[3:4])
    zlen=len("".join(j[1:2]))
    qlen=len("".join(j[3:4]))
    
   
    if zlen>qlen:
     for i in range(0,100):
       q=q+" "
       if len(q)==len(z):
         break
    else:
      for i in range(0,100):
         if len(q)==len(z):
            break
         z=z+" "
      

    print(f"""
{j[0:1]}
               
               |{z}|                              |{j[2:3]}|

               |{q}|                              |{j[4:5]}|

     """)
    
    print("--------------------------------------------------------------------------------------------------------------\n")
    user=input("LOCK YOU ANSWER :  ")
    if user==ans.lower():
       print(f""" YOU LOCKED YOUR ANSWER AS ({user.upper()}) AND IT IS THE :
       """)
       a=input("HIT ENTER TO CONTINUE : ")
       while a!="":
       
          input("HIT ENTER TO CONTINUE : ")==""
       print(f"""\n\n\n\n\n!  
               ********************************************************
               *     KEEP GOING TO WIN THE GRAND PRIZE! 🏆🎯          *
               ******************************************************""")
    elif user.lower()=="lifeline":
       lifeline(j)
    else:
        print(f""" YOU LOCKED YOUR ANSWER AS {user} AND IT IS A.>\n\n
       """)
        a=input("HIT ENTER TO CONTINUE :   ")
        while a!="":
       
          input("HIT ENTER TO CONTINUE : ")==""
         
        exit(f"""\n\n\n\n\n
___________________________________________________________________________       
|      WRONG__ANSWER - BETTER - LUCK - NEXT - TIME                         |
|--------------------------------------------------------------------------|""")
