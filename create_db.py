import sqlite3
import os

# Set up paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'movies.db')

# Delete old database if it exists
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

# Create and connect to new database
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Create the movies table
c.execute('''
CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    poster TEXT,
    description TEXT
)
''')

# List of movies (ensure poster names match image filenames in static/images/)
movies = [
    
    ("Inception", "Sci-fi", "inception.jpg", "A thief who steals corporate secrets through dream-sharing technology."),
    ("Titanic", "Romance", "titanic.jpg", "A love story that blossoms aboard the ill-fated RMS Titanic."),
    ("The Conjuring", "Horror", "conjuring.jpg", "Paranormal investigators help a family terrorized by a dark presence."),
    ("John Wick", "Action", "johnwick.jpg", "An ex-hitman comes out of retirement to track down gangsters."),
    ("Interstellar", "Sci-fi", "interstellar.jpg", "A team travels through a wormhole in search of a new home for humanity."),
    ("Avengers: Endgame", "Action", "Avengers endgame.jpg", "Superheroes unite to reverse the damage caused by Thanos."),
    ("The Notebook", "Romance", "the note book.jpg", "A young couple falls in love in the 1940s."),
    ("Hereditary", "Horror", "hereditary.jpg", "A family's dark secrets unfold after the matriarch dies."),
    ("Blade Runner 2049", "Sci-fi", "blade runner 2049.jpg", "A young blade runner uncovers a long-buried secret."),
    ("Mad Max: Fury Road", "Action", "mad max fury road.jpg", "In a post-apocalyptic wasteland, a woman rebels against a tyrant."),
    ("La La Land", "Romance", "la la land .jpg", "An aspiring actress and a jazz musician pursue their dreams in LA."),
    ("A Quiet Place", "Horror", "a quiet place.jpg", "A family must stay silent to avoid blind monsters with sharp hearing."),
    ("The Matrix", "Sci-fi", "the matrix.jpg", "A computer hacker learns the truth about his reality."),
    ("Gladiator", "Action", "gladiator.jpg", "A betrayed Roman general seeks revenge as a gladiator."),
    ("Pride and Prejudice", "Romance", "pride and prejudice.jpg", "Sparks fly between Elizabeth Bennet and Mr. Darcy."),
    ("The Ring", "Horror", "the ring.jpg", "A cursed videotape leads to a deadly chain of events."),
    ("Dune", "Sci-fi", "dune.jpg", "A noble family becomes embroiled in a war over a desert planet's spice."),
    ("Skyfall", "Action", "sky fall.jpg", "James Bond investigates an attack on MI6."),
    ("Me Before You", "Romance", "me before you.jpg", "A caretaker falls for a paralyzed man in her care."),
    ("It", "Horror", "It.jpg", "A group of children face a shape-shifting clown."),
    ("Ex Machina", "Sci-fi", "Ex Machina.jpg", "A programmer is invited to administer the Turing test to an AI."),
  
    ('All We Imagine as Light', 'Drama', 'all_we_imagine_as_light.jpg', 'Three working-class women navigate life and dreams in Mumbai.'),
    ('Laapataa Ladies', 'Drama', 'laapataa_ladies.jpg', 'Two brides are mistakenly swapped during a train journey.'),
    ('The Buckingham Murders', 'Drama', 'the_buckingham_murders.jpg', 'A detective investigates a child’s murder in England.'),
    ('Gulmohar', 'Drama', 'gulmohar.jpg', 'Family tensions rise as they prepare to leave their ancestral home.'),
    ('Bheed', 'Drama', 'bheed.jpg', 'Migrant workers struggle during India’s 2020 lockdown.'),

   
    ('Dream Girl 2', 'Comedy', 'dream_girl_2.jpg', 'Karam transforms into Pooja, creating hilarious confusion.'),
    ('Murder Mubarak', 'Comedy', 'murder_mubarak.jpg', 'A murder in a high-society club uncovers hidden secrets.'),
    ('Laapataa Ladies', 'Comedy', 'laapataa_ladies.jpg', 'A light-hearted journey about mistaken identities.'),
    ('Zara Hatke Zara Bachke', 'Comedy', 'zara_hatke_zara_bachke.jpg', 'A couple fakes a divorce to get a government flat.'),
    ('Selfiee', 'Comedy', 'selfiee.jpg', 'A fan’s admiration turns into a public spat with his idol.'),

   
    ('Jaane Jaan', 'Thriller', 'jaane_jaan.jpg', 'A woman is drawn into a murder investigation.'),
    ('Khufiya', 'Thriller', 'khufiya.jpg', 'A spy tracks a mole leaking defense secrets.'),
    ('Gumraah', 'Thriller', 'gumraah.jpg', 'A twin mystery confuses the murder investigation.'),
    ('Jigra', 'Thriller', 'jigra.jpg', 'A sister fights to rescue her brother from prison.'),
    ('Kill', 'Thriller', 'kill.jpg', 'A commando battles hijackers on a train.'),   

   
    ('The Buckingham Murders', 'Crime', 'the_buckingham_murders.jpg', 'Detective investigates murder in a British town.'),
    ('Gumraah', 'Crime', 'gumraah.jpg', 'A murder mystery involving identical twins.'),
    ('Khufiya', 'Crime', 'khufiya.jpg', 'Espionage and betrayal within RAW.'),
    ('Murder Mubarak', 'Crime', 'murder_mubarak.jpg', 'A cop investigates a murder in a country club.'),
    ('Jaane Jaan', 'Crime', 'jaane_jaan.jpg', 'A math teacher becomes entangled in a criminal case.'),

  
    ('Hanuman vs Mahiravana', 'Animation', 'hanuman_vs_mahiravana.jpg', 'Hanuman saves Rama and Lakshmana from Mahiravana.'),
    ('Chhota Bheem and the Curse of Damyaan', 'Animation', 'bheem_damyaan.jpg', 'Bheem fights an evil sorcerer to save his land.'),
    ('Motu Patlu: King of Kings', 'Animation', 'motu_patlu_king.jpg', 'Motu and Patlu help a lion reclaim his throne.'),
    ('The Legend of Hanuman Season 3', 'Animation', 'legend_of_hanuman_3.jpg', 'Hanuman’s mythological journey continues.'),
    ('Krishna: The Birth', 'Animation', 'krishna_birth.jpg', 'An animated tale of Lord Krishna’s birth.'),


    ('Neeyat', 'Mystery', 'neeyat.jpg', 'A birthday celebration turns into a murder scene.'),
    ('Jaane Jaan', 'Mystery', 'jaane_jaan.jpg', 'A woman’s hidden past unravels in a murder case.'),
    ('Khufiya', 'Mystery', 'khufiya.jpg', 'Spy thriller with layers of secrets and betrayal.'),
    ('Murder Mubarak', 'Mystery', 'murder_mubarak.jpg', 'Everyone has a motive in this elite murder mystery.'),
    ('The Buckingham Murders', 'Mystery', 'the_buckingham_murders.jpg', 'A grieving detective unravels a complex murder case.'),

    
    ('Kill', 'Adventure', 'kill.jpg', 'A train turns into a battlefield for a commando.'),
    ('Jigra', 'Adventure', 'jigra.jpg', 'Sister embarks on a daring rescue mission.'),
    ('Laapataa Ladies', 'Adventure', 'laapataa_ladies.jpg', 'Two brides journey through rural India after a mix-up.'),
    ('Chhota Bheem and the Curse of Damyaan', 'Adventure', 'bheem_damyaan.jpg', 'Bheem saves Dholakpur from a dark curse.'),
    ('Motu Patlu: King of Kings', 'Adventure', 'motu_patlu_king.jpg', 'Adventures unfold as Motlu and Patlu fight poachers.'),

   
    ('Brahmastra: Part One – Shiva', 'Fantasy', 'brahmastra.jpg', 'A young man learns about his mystical powers.'),
    ('Tumbbad', 'Fantasy', 'tumbbad.jpg', 'A dark tale of greed and a hidden deity.'),
    ('Shamshera', 'Fantasy', 'shamshera.jpg', 'A warrior leads a rebellion against British rule.'),
    ('Ra one', 'Fantasy', 'raone.jpg', 'A video game villain enters the real world.'),
    ('Krrish 3', 'Fantasy', 'krrish 3.jpg', 'A superhero fights evil mutants to save the world.')
]

# Insert movie records
c.executemany("INSERT INTO movies (title, genre, poster, description) VALUES (?, ?, ?, ?)", movies)

# Finalize and close
conn.commit()
conn.close()
print("Database initialized successfully.")