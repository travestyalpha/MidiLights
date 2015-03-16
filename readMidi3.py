import binascii
import time

from pyfirmata import Arduino, util
board = Arduino('/dev/ttyACM0')

track = list()
timeDivision = 0

def Main():
    print "Main"
    Initialize()
    loadMidi = "JoyToTheWorld-alt.midi"
    trackLength = getTrackLength(loadMidi)
    loadTrackToList(loadMidi, trackLength)
    while True:
        midiTrackLoop(trackLength)
        time.sleep(2)

def Initialize():
    print "Initialize"
    for x in range (4,12):
        board.digital[x].write(1)
    time.sleep(2)

def getDelta_time(j): # calculate the delta time
    # this comes from http://csi-info.baylor.edu/data/Midi%20Lab/midiparse.py
    # I've slightly modified it to fit my needs, but it was extremely helpful
    
    print "getDeltaTime"
    sum = 0
    byteCount = 0
    while 1:
        x = ord(track[j]) # converts bytestring to integer
        j = j + 1
        sum = (sum << 7) + (x & 0x7F) # handwavy bitwise magic (shift and combine)
        byteCount += 1
        if not (x & 0x80): # checks MSB of byte
            print "delta time:", sum,
            delta_time(sum)
            return sum, byteCount

def delta_time(delay): # pauses for delta time
    global timeDivision
    tempo = 120.00 # tempo is set to 120 BPM
    ticksPerSecond = int(timeDivision,16)
    dt = (60.0*float(delay))/(tempo*ticksPerSecond) # calculate delta time as fraction of a second
    time.sleep(dt) #delay for delta time seconds
    print "delay for:", round(dt,3), "seconds"
    

def checkMidi_event(j): #determines the midi event type
    print "midi event:",
    event_type = ord(track[j])

    if event_type == 0xFF: # check for meta event message
        return(meta_event(j))

    # check for note on message
    elif event_type & 0b11110000 == 0x90: # use 0b10010000 as bitmask
        return(note_on(j))
 
    # check for note off message
    elif event_type & 0b11110000 == 0x80: # use 0b10000000 as bitmask
        return(note_off(j))

    # if there is an unknown message display this and carry on.
    else:
        print "Warning - Unutilized Midi Event"       

def note_on(j): #note on event
    byteCount = 3
    value = binascii.b2a_hex(track[j+1])
    velocity = binascii.b2a_hex(track[j+2])
    print "Note On: 0x" + binascii.b2a_hex(track[j]), "value: 0x" + value, "velocity: 0x" + velocity
    play_note(ord(track[j+1]), velocity)
    #time.sleep(0.1)
    return(byteCount)

def note_off(j): #note off event
    byteCount = 3
    value = binascii.b2a_hex(track[j+1])
    velocity = binascii.b2a_hex(track[j+2])
    print "Note Off: 0x" + binascii.b2a_hex(track[j]), "value: 0x" + value, "velocity: 0x" + velocity
    stop_note(ord(track[j+1]))
    time.sleep(0.1)
    return(byteCount)
 

def meta_event(j): #meta event
    byteCount = 3
    print "meta event: ",
    value = binascii.b2a_hex(track[j+1])
    return (byteCount)
    print value

def play_note(note, velocity): # turns on note
    print "             play_note:",
    # add code here to turn on note/lights
    if note <= 55:
        board.digital[4].write(0)
        print "board.digital[4].write(0)"
    elif note == 57:
        board.digital[5].write(0)
        print "board.digital[5].write(0)"
    elif note == 59:
        board.digital[6].write(0)
        print "board.digital[6].write(0)"
    elif note == 60:
        board.digital[7].write(0)
        print "board.digital[7].write(0)"
    elif note == 62:
        board.digital[8].write(0)
        print "board.digital[8].write(0)"
    elif note == 64:
        board.digital[9].write(0)
        print "board.digital[9].write(0)"
    elif note == 66:
        board.digital[10].write(0)
        print "board.digital[10].write(0)"
    elif note >= 67:
        board.digital[11].write(0)
        print "board.digital[11].write(0)"
    else:
        print "error - unknown note"

def stop_note(note): # turns off note
    print "             stop_note:",
    # add code here to turn off note/lights
    if note <= 55:
        board.digital[4].write(1)
        print "board.digital[4].write(1)"
    elif note == 57:
        board.digital[5].write(1)
        print "board.digital[5].write(1)"
    elif note == 59:
        board.digital[6].write(1)
        print "board.digital[6].write(1)"
    elif note == 60:
        board.digital[7].write(1)
        print "board.digital[7].write(1)"
    elif note == 62:
        board.digital[8].write(1)
        print "board.digital[8].write(1)"
    elif note == 64:
        board.digital[9].write(1)
        print "board.digital[9].write(1)"
    elif note == 66:
        board.digital[10].write(1)
        print "board.digital[10].write(1)"
    elif note >= 67:
        board.digital[11].write(1)
        print "board.digital[11].write(1)"
    else:
        print "error - unknown note"
        
def getTrackLength(loadMidi): # gets all header information and length of track
    with open(loadMidi, "rb") as file:
        global timeDivision
        # Display various header information
        fileHeaderID = file.read(4)
        print "Midi File Header: " + fileHeaderID
        file.seek(4,1)
        midiType = binascii.b2a_hex(file.read(2))
        print "Midi file type: " + midiType
        noOfTracks = binascii.b2a_hex(file.read(2))
        print "Number of tracks: " +noOfTracks
        timeDivision = binascii.b2a_hex(file.read(2))
        print "Time Division(ticks per quarternote): " + timeDivision
        trackHeaderID = file.read(4)
        print "Track Header ID: " + trackHeaderID
        file.seek(18)
        trackLength_hex = binascii.b2a_hex(file.read(4))
        trackLen = int(trackLength_hex, 16)
        print "Track length: ", trackLen, " bytes"
    return(trackLen)


    """
    bpm quarter note gets one beat, 8 ticks per quarter note,
    60 seconds in a minute:

    time.sleep(60) # one minute, so 120 bpm, therefore 8*120 ticks per minute
    so 960 ticks per minute. Thus 16 ticks per second. And one tick is 1/16
    of a second

    Finally:

    dv/((timeDivision*tempo)/60)
    """

def loadTrackToList(loadMidi, tl):  # begin looping through the track and adding track to list
    print "loadTrackToList()"
    with open(loadMidi, "rb") as file:
        
        file.seek(22)
        for i in range (0,tl):
            byte = file.read(1)
            track.append(byte)
            #print binascii.b2a_hex(track[i]),
    


def midiTrackLoop(tl): # loops through the midi track delta time, event, and repeats
    print "midiTrackLoop"
    trackCounter = 0 # set starting index to zero
    while trackCounter < tl: # loop through the track
      
        print "trackbyte #", trackCounter, #displays the index number of the track byte
        deltaTime, vlvBytes = getDelta_time(trackCounter)
        trackCounter += vlvBytes
        #value, velocity, eventBytes = checkMidi_event(trackCounter)
        eventBytes = checkMidi_event(trackCounter)
        trackCounter += 3
    time.sleep(2)

print "start"
Main()
print "end"
