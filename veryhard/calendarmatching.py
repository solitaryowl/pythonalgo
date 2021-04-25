# https://www.algoexpert.io/questions/Calendar%20Matching


def createFreeSlots(calendar,dailyBounds):
    slotsArr = []
    right = dailyBounds[0]
    for i in range(0, len(calendar)):
        current = calendar[i]
        if current[0] > right:
            slotsArr.append([right, current[0]])
            right = current[1]
        else:
            right = current[1]
    if right < dailyBounds[1]:
        slotsArr.append([right,dailyBounds[1]])
    return slotsArr

def overlap(slot1, slot2):
    start1 = slot1[0]
    start2 = slot1[0]
    end1 = slot1[1]
    end2 = slot2[1]

    if (start1 >= end2) | (start2 >= end1):
        return False
    return True
#
def getOverlap(slot1,slot2):
    start1 = slot1[0]
    start2 = slot2[0]
    end1 = slot1[1]
    end2 = slot2[1]

    result=[]

    result.append(max(start1,start2))
    result.append(min(end1,end2))
    return  result

def slotLength(slot):
    return minutes(slot[1])- minutes(slot[0])

def minutes(num):
    hours= int(num)
    mins = hours * 60 + round((num - hours)*100,2)
    return mins




def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Write your code here.

    calendar1=list(map(lambda m: [float(m[0].replace(":",".")), float(m[1].replace(":","."))], calendar1))
    calendar2 = list(map(lambda m: [float(m[0].replace(":",".")), float(m[1].replace(":","."))], calendar2))
    dailyBounds1 = list(map(lambda m: float(m.replace(":",".")), dailyBounds1))
    dailyBounds2 = list(map(lambda m: float(m.replace(":", ".")), dailyBounds2))
    results=[]
    slotsArr1 = createFreeSlots(calendar1, dailyBounds1)
    slotsArr2 = createFreeSlots(calendar2, dailyBounds2)
    i=0;
    j=0;
    results=[]
    while i < len(slotsArr1):
        curr1 = slotsArr1[i]
        while j <len(slotsArr2):
            curr2 = slotsArr2[j]
            if overlap(curr1,curr2):
                slot = getOverlap(curr1,curr2)
                if slotLength(slot) >= meetingDuration:
                    results.append(slot)
                i = i+1
                j = j+1
                break
            else:
                if curr2[0] >= curr1[1]:
                    i=i+1
                    break
                else:
                    j=j+1

    results = list(map(lambda m: [str(m[0]).replace(".",":"), str(m[1]).replace(".",":")], results))




if __name__ == '__main__':
    arr=[["11.0","12.3"]]
    print(float("9.00"))
    print(list(map(lambda m: [float(m[0]),float(m[1])],arr)))
    cal1=[
        ["9:00", "10:30"],
        ["12:00", "13:00"],
        ["16:00", "18:00"]
    ]

    db1=["9:00", "20:00"]

    cal2= [
        ["10:00", "11:30"],
        ["12:30", "14:30"],
        ["14:30", "15:00"],
        ["16:00", "17:00"]
    ]
    db2=["10:00", "18:30"]
    calendarMatching(cal1,db1,cal2,db2,30)

    # cal1= [[9.0, 10.30],[12.0, 13.0],[16.0,18.0]]
    # cal2 = [[10.0, 11.3],[12.3,14.3],[14.3,15.0],[16.0,17.0]]
    # dailyBounds1= [9.0,20.0]
    # dailyBounds2=[10.0, 18.3]
    # duration=30
    # calendarMatching(cal1,dailyBounds1,cal2,dailyBounds2,duration)

