import re

baseUrl = "https://fe.xuanen.com.tw/"
bookingUrl = baseUrl + "fe02.aspx?module=net_booking&files=booking_place&StepFlag=25&PT=1"

placeIdTable = {
    "2F羽 1" : "83",
    "2F羽1" : "83",
    "2F羽2" : "84",
    "2F羽3" : "1074",
    "2F羽4" : "1075",
    "2F羽5" : "87",
    "2F羽6" : "88",
    "2F羽7" : "2115",
    "2F羽8" : "2116",
}

def book(session, date, hour, placeId, maxErrRetry = 1):
    queryParamters = "&D=%s&QTime=%d&QPid=%s" %(date.strftime("%Y/%m/%d"), hour, placeId)
    queryUrl = bookingUrl + queryParamters
    retryCnt = 0

    while (retryCnt < maxErrRetry):
        try:
            resp = session.get(queryUrl)
            assert (resp.status_code == 200), "fail to book"

            bookid = re.search("Y=([0-9]+)", resp.text).group(1)
            return bookid if (bookid != "0") else None

        except Exception as e:
            print(e)
            retryCnt += 1

    return None


