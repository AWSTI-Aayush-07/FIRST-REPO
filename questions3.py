import random
from lifeline import *

r=random.randrange(0,30)

def qno5():
    challenging_questions = [
   
    ["What is the only known natural satellite of Pluto?", "A) Charon", "B) Hydra", "C) Nix", "D) Styx", "a"],
    ["Which ancient Greek mathematician calculated the Earth's circumference?", "A) Eratosthenes", "B) Pythagoras", "C) Euclid", "D) Archimedes", "a"],
    ["Who is credited with discovering the structure of the DNA double helix?", "A) James Watson and Francis Crick", "B) Rosalind Franklin", "C) Maurice Wilkins", "D) All of the above", "d"],
    ["What is the name of the deepest trench in the Earth's oceans?", "A) Mariana Trench", "B) Tonga Trench", "C) Java Trench", "D) Kuril-Kamchatka Trench", "a"],
    ["Which empire was founded by Genghis Khan?", "A) Ottoman Empire", "B) Mongol Empire", "C) Mughal Empire", "D) Byzantine Empire", "b"],
    ["What is the chemical formula for table salt?", "A) NaCl", "B) KCl", "C) CaCO3", "D) MgSO4", "a"],
    ["Which element is the most abundant in the universe?", "A) Hydrogen", "B) Helium", "C) Oxygen", "D) Carbon", "a"],
    ["Who painted the famous artwork 'The Persistence of Memory'?", "A) Pablo Picasso", "B) Salvador Dalí", "C) Vincent van Gogh", "D) Claude Monet", "b"],
    ["Which organelle in a cell is known as the 'powerhouse'?", "A) Mitochondria", "B) Ribosome", "C) Nucleus", "D) Golgi apparatus", "a"],
    ["What is the oldest written language in the world?", "A) Sumerian", "B) Sanskrit", "C) Egyptian Hieroglyphics", "D) Akkadian", "a"],
    ["Which planet has the shortest day in the solar system?", "A) Jupiter", "B) Venus", "C) Mercury", "D) Saturn", "a"],
    ["What is the term for animals that only eat plants?", "A) Carnivores", "B) Herbivores", "C) Omnivores", "D) Detritivores", "b"],
    ["Which material is commonly used in nuclear reactors as a moderator?", "A) Graphite", "B) Lead", "C) Mercury", "D) Tungsten", "a"],
    ["What is the name of the philosopher who developed the idea of the 'Allegory of the Cave'?", "A) Socrates", "B) Plato", "C) Aristotle", "D) Epicurus", "b"],
    ["What is the highest waterfall in the world?", "A) Angel Falls", "B) Victoria Falls", "C) Niagara Falls", "D) Tugela Falls", "a"],
    ["Which organ in the human body has the ability to regenerate?", "A) Liver", "B) Heart", "C) Lung", "D) Kidney", "a"],
    ["What is the largest living structure on Earth?", "A) Great Barrier Reef", "B) Amazon Rainforest", "C) Redwood Forest", "D) Yellowstone Caldera", "a"],
    ["Which physicist is known as the father of quantum mechanics?", "A) Max Planck", "B) Albert Einstein", "C) Werner Heisenberg", "D) Niels Bohr", "a"],
    ["What is the most distant human-made object from Earth?", "A) Voyager 1", "B) Hubble Space Telescope", "C) Pioneer 10", "D) New Horizons", "a"],
    ["Which gas is commonly known as laughing gas?", "A) Nitrous Oxide", "B) Carbon Dioxide", "C) Ammonia", "D) Sulfur Hexafluoride", "a"],
    ["What is the speed of light in a vacuum?", "A) 3 x 10^8 m/s", "B) 3 x 10^6 m/s", "C) 3 x 10^5 m/s", "D) 3 x 10^4 m/s", "a"],
    ["Who discovered the law of gravitation?", "A) Isaac Newton", "B) Galileo Galilei", "C) Johannes Kepler", "D) Albert Einstein", "a"],
    ["What is the rarest naturally occurring element on Earth?", "A) Francium", "B) Astatine", "C) Californium", "D) Osmium", "b"],
    ["What is the largest volcano in the solar system?", "A) Olympus Mons", "B) Mauna Loa", "C) Mount Etna", "D) Mount Vesuvius", "a"],
    ["What is the term for the male reproductive part of a flower?", "A) Stamen", "B) Pistil", "C) Sepal", "D) Ovary", "a"],
    ["Which molecule is responsible for carrying genetic information?", "A) DNA", "B) RNA", "C) Protein", "D) Lipid", "a"],
    ["What is the name of the galaxy closest to the Milky Way?", "A) Andromeda", "B) Triangulum", "C) Large Magellanic Cloud", "D) Small Magellanic Cloud", "a"],
    ["Which Nobel Prize category was established last?", "A) Economics", "B) Literature", "C) Peace", "D) Chemistry", "a"],
    ["Who developed the periodic table?", "A) Dmitri Mendeleev", "B) John Dalton", "C) Antoine Lavoisier", "D) Henry Moseley", "a"],
    ["What is the hardest natural substance on Earth?", "A) Diamond", "B) Graphene", "C) Quartz", "D) Corundum", "a"]


]

    j=challenging_questions[r]
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
    user=input("LOCK YOU ANSWER :  ")


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



r=random.randrange(0,30)

def qno6():
    level_3_questions = [
    ["What is the smallest country in the world by area?", "A) Monaco", "B) Vatican City", "C) San Marino", "D) Liechtenstein", "b"],
    ["Which mathematician is known as the 'Prince of Mathematicians'?", "A) Isaac Newton", "B) Carl Friedrich Gauss", "C) Euclid", "D) Pythagoras", "b"],
    ["What is the only metal that is liquid at room temperature?", "A) Mercury", "B) Gallium", "C) Cesium", "D) Bromine", "a"],
    ["Who was the first person to reach the South Pole?", "A) Robert Scott", "B) Roald Amundsen", "C) Ernest Shackleton", "D) Edmund Hillary", "b"],
    ["Which treaty ended World War I?", "A) Treaty of Versailles", "B) Treaty of Tordesillas", "C) Treaty of Paris", "D) Treaty of Ghent", "a"],
    ["Which planet has a day longer than its year?", "A) Mercury", "B) Venus", "C) Neptune", "D) Uranus", "b"],
    ["What is the oldest known written story in the world?", "A) The Iliad", "B) The Epic of Gilgamesh", "C) Beowulf", "D) Mahabharata", "b"],
    ["Which element is named after a planet?", "A) Uranium", "B) Plutonium", "C) Neptunium", "D) All of the above", "d"],
    ["What is the hardest natural substance on Earth?", "A) Diamond", "B) Quartz", "C) Graphite", "D) Corundum", "a"],
    ["Which city is known as the 'Eternal City'?", "A) Athens", "B) Rome", "C) Jerusalem", "D) Cairo", "b"],
    ["What is the most abundant gas in Earth's atmosphere?", "A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Argon", "b"],
    ["Which Nobel Prize category did Marie Curie win twice?", "A) Physics and Peace", "B) Chemistry and Physics", "C) Medicine and Physics", "D) Chemistry and Medicine", "b"],
    ["Who is the author of *Don Quixote*?", "A) Miguel de Cervantes", "B) Leo Tolstoy", "C) Gabriel Garcia Marquez", "D) Victor Hugo", "a"],
    ["What is the term for molten rock beneath the Earth’s surface?", "A) Lava", "B) Magma", "C) Basalt", "D) Granite", "b"],
    ["Which ancient structure is located in Giza, Egypt?", "A) Colossus of Rhodes", "B) Pyramid of Khufu", "C) Hanging Gardens", "D) Temple of Artemis", "b"],
    ["What is the longest river in the world?", "A) Amazon", "B) Nile", "C) Yangtze", "D) Mississippi", "a"],
    ["Which explorer was the first to circumnavigate the globe?", "A) Ferdinand Magellan", "B) Christopher Columbus", "C) Vasco da Gama", "D) Amerigo Vespucci", "a"],
    ["Which branch of mathematics deals with shapes and their properties?", "A) Algebra", "B) Geometry", "C) Calculus", "D) Trigonometry", "b"],
    ["What is the most spoken language in the world?", "A) English", "B) Spanish", "C) Mandarin Chinese", "D) Hindi", "c"],
    ["What is the name of the star closest to Earth?", "A) Proxima Centauri", "B) Sirius", "C) Alpha Centauri", "D) Betelgeuse", "a"],
    ["Which scientist proposed the three laws of motion?", "A) Galileo Galilei", "B) Isaac Newton", "C) Albert Einstein", "D) Johannes Kepler", "b"],
    ["What is the largest desert in the world?", "A) Sahara", "B) Arctic Desert", "C) Gobi Desert", "D) Antarctic Desert", "d"],
    ["What is the name of the largest moon of Saturn?", "A) Europa", "B) Titan", "C) Callisto", "D) Ganymede", "b"],
    ["Which civilization built Machu Picchu?", "A) Aztec", "B) Inca", "C) Maya", "D) Olmec", "b"],
    ["Which branch of science deals with the study of fungi?", "A) Botany", "B) Mycology", "C) Zoology", "D) Microbiology", "b"],
    ["What is the chemical formula of ozone?", "A) O2", "B) O3", "C) O4", "D) O5", "b"],
    ["Which Renaissance artist painted the ceiling of the Sistine Chapel?", "A) Leonardo da Vinci", "B) Michelangelo", "C) Raphael", "D) Donatello", "b"],
    ["What is the capital of Iceland?", "A) Reykjavik", "B) Helsinki", "C) Oslo", "D) Stockholm", "a"],
    ["Which philosopher is known as the 'Father of Western Philosophy'?", "A) Socrates", "B) Plato", "C) Aristotle", "D) Pythagoras", "a"],
    ["What is the main component of the Sun?", "A) Hydrogen", "B) Helium", "C) Carbon", "D) Oxygen", "a"]
]

    j=level_3_questions[r]
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
    elif user.upper()=="LIFELINE":
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
