'''
6 kyu
Name: Music theory - MinorMajor chords

https://www.codewars.com/kata/57052ac958b58fbede001616/python
Task: Check if given chord is minor or major.

Rules:

Basic minor/major chord have three elements.

Chord is minor when interval between first and second element equals 3 and between second and third -> 4.

Chord is major when interval between first and second element equals 4 and between second and third -> 3.

In minor/major chord interval between first and third element equals... 7.
'''

def minor_or_major(chord):
    ls=chord.split()
    if len(ls)!=3:
        return 'Not a chord'
    else:
        notes = {'C':1, 'C#':2, 'Db':2, 'D':3, 'D#':4, 'Eb':4, 'E':5, 'F':6, 'F#':7, 'Gb':7,
                 'G':8, 'G#':9, 'Ab':9, 'A':10, 'A#':11, 'Bb':11, 'B':12}
        if ls[0] not in notes or ls[1] not in notes or ls[2] not in notes:
            return 'Not a chord'
        if notes[ls[1]]<notes[ls[0]] and notes[ls[2]]>notes[ls[1]]:
            if notes[ls[1]]+12-notes[ls[0]]==3 and notes[ls[2]]-notes[ls[1]]==4:
                return 'Minor'
            elif notes[ls[1]]+12-notes[ls[0]]==4 and notes[ls[2]]-notes[ls[1]]==3:
                return 'Major'
            else:
                return 'Not a chord'
        elif notes[ls[1]]>notes[ls[0]] and notes[ls[2]]<notes[ls[1]]:
            if notes[ls[1]]-notes[ls[0]]==3 and notes[ls[2]]+12-notes[ls[1]]==4:
                return 'Minor'
            elif notes[ls[1]]-notes[ls[0]]==4 and notes[ls[2]]+12-notes[ls[1]]==3:
                return 'Major'
            else:
                return 'Not a chord'
        else:
            if notes[ls[1]]-notes[ls[0]]==3 and notes[ls[2]]-notes[ls[1]]==4:
                return 'Minor'
            elif notes[ls[1]]-notes[ls[0]]==4 and notes[ls[2]]-notes[ls[1]]==3:
                return 'Major'
            else:
                return 'Not a chord'