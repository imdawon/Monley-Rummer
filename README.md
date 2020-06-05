# The Purpose of MonleyRummer
Use android MonkeyRunner to brute force the "My Eyes Only" photo locker.

## The Target
Snapchat's "My Eyes Only" encrypted photos folder.

## My Eyes Only Behavior:
* To open the folder, you must enter a 4 digit passcode using only numbers. 
* After 5 failed passcode attempts, the folder will deny any additional access attempts for 60 seconds.
* After 60 seconds are up, you again can attempt 5 times, leading to another 60 second lockout.

## The Method
1. With snapchat open, navigate to the "My Eyes Only" passcode lock screen.
2. MonkeyRunner emulates screen taps and enters passcodes in traditional brute-force order: 1111, 1112, 1113, etc...
3. After 5 failed login attempts, MonekyRunner will tap the top left "down" arrow to close the passcode lock screen
4. MonkeyRunner will tap the top left again to open the user profile window.
5. MonkeyRunner will tap the Settings icon.
6. MonkeyRunner will scroll down to Log Out button and tap it. It will then tap the Log Out buttton in dialog box.
7. MonkeyRunner will wait 3 seconds, then tap "Log in as <lastLoggedInUsernameHere>" and wait 7 seconds to authenticate.
8. MonkeyRunner will tap the bottom middle icon to open the "Memories" section. From here, it will tap "My Eyes Only" and repeat starting at step 2.
