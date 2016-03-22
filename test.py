import itertools

globalGroup = 'abcdefghijkl'
globalCombinations = itertools.combinations(globalGroup,3)

exploredGroup = set()

stateStack = [set([i]) for i in globalCombinations]
currentState = None

iterator = 0

while len(stateStack) > 0:
    currentState = stateStack.pop()
    currentGroup = 'abcdefghijkl'
    for group in list(currentState):
        for student in group:
            currentGroup = currentGroup.replace(student,'')
    currentCombinations = itertools.combinations(currentGroup,3)
    if len(currentState) == 3:
        currentState.add(list(currentCombinations)[0])
        exploredGroup.add(frozenset(currentState))
    else:
        for newGroup in currentCombinations:
            addingState = set(currentState)
            addingState.add(newGroup)
            stateStack.append(addingState)

for entry in exploredGroup:
    line = ''
    for group in entry:
        for student in group:
            line += student
        line += ','
    print line
