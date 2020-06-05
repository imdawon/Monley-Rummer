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

## The Numbers
### A "set" is defined as 5 passcode attempts that lead to a 60 sec cooldown / lockout period where we must log out and in again
* A 4 digit passcode at max is 10,000 different combinations.
* We can enter 5 passcodes per "set"
* This means, at max, we will have 2,000 passcode attempt "sets".
* I estimate it will take 2 seconds to enter 5 passcode attempts. It will then take 2 seconds to log out, a 3 second wait, 7 seconds to log back in, and then 2 seconds to get back to enter another passcode set. This means our maximum amount of time it will take to brute force the correct passcode will be around 8.88 hours.

My calculations are as follows *they may be wrong!:*

2000 sets * 16 seconds set duration = 533.33 seconds total
533.33 seconds / 60 = 8.88 hours
