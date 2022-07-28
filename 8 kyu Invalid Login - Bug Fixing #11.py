def validate(username, password):
    if username.lower() != password.lower() or password.lower() != 'password' or '//' in password or '||' in password:
        return 'Wrong username or password!'
    return 'Successfully Logged in!'



print(validate('Timmy', 'password'), 'Successfully Logged in!', "Should succefully login!")
print(validate('Timmy', 'h4x0r'), 'Wrong username or password!', "The password was wrong")
print(validate('Alice', 'alice'), 'Successfully Logged in!', "Should succefully login!")
print(validate('Timmy', 'password"||""=="'), 'Wrong username or password!',
      "Should fail to login because of injected code")
print(validate('Admin', 'gs5bw"||1==1//'), 'Wrong username or password!',
      "Should fail to login because of injected code")
