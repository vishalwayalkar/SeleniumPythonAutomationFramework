from test.Keywords.LoginKeywords import LoginKeywords
from test.Profiles.ENTProfile import ENTProfile
from test.conftest import Base

class Test_InValid_Login_Credential(Base):
    def test_invalid_login_credential(self):
        LoginKeywords.login_in_with_invalid_credential(self.driver, ENTProfile.USERNAME, ENTProfile.PASSWORD1)
