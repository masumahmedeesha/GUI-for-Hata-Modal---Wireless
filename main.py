from tkinter import *
from tkinter import ttk
from FirstProblem import FirstProblem
from SecondProblem import SecondProblem

root = Tk()
root.title("MOBILE AND WIRELESS COMMUNICATION LAB (CSE 458)_2016331028")
root.geometry("800x750+50+50")

notebooks = ttk.Notebook(root)
firstFrameCC = Frame(notebooks)
secondFrame = Frame(notebooks)
notebooks.pack(expand=1, fill="both")
notebooks.add(firstFrameCC, text="CELL STRUCTURE")
notebooks.add(secondFrame, text="OKUMURA/HATA MODEL")

def entryCreation(frameObject, text):
    return ttk.Entry(frameObject, text=text, width=20)

def labelCreation(frameObject, text):
    return Label(frameObject, text=text, padx=15, pady=15)

firstFrame = LabelFrame(
    firstFrameCC, text="INPUT BOX (Please fill up all inputs correctly)")
firstFrame.grid(padx=30, pady=30, row=0, column=0)

def combineForFirst(rawText, text, rr):
    labelCreation(firstFrame, rawText).grid(row=rr, column=0, sticky='E')
    entryCreation(firstFrame, text).grid(row=rr, column=1,padx=20, pady=20)

totalArea = StringVar()
combineForFirst("Area size to cover (in km)", totalArea, 0)

selectedCell = StringVar()
cellOptions = ['MacroCell (1 to 10 km)', 'MicroCell (0.1 to 1 km)']
selectedCell.set(cellOptions[0])
labelCreation(firstFrame, "Cell type").grid(row=1, column=0, sticky='E')
firstOp = OptionMenu(firstFrame, selectedCell, *cellOptions)
firstOp.configure(width=18)
firstOp.grid(row=1, column=1)

radiusOfACell = StringVar()
combineForFirst("Radius of each cell (in km)", radiusOfACell,2)

frequencyAlotted = StringVar()
combineForFirst("Total number of frequencies allotted to the system",frequencyAlotted, 3)

reusefactor = StringVar()
combineForFirst("Frequency Reuse Factor (1, 3, 4, 7, 9, 12, 13, 16, and so on)", reusefactor, 4)

def printBoth(rr, text1, text2):
    Label(outputFrame, text=text1 + " = "+ str(text2), width=60).grid(row=rr, column=0, sticky='W')
    # Label(outputFrame, text=text2).grid(row=rr, column=1)

def errorHandling():
    Label(outputFrame, text=gg, width=60, fg="red", padx=7, pady=7).grid(row=0, column=0)

countedPrint = StringVar()
countedPrint.set(0)

def printResult():
    global outputFrame
    if (int(countedPrint.get()) == 1):
        outputFrame.destroy()

    outputFrame = LabelFrame(firstFrameCC, text="Output")
    outputFrame.grid(padx=10, pady=10, row=7, column=0, columnspan=2)
    global gg
    flag = True
    checking = radiusOfACell.get()
    if (checking):
        if selectedCell.get() == "MacroCell (1 to 10 km)":
            if (float(radiusOfACell.get()) > 1. and float(radiusOfACell.get()) <= 20.0):
                flag = True
            else:
                flag = False
                countedPrint.set(1)
                gg = "ERROR: MacroCell cell should be, 1.0 km < MacroCell <= 10.0"
                errorHandling()
                return
        elif selectedCell.get() == "MicroCell (0.1 to 1 km)":
            if (float(radiusOfACell.get()) <= 1.):
                flag = True
            else:
                flag = False
                countedPrint.set(1)
                gg = "ERROR: MicroCell should be less than or equal to 1.0"
                errorHandling()
                return

    if (flag and totalArea.get() and radiusOfACell.get() and frequencyAlotted.get() and reusefactor.get()):
        results = FirstProblem(areaSize=int(totalArea.get()), cellRadius=float(radiusOfACell.get(
        )), frequencyAlotted=int(frequencyAlotted.get()), reuseFactor=int(reusefactor.get()))
        
        countedPrint.set(1)
        # gg = ""
        printBoth(0, "Number of cells required", results.numberOfCells)
        printBoth(1, "Number of channels per cell",
                    results.channelsPerCell)
        printBoth(2, "Total channel capacity", results.totalCapacity)
        printBoth(3, "Total number of possible concurrent call",
                    results.totalCapacity)
    else:
        countedPrint.set(1)
        gg = "ERROR: Please fill up all inputs correctly, and SUBMIT again"
        errorHandling()

Button(firstFrame, text="SUMBIT", width= 30, padx=7, pady=7, command=printResult).grid(
    row=5, column=0, columnspan=2, padx=7, pady=7)

def destryAll():
    if (int(countedPrint.get()) == 1):
        outputFrame.destroy()

Button(firstFrame, text="CLEAR", command=destryAll, width= 30, padx=7, pady=7).grid(row=6, column=0, columnspan=2, padx=7, pady=7)


## ........................... SECOND_PROBLEM ............................................. ##

secondSecondaryFrame = LabelFrame(
    secondFrame, text="INPUT BOX (Please fill up all inputs correctly)")
secondSecondaryFrame.grid(padx=20, pady=30, row=0, column=0)

carrierFrequency = StringVar()
heightT = StringVar()
heightR = StringVar()
distance = StringVar()

def createCombine(frameObject, rawText, text, rr):
    labelCreation(frameObject, rawText).grid(row=rr, column=0, sticky="E")
    entryCreation(frameObject, text).grid(row=rr, column=1, padx=10, pady=10)

createCombine(secondSecondaryFrame,
              "Carrier frequency in MHz from 150 to 1500 MHz", carrierFrequency, 0)
createCombine(secondSecondaryFrame,
              "Height of transmitting antenna (base station) in m, from 30 to 300 m", heightT, 1)
createCombine(secondSecondaryFrame,
              "Height of receiving antenna (mobile unit) in m, from 1 to 10 m", heightR, 2)
createCombine(secondSecondaryFrame,
              "Propagation distance between antennas in km, from 1 to 20 km", distance, 3)

selectedCity = StringVar()
cityOptions = ["Small/Medium", "Large"]
selectedCity.set(cityOptions[0])
labelCreation(secondSecondaryFrame, "City size").grid(
    row=4, column=0, sticky="E")
jjst = OptionMenu(secondSecondaryFrame, selectedCity, *cityOptions)
jjst.configure(width=17)
jjst.grid(row=4, column=1)

selectAreaType = StringVar()
areaTypes = ["Urban", "Suburban", "Open area"]
selectAreaType.set(areaTypes[0])
labelCreation(secondSecondaryFrame, "Area type").grid(
    row=5, column=0, sticky="E")
aty = OptionMenu(secondSecondaryFrame, selectAreaType, *areaTypes)
aty.configure(width=17)
aty.grid(row=5, column=1)

def printResultForSecond(frameObject, extra):
    if (extra == 0):
        Label(frameObject, text=outputSecond, width=70, fg="red").grid(row=0, column=0, padx=10, pady=10)
    else:
        Label(frameObject, text=outputSecond, width=70).grid(row=0, column=0, padx=10, pady=10)

countedPrintForSecond = StringVar()
countedPrintForSecond.set(0)

def printOutputOfHata():
    global outputFrameForSecond
    global outputSecond

    if (int(countedPrintForSecond.get()) == 1):
        outputFrameForSecond.destroy()

    outputFrameForSecond = LabelFrame(secondFrame, text="Output")
    outputFrameForSecond.grid(padx=20, pady=20, row=8, column=0, columnspan=2)

    if (carrierFrequency.get() and heightT.get() and heightR.get() and distance.get() and selectedCity.get() and selectAreaType.get()):
        if (int(carrierFrequency.get()) < 150 or int(carrierFrequency.get()) > 1500):
            countedPrintForSecond.set(1)
            outputSecond = "ERROR: Carrier frequency should be from 150 to 1500 MHz"
            printResultForSecond(outputFrameForSecond,0) 
            return
        elif(int(heightT.get()) < 30 or int(heightT.get()) > 300) :
            countedPrintForSecond.set(1)
            outputSecond = "ERROR: Height of transmitting antenna (base station) should be from 30 to 300 m"
            printResultForSecond(outputFrameForSecond,0)
            return
        elif (int(heightR.get()) < 1 or int(heightR.get()) > 10):
            countedPrintForSecond.set(1)
            outputSecond = "ERROR: Height of receiving antenna (mobile unit) should be from 1 to 10 m"
            printResultForSecond(outputFrameForSecond,0)
            return
        elif (int(distance.get()) < 1 or int(distance.get()) > 20 ):
            countedPrintForSecond.set(1)
            outputSecond = "ERROR: Propagation distance between antennas should be from 1 to 20 km"
            printResultForSecond(outputFrameForSecond,0)
            return
        infos = SecondProblem(carrierFrequency=int(carrierFrequency.get()),
                            heightT=int(heightT.get()),
                            heightR=int(heightR.get()),
                            distance=int(distance.get()),
                            selectedCity=selectedCity.get(),
                            selectAreaType=selectAreaType.get())
        countedPrintForSecond.set(1)
        outputSecond = "Predicted Path loss is " + str(infos.pathLoss) + " dB"
        printResultForSecond(outputFrameForSecond,1)
    else:
        countedPrintForSecond.set(1)
        outputSecond = "ERROR: Please fill up all inputs correctly, and SUBMIT again"
        printResultForSecond(outputFrameForSecond,0)

def clearHataOutput():
    if (int(countedPrintForSecond.get()) == 1):
        outputFrameForSecond.destroy()
    # countedPrintForSecond.set(1)
    # outputFrameForSecond.destroy()
    


Button(secondSecondaryFrame, text="SUBMIT", width=30, padx=7, pady=7, command=printOutputOfHata).grid(
    row=6, column=0, columnspan=2, padx=7, pady=7)
Button(secondSecondaryFrame, text="CLEAR", width=30, padx=7, pady=7, command=clearHataOutput).grid(
    row=7, column=0, columnspan=2, padx=7, pady=7)


root.mainloop()
