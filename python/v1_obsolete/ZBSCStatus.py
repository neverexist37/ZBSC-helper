from bs4 import BeautifulSoup

baseUrl = "https://fe.xuanen.com.tw/"
placeStatusUrl = baseUrl + "fe02.aspx?module=net_booking&files=booking_place&StepFlag=2&PT=1"

def parseBadmintonResp(respText):
    try:
        badmintonDict = {}
        respBS = BeautifulSoup(respText, "html.parser")
        placeElements = respBS.select_one("span#ContentPlaceHolder1_Step2_data table").select("tr")[1:]

        for placeElement in placeElements:
            data, dataIdx = placeElement.select("td"), 0

            if (data[dataIdx].has_attr('rowspan')):
                currKey = data[dataIdx].text[:2]
                badmintonDict[currKey] = []
                dataIdx += 1

            bookingBtnImg = data[dataIdx + 2].select_one("img")
            if (bookingBtnImg != None) and (not bookingBtnImg.has_attr("title")):
                placeName = data[dataIdx].text
                badmintonDict[currKey].append(placeName)

        return badmintonDict
    except:
        return None

def getBadmintonStatus(session, date, daySection = 1, maxErrRetry = 1):
    queryParamters = "&D=%s&D2=%d" %(date.strftime("%Y/%m/%d"), daySection)
    queryUrl = placeStatusUrl + queryParamters
    retryCnt = 0

    while (retryCnt < maxErrRetry):
        try:
            resp = session.get(queryUrl)
            assert (resp.status_code == 200), "fail to fetch badminton status"

            return parseBadmintonResp(resp.text)

        except Exception as e:
            print(e)
            retryCnt += 1

    return None

    