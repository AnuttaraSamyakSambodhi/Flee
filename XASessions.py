import pandas as pd
import win32com.client
import pythoncom

class XASessionEvent(object):
    login_state = 0

    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def OnLogin(self, code, msg):
        if code =="0000":
            print("로그인 성공")
            XASessionEvent.login_state = 1
        else:
            print("로그인 실패")

instXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEvent)

"""
계좌정보 = pd.read_csv("secret/passwords.csv")
주식계좌정보 = 계좌정보.query("구분 == '거래'")
id = 주식계좌정보['사용자ID'].values[0].strip()
passwd = 주식계좌정보['비밀번호'].values[0].strip()
cert_passwd = 주식계좌정보['공인인증비밀번호'].values[0].strip()
url = 주식계좌정보['url'].values[0].strip()
"""
id = "lokavid"
passwd = "m5s78qu4"
cert_passwd = "[anuttara]0"


instXASession.ConnectServer("hts.ebestsec.co.kr", 20001)
instXASession.Login(id, passwd, cert_passwd, 0, 0)

while XASessionEvent.login_state == 0:
    pythoncom.PumpWaitingMessages()

num_account = instXASession.GetAccountListCount()

for i in range(num_account):
    account = instXASession.GetAccountList(i)
    print(account)

"""
계좌 = []
계좌수 = instXASession.GetAccountListCount()

for i in range(계좌수):
    계좌.append(instXASession.GetAccountList(i))

return(True, 0, "OK", 계좌, instXASession)"""



