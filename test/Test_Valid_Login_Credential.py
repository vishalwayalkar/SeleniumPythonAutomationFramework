from test.conftest import Base
from test.Keywords.LoginKeywords import LoginKeywords
from test.Profiles.ENTProfile import ENTProfile

class Test_Valid_Login_Credential(Base):
    def test_valid_login_credential(self):
        LoginKeywords.login_in_with_valid_credential(self.driver, ENTProfile.USERNAME, ENTProfile.PASSWORD)
        LoginKeywords.log_out(self.driver)
