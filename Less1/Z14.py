def bananas(strmain) -> set:

    def wordcounter(strmain, strcheck, strnew):
        if strcheck == '':
            diff = len(strmain)
            if diff > 0:
                strnew += '-' * diff
            result.add(strnew)
            return
        for i in range(len(strmain) - len(strcheck) + 1):

            if strmain[0] == strcheck[0]:

                wordcounter(strmain[1:], strcheck[1:], strnew + strcheck[0])

            strnew += '-'
            strmain = strmain[1:]

    strcheck = 'banana'
    result = set()
    strnew = ''

    if len(strmain) < len(strcheck):
        return result

    wordcounter(strmain, strcheck, strnew)
    return result

    

