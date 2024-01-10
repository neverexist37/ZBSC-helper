import requests
from io import BytesIO
from PIL import Image
import ZBSCCaptcha

baseUrl = "https://fe.xuanen.com.tw/"
captchaURL = baseUrl + "NewCaptcha.aspx"
loginUrl = baseUrl + "fe02.aspx?Module=login_page&files=login"

defaultHeaders = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

def login(user, password, maxErrRetry = 3):
    ss = requests.session()
    ss.headers = defaultHeaders
    
    retryCnt = 0
    rtnSession = None

    while (retryCnt < maxErrRetry):
        try:
            resp = ss.get(captchaURL)
            assert (resp.status_code == 200), "fail to fetch captcha"

            img = Image.open(BytesIO(resp.content))
            captchaCode = ZBSCCaptcha.recognize(img)
            assert (captchaCode != None), "fail to recognize captcha"

            postData = {"loginid": user, "loginpw": password, "Captcha_text": captchaCode}
            resp = ss.post(loginUrl, data = postData)
            assert (resp.status_code == 200), "fail to login"

            respFirstLine = str(resp.text).split("\n")[0].strip()
            assert (respFirstLine == ""), "login resp error: %s" %(respFirstLine)

        except Exception as e:
            print(e)
            retryCnt += 1

        else:
            rtnSession = ss
            break

    return rtnSession
