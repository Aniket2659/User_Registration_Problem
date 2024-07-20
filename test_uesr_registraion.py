from src.user_registration import UserRegistration

def test_users_first_name():
    # test case for valid first name
    result=UserRegistration().users_first_name('Aniket')
    assert result==True

    # test case for invalid first name
    result=UserRegistration().users_first_name('aniket')
    assert result==False

    # test case for invalid first name
    result=UserRegistration().users_first_name('ani')
    assert result==False


def test_users_last_name():
    # test case for valid last name
    result=UserRegistration().users_last_name('Babar')
    assert result==True

    # test case for invalid last name 
    result=UserRegistration().users_last_name('babar')
    assert result==False

    # test case for invalid last name 
    result=UserRegistration().users_last_name('ba')
    assert result==False

def test_email():
    # test case for valid email 
    result=UserRegistration().validate_email('abc.xyz@bl.co.in')
    assert result==True

    # test case for invalid email 
    result=UserRegistration().validate_email('abc.xyz@bl')
    assert result==False

    # test case for invalid email 
    result=UserRegistration().validate_email('abc@bl.co')
    assert result==False

def test_mobile_number():
    # test case for valid mobile number
    result=UserRegistration().mobile_number('91 7387837430')
    assert result==True

    # test case for invalid mobile number
    result=UserRegistration().mobile_number('7387837430')
    assert result==False

    # test case for invalid mobile number
    result=UserRegistration().mobile_number('917387837430')
    assert result==False

def test_password_rules():
    # test case for valid password 
    result=UserRegistration().password_rules('7387837430@aA')
    assert result==True

    # test case for invalid password
    result=UserRegistration().password_rules('7387837430')
    assert result==False

    # test case for invalid password
    result=UserRegistration().password_rules('333344478@a')
    assert result==False

    # test case for invalid password
    result=UserRegistration().password_rules('hgwehfgjgkgew')
    assert result==False
