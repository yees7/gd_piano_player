from music21 import pitch

# NOTE TABLE:

# OCTAVE 4 abcdefg
# A = A4
# b = Bb4 (A#4)
# B = B4
# C = C4
# d = Db4 (C#4)
# D = D4
# e = Eb4 (D#4)
# E = E4
# F = F4
# g = Gb4 (F#4)
# G = G4
# a = Ab4 (G#4)

# OCTAVE 3 hijklmn
# H = A3
# i = Bb3 (A#3)
# I = B3
# J = C3
# k = Db3 (C#3)
# K = D3
# l = Eb3 (D#3)
# L = E3
# M = F3
# n = Gb3 (F#3)
# N = G3
# h = Ab3 (G#3)

# OCTAVE 5 opqrstu
# O = A5
# p = Bb5 (A#5)          
# P = B5
# Q = C5
# r = Db5 (C#5)
# R = D5
# s = Eb5 (D#5)
# S = E5
# T = F5
# u = Gb5 (F#5)
# U = G5
# o = Ab5 (G#5)

# OCTAVE 2 vwxyz012
# V = A2
# w = Bb2 (A#2)
# W = B2
# X = C2
# y = Db2 (C#2)
# Y = D2
# z = Eb2 (D#2)
# Z = E2
# 0 = F2
# 1 = Gb2 (F#2)
# 2 = G2
# v = Ab2 (G#2)

# OCTAVE 6 3456789-_=+!
# 3 = A6
# 4 = Bb6 (A#2)
# 5 = B6
# 6 = C6
# 7 = Db6 (C#2)
# 8 = D6
# 9 = Eb6 (D#2)
# - = E6
# _ = F6
# = = Gb6 (F#6)
# + = G6
# ! = Ab6 (G#6)

# OCTAVE 7 @#$%^&*()[{}
# @ = A7
# # = Bb7 (A#6)
# $ = B7
# % = C7
# ^ = Db7 (C#6)
# & = D7
# (unsupported)
# * = Eb7 (D#6)
# ( = E7
# ) = F7
# [ = Gb7 (F#6)
# { = G7
# } = Ab7 (G#6)

# OCTAVE 1 ]\|;:'",<.>/
# (unsupported)
# ] = A7
# \ = Bb7 (A#6)
# | = B7
# ; = C7
# : = Db7 (C#6)
# ' = D7
# " = Eb7 (D#6)
# , = E7
# < = F7
# . = Gb7 (F#6)
# > = G7
# / = Ab7 (G#6)

def note_to_char(note: pitch) -> str:
    match note.nameWithOctave:
        # OCTAVE 4 abcdefg
        # A = A4
        # b = Bb4 (A#4)
        # B = B4
        # C = C4
        # d = Db4 (C#4)
        # D = D4
        # e = Eb4 (D#4)
        # E = E4
        # F = F4
        # g = Gb4 (F#4)
        # G = G4
        # a = Ab4 (G#4)
        case 'A4':
            return 'A'
        case 'A#4' | 'B-4':
            return 'b'
        case 'B4':
            return 'B'
        case 'C4':
            return 'C'
        case 'C#4' | 'D-4':
            return 'd'
        case 'D4':
            return 'D'
        case 'D#4' | 'E-4':
            return 'e'
        case 'E4':
            return 'E'
        case 'F4':
            return 'F'
        case 'F#4' | 'G-4':
            return 'g'
        case 'G4':
            return 'G'
        case 'G#4' | 'A-4':
            return 'a'
        
        # OCTAVE 3 hijklmn
        # H = A3
        # i = Bb3 (A#3)
        # I = B3
        # J = C3
        # k = Db3 (C#3)
        # K = D3
        # l = Eb3 (D#3)
        # L = E3
        # M = F3
        # n = Gb3 (F#3)
        # N = G3
        # h = Ab3 (G#3)
        
        case 'A3':
            return 'H'
        case 'A#3' | 'B-3':
            return 'i'
        case 'B3':
            return 'I'
        case 'C3':
            return 'J'
        case 'C#3' | 'D-3':
            return 'k'
        case 'D3':
            return 'K'
        case 'D#3' | 'E-3':
            return 'l'
        case 'E3':
            return 'L'
        case 'F3':
            return 'M'
        case 'F#3' | 'G-3':
            return 'n'
        case 'G3':
            return 'N'
        case 'G#3' | 'A-3':
            return 'h'
        
        # OCTAVE 5 opqrstu
        # O = A5
        # p = Bb5 (A#5)          
        # P = B5
        # Q = C5
        # r = Db5 (C#5)
        # R = D5
        # s = Eb5 (D#5)
        # S = E5
        # T = F5
        # u = Gb5 (F#5)
        # U = G5
        # o = Ab5 (G#5)
        
        case 'A5':
            return 'O'
        case 'A#5' | 'B-5':
            return 'p'
        case 'B5':
            return 'P'
        case 'C5':
            return 'Q'
        case 'C#5' | 'D-5':
            return 'r'
        case 'D5':
            return 'R'
        case 'D#5' | 'E-5':
            return 's'
        case 'E5':
            return 'S'
        case 'F5':
            return 'T'
        case 'F#5' | 'G-5':
            return 'u'
        case 'G5':
            return 'U'
        case 'G#5' | 'A-5':
            return 'o'
        
        # OCTAVE 2 vwxyz012
        # V = A2
        # w = Bb2 (A#2)
        # W = B2
        # X = C2
        # y = Db2 (C#2)
        # Y = D2
        # z = Eb2 (D#2)
        # Z = E2
        # 0 = F2
        # 1 = Gb2 (F#2)
        # 2 = G2
        # v = Ab2 (G#2)
        
        # (octave 1 currently unsupported, notes in octave 1 are moved to octave 2)

        case 'A2' | 'A1':
            return 'V'
        case 'A#2' | 'B-2' | 'B-1' | 'A#1':
            return 'w'
        case 'B2' | 'B1':
            return 'W'
        case 'C2' | 'C1':
            return 'X'
        case 'C#2' | 'D-2' | 'C#1' | 'D-1':
            return 'y'
        case 'D2' | 'D1':
            return 'Y'
        case 'D#2' | 'E-2' | 'D#1' | 'E-1':
            return 'z'
        case 'E2' | 'E1':
            return 'Z'
        case 'F2' | 'F1':
            return '0'
        case 'F#2' | 'G-2' | 'G-1' | 'F#1':
            return '1'
        case 'G2' | 'G1':
            return '2'
        case 'G#2' | 'A-2' | 'A-1' | 'G#1':
            return 'v'
        
        # OCTAVE 6 3456789-_=+!
        # 3 = A6
        # 4 = Bb6 (A#2)
        # 5 = B6
        # 6 = C6
        # 7 = Db6 (C#2)
        # 8 = D6
        # 9 = Eb6 (D#2)
        # - = E6
        # _ = F6
        # = = Gb6 (F#6)
        # + = G6
        # ! = Ab6 (G#6)
        
        case 'A6':
            return '3'
        case 'A#6' | 'B-6':
            return '4'
        case 'B6':
            return '5'
        case 'C6':
            return '6'
        case 'C#6' | 'D-6':
            return '7'
        case 'D6':
            return '8'
        case 'D#6' | 'E-6':
            return '9'
        case 'E6':
            return '-'
        case 'F6':
            return '_'
        case 'F#6' | 'G-6':
            return '='
        case 'G6':
            return '+'
        case 'G#6' | 'A-6':
            return '!'
        
        # OCTAVE 7 @#$%^&*()[{}
        # @ = A7
        # # = Bb7 (A#6)
        # $ = B7
        # % = C7
        # ^ = Db7 (C#6)
        # & = D7
        # (unsupported)
        # * = Eb7 (D#6)
        # ( = E7
        # ) = F7
        # [ = Gb7 (F#6)
        # { = G7
        # } = Ab7 (G#6)
        
        case 'A7':
            return '@'
        case 'A#7' | 'B-7':
            return '#'
        case 'B7':
            return '$'
        case 'C7':
            return '%'
        case 'C#7' | 'D-7':
            return '^'
        case 'D7':
            return '&'
        
        # OCTAVE 1 ]\|;:'",<.>/
        # (unsupported)
        # ] = A7
        # \ = Bb7 (A#6)
        # | = B7
        # ; = C7
        # : = Db7 (C#6)
        # ' = D7
        # " = Eb7 (D#6)
        # , = E7
        # < = F7
        # . = Gb7 (F#6)
        # > = G7
        # / = Ab7 (G#6)
        # (octave 1 currently unsupported, notes in octave 1 are moved to octave 2)
        
        case _:
            return '??'