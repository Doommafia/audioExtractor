from moviepy.editor import VideoFileClip
from tkinter import Tk
from tkinter import filedialog

# timeConverter
def timeSecs(timeStr):
    try:
        m, s = map(int, timeStr.split(':'))
        return m * 60 + s
    except:
        print("Invalid time format - MM:SS")
        return None

def extAudio(vidFile, outFile, startTime=None, endTime=None):
    try:
        video = VideoFileClip(vidFile)
        if startTime and endTime:
            startSecs = timeSecs(startTime)
            endSecs = timeSecs(endTime) if endTime not in ["all", "end"] else video.duration
            video = video.subclip(startSecs, endSecs)
        audio = video.audio
        audio.write_audiofile(outFile)
    except Exception as e:
        print(f"Error: {e}")

def userInputs():
    Tk().withdraw()
    vidFile = filedialog.askopenfilename() 
    outFile = filedialog.asksaveasfilename()

    print("1 Entire vid")
    print("\n2 Specific part")
    choice = input(">")

    if vidFile and outFile:
        if choice == '1':
            extAudio(vidFile, outFile)
        elif choice == '2':
            startTime = input("Start time (MM:SS): ")
            endTime = input("End time (MM:SS or 'all'/'end'): ")
            if endTime in ["all", "end"]:
                endTime = None
            extAudio(vidFile, outFile, startTime, endTime)
        else:
            print("Invalid choice")
    else:
        print("No file selected.")

userInputs()
