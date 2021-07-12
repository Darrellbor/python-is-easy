candList=["'i Love Jesus","'Oceans","Crowns","King of heaven"]
votersRank=[["'i Love Jesus","'Oceans","Crowns","King of heaven"],["Crowns","'i Love Jesus","'Oceans","King of heaven"],["'Oceans","Crowns","'i Love Jesus","King of heaven"],["Crowns","'Oceans","'i Love Jesus","King of heaven"],["'Oceans","'i Love Jesus","Crowns","King of heaven"],["'Oceans","'i Love Jesus","Crowns","King of heaven"],["'Oceans","'i Love Jesus","Crowns","King of heaven"],["'Oceans","'i Love Jesus","Crowns","King of heaven"],["'Oceans","'i Love Jesus","Crowns","King of heaven"]]


def ballot(a):
    b={}
    a_len=len(a)
    for i in range (len(a)):
        b[i]=a_len-i
    return b

def indextoPoint(a,b):
    return b[a]

def tally(candList,votersRank):
    scoreTable=ballot(candList)
    Tally={}
    for i in range(len(candList)):
        count=0
        for vote in votersRank:
            index=vote.index(candList[i])
            print('vote index: ',index, 'vote: ', vote);
            count+=(indextoPoint(index,scoreTable))
        Tally[candList[i]]=count
    return Tally

print (tally(candList,votersRank))