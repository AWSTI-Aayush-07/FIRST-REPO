import random
from lifeline import *

r=random.randrange(0,20)

def qno3():
    easy_kbc_questions_nepal = [
    
    ["Which rare astronomical phenomenon occurs when a planet appears to reverse its direction in the sky?", "A) Retrograde Motion", "B) Solar Flare", "C) Parallax Effect", "D) Perihelion", "a"],
    ["Which ancient library, considered one of the largest and most significant, was destroyed in antiquity?", "A) Library of Alexandria", "B) Pergamon Library", "C) Library of Nineveh", "D) Vatican Library", "a"],
    ["What is the name of the protein responsible for oxygen transport in the blood?", "A) Collagen", "B) Hemoglobin", "C) Myoglobin", "D) Keratin", "b"],
    ["Which chemical element was named after the Latin name for Paris?", "A) Lutetium", "B) Francium", "C) Gallium", "D) Polonium", "a"],
    ["Who is the author of the book 'A Brief History of Time'?", "A) Carl Sagan", "B) Stephen Hawking", "C) Richard Feynman", "D) Neil deGrasse Tyson", "b"],
    ["What is the oldest known piece of literature in the world?", "A) The Iliad", "B) Epic of Gilgamesh", "C) The Mahabharata", "D) The Torah", "b"],
    ["Which is the only planet in the solar system that rotates on its side?", "A) Neptune", "B) Venus", "C) Uranus", "D) Mars", "c"],
    ["What is the name of the ancient trade route that connected the East and the West?", "A) Silk Road", "B) Spice Route", "C) Amber Road", "D) Royal Road", "a"],
    ["What is the rarest blood type in the world?", "A) AB Negative", "B) O Negative", "C) HH Blood Type", "D) A Positive", "c"],
    ["Which famous equation is represented as E=mc²?", "A) Newton's Law of Gravity", "B) Einstein's Theory of Relativity", "C) Schrodinger's Wave Equation", "D) Heisenberg's Uncertainty Principle", "b"],
    ["Which part of the brain is primarily responsible for memory?", "A) Hippocampus", "B) Cerebellum", "C) Amygdala", "D) Thalamus", "a"],
    ["What is the name of the largest moon of Saturn?", "A) Europa", "B) Titan", "C) Ganymede", "D) Triton", "b"],
    ["What is the term for the study of ancient writing systems and scripts?", "A) Archaeology", "B) Epigraphy", "C) Paleography", "D) Semantics", "c"],
    ["Which branch of physics deals with the behavior of light?", "A) Optics", "B) Thermodynamics", "C) Acoustics", "D) Quantum Mechanics", "a"],
    ["Which is the oldest continuously inhabited city in the world?", "A) Jerusalem", "B) Damascus", "C) Athens", "D) Varanasi", "b"],
    ["What is the name of the treaty that ended World War I?", "A) Treaty of Trianon", "B) Treaty of Versailles", "C) Treaty of Brest-Litovsk", "D) Treaty of Saint-Germain", "b"],
    ["What is the unit used to measure the intensity of sound?", "A) Decibel", "B) Hertz", "C) Pascal", "D) Joule", "a"],
    ["Which layer of the Earth's atmosphere contains the ozone layer?", "A) Troposphere", "B) Stratosphere", "C) Mesosphere", "D) Thermosphere", "b"],
    ["What is the heaviest naturally occurring element?", "A) Uranium", "B) Plutonium", "C) Thorium", "D) Osmium", "a"],
    ["Which mathematician's work formed the basis for modern computer science?", "A) Blaise Pascal", "B) John von Neumann", "C) Alan Turing", "D) George Boole", "c"]
]



    j=easy_kbc_questions_nepal[r]
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

                {z}                              {j[2:3]}

                {q}                              {j[4:5]}

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



r=random.randrange(0,20)

def qno4():
    moderate_easy_questions = [
    
    ["What is the approximate age of the universe as determined by current scientific estimates?", "A) 10.5 billion years", "B) 13.8 billion years", "C) 15.3 billion years", "D) 12.1 billion years", "b"],
    ["Who developed the theory of General Relativity?", "A) Isaac Newton", "B) Nikola Tesla", "C) Albert Einstein", "D) Galileo Galilei", "c"],
    ["Which ancient script remains undeciphered to this day?", "A) Linear B", "B) Rongorongo", "C) Cuneiform", "D) Hieroglyphics", "b"],
    ["Which is the least densely populated sovereign country in the world?", "A) Mongolia", "B) Greenland", "C) Iceland", "D) Namibia", "a"],
    ["What is the only confirmed artificial object to have left the Solar System?", "A) Hubble Space Telescope", "B) Voyager 1", "C) Voyager 2", "D) New Horizons", "b"],
    ["Which subatomic particle was theorized by Peter Higgs and confirmed in 2012?", "A) Neutrino", "B) Quark", "C) Higgs boson", "D) Gluon", "c"],
    ["What is the rarest blood type in the world?", "A) AB positive", "B) O negative", "C) AB negative", "D) Rh-null", "d"],
    ["Who was the author of the ancient Indian text *Arthashastra*?", "A) Valmiki", "B) Vatsyayana", "C) Chanakya", "D) Kalidasa", "c"],
    ["What is the name of the largest volcano in the Solar System?", "A) Olympus Mons", "B) Mauna Loa", "C) Tamu Massif", "D) Mount Everest", "a"],
    ["Which philosopher is credited with the famous statement 'I think, therefore I am'?", "A) Immanuel Kant", "B) René Descartes", "C) Aristotle", "D) Friedrich Nietzsche", "b"],
    ["What is the term for the study of mushrooms?", "A) Botany", "B) Mycology", "C) Zoology", "D) Ecology", "b"],
    ["What is the largest organ in the human body?", "A) Liver", "B) Skin", "C) Lungs", "D) Brain", "b"],
    ["What is the chemical element with the atomic number 118?", "A) Livermorium", "B) Oganesson", "C) Flerovium", "D) Tennessine", "b"],
    ["Which country was formerly known as Abyssinia?", "A) Sudan", "B) Ethiopia", "C) Eritrea", "D) Somalia", "b"],
    ["What does the term 'Quasar' refer to?", "A) A type of star", "B) A supermassive black hole emitting energy", "C) A galaxy cluster", "D) A planetary nebula", "b"],
    ["Which famous artist is associated with the painting *The Persistence of Memory*?", "A) Salvador Dalí", "B) Pablo Picasso", "C) Vincent van Gogh", "D) Claude Monet", "a"],
    ["Who discovered penicillin?", "A) Alexander Fleming", "B) Louis Pasteur", "C) Marie Curie", "D) Joseph Lister", "a"],
    ["What is the smallest unit of matter that retains the properties of an element?", "A) Molecule", "B) Atom", "C) Proton", "D) Neutron", "b"],
    ["Which desert is the largest in the world?", "A) Sahara", "B) Gobi", "C) Antarctic Desert", "D) Arabian Desert", "c"],
    ["What is the SI unit of electric current?", "A) Volt", "B) Ohm", "C) Ampere", "D) Watt", "c"]


]

    j=moderate_easy_questions[r]
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

                {z}                              {j[2:3]}

                {q}                              {j[4:5]}

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
