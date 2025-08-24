from midiutil import MIDIFile

# Paramètres généraux
tempo = 98
track = 0
channel = 0
volume = 100

# Création du fichier MIDI
mf = MIDIFile(1)  # 1 piste
mf.addTempo(track, 0, tempo)

# Progression d'accords pop urbaine (Am - F - C - G)
chords = [
    [57, 60, 64],   # Am
    [53, 57, 60],   # F
    [55, 59, 62],   # C
    [55, 59, 62, 67]  # G
]

# Fonctions utilitaires
def add_chord(mf, time, chord, duration, channel=0, velocity=80):
    for note in chord:
        mf.addNote(track, channel, note, time, duration, velocity)

def add_melody(mf, time, melody, duration=0.5, channel=1, velocity=100):
    for note in melody:
        mf.addNote(track, channel, note, time, duration, velocity)
        time += duration

# 1. Couplet 1 (Tiakola)
time = 0
for i in range(4):
    add_chord(mf, time, chords[i % 4], 2)
    # Mélodie chantée/rapée
    melody = [69, 71, 72, 71, 69, 67] if i % 2 == 0 else [67, 69, 71, 72, 74]
    add_melody(mf, time + 0.5, melody)
    time += 2

# 2. Refrain 1 (Gims + backs)
for i in range(4):
    add_chord(mf, time, chords[i % 4], 2, channel=0, velocity=100)
    # Mélodie refrain (lead + back)
    lead = [72, 74, 76, 74, 72, 71]  # Gims
    backs = [79, 76, 74, 76, 79, 81]  # Aya/Tiakola back
    add_melody(mf, time + 0.5, lead, channel=1)
    add_melody(mf, time + 1, backs, channel=2, velocity=70)
    time += 2

# 3. Couplet 2
# 3a. Rap Central Cee
for i in range(2):
    add_chord(mf, time, chords[i % 4], 2, channel=0, velocity=90)
    rap_flow = [67, 67, 69, 71, 69, 67, 65, 64]  # Flow staccato
    add_melody(mf, time + 0.5, rap_flow, duration=0.25, channel=3, velocity=110)
    time += 2

# 3b. Chant Aya Nakamura
for i in range(2):
    add_chord(mf, time, chords[(i+2) % 4], 2, channel=0, velocity=90)
    aya_mel = [74, 76, 79, 76, 74, 72]
    add_melody(mf, time + 0.5, aya_mel, channel=4, velocity=100)
    time += 2

# 4. Refrain 2 (Gims + backs)
for i in range(4):
    add_chord(mf, time, chords[i % 4], 2, channel=0, velocity=100)
    lead = [72, 74, 76, 74, 72, 71]
    backs = [79, 76, 74, 76, 79, 81]
    add_melody(mf, time + 0.5, lead, channel=1)
    add_melody(mf, time + 1, backs, channel=2, velocity=70)
    time += 2

# 5. Outro Tiakola
for i in range(2):
    add_chord(mf, time, chords[i % 4], 2, channel=0, velocity=70)
    outro_mel = [67, 69, 71, 69, 67]
    add_melody(mf, time + 0.5, outro_mel, channel=1, velocity=60)
    time += 2

# Écriture du fichier MIDI
with open("pop_urbain_love_luxe.mid", "wb") as f:
    mf.writeFile(f)

print("Fichier MIDI généré : pop_urbain_love_luxe.mid")
