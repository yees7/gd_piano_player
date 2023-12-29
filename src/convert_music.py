import music21
from src.note_to_char import note_to_char

# converts sheet music to temporary data file that contains note data

# available sheet music file types: 
# https://web.mit.edu/music21/doc/usersGuide/usersGuide_08_installingMusicXML.html#file-types-available-to-music21

def convert_music(filename):

    b = music21.converter.parse(filename)

    txt = ""
    beats = []
    beat = 0
    bar = 0

    treble_staff: music21.stream.PartStaff = None
    bass_staff: music21.stream.PartStaff = None

    for x in b.recurse():
        if type(x) is music21.stream.PartStaff:
            if treble_staff is None:
                treble_staff = x
            else:
                bass_staff = x

    for x in treble_staff.recurse():
        if type(x) is music21.stream.Measure:
            for i in range(16):
                beats.append('')
            for tN in x.recurse():
                notes = ""
                if type(tN) is music21.chord.Chord:
                    es = music21.analysis.enharmonics.EnharmonicSimplifier(tN.pitches)
                    for i in es.bestPitches():
                        c = note_to_char(i)
                        if c == '??':
                            raise KeyError("Note '" + i.nameWithOctave + "' could not be converted: note unsupported")
                        notes += c
                elif type(tN) is music21.note.Note:
                    es = music21.analysis.enharmonics.EnharmonicSimplifier(tN.pitches)
                    c = note_to_char(es.bestPitches()[0])
                    if c == '??':
                        raise KeyError("Note '" + tN.nameWithOctave + "' could not be converted: note unsupported")
                    notes += c
                elif type(tN) is music21.note.Rest:
                    pass
                else:
                    continue
                beats[int(bar*16+(tN.beat-1)*4)] += notes
            bar += 1
    bar = 0                

    for x in bass_staff.recurse():
        if type(x) is music21.stream.Measure:
            for tN in x.recurse():
                notes = ""
                if type(tN) is music21.chord.Chord:
                    es = music21.analysis.enharmonics.EnharmonicSimplifier(tN.pitches)
                    for i in es.bestPitches():
                        c = note_to_char(i)
                        if c == '??':
                            raise KeyError("Note '" + i.nameWithOctave + "' could not be converted: note unsupported")
                        notes += c
                elif type(tN) is music21.note.Note:
                    es = music21.analysis.enharmonics.EnharmonicSimplifier(tN.pitches)
                    c = note_to_char(es.bestPitches()[0])
                    if c == '??':
                        raise KeyError("Note '" + tN.nameWithOctave + "' could not be converted: note unsupported")
                    notes += c
                elif type(tN) is music21.note.Rest:
                    pass
                else:
                    continue
                beats[int(bar*16+(tN.beat-1)*4)] += notes
            bar+=1

    with open("build/tmp.txt", "w") as f:
        f.write(' '.join(beats))