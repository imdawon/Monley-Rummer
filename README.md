# The Purpose of MonleyRummer
Use android MonkeyRunner to brute force the "My Eyes Only" photo locker.

## The Target
Snapchat's "My Eyes Only" (sometimes reffered to as MEO) encrypted photos folder.

## My Eyes Only (MEO) Behavior:
* To open the folder, you must enter a 4 digit passcode using only numbers. 
* After 5 failed passcode attempts, the folder will deny any additional access attempts for 60 seconds. 
  **NOTE: We are attempting 4 logins per set. Once you enter 5 incorrect passcodes, the following passcode input, even if it is correct, will still lock you out and deny future passcode submissions.
* After 60 seconds are up, you again can attempt an additonal **4** times, leading to another 60 second lockout.

### My Eyes Only Protection (MEO) Features ###
* Using traditional MonkeyRunner "MonkeyDevice.DOWN_AND_UP" function is detected in someway by Snapchat. Once you do 10 login attempts, which includes 2 logouts, Snapchat will lock MEO as if we had entered 5 wrong passcodes

## The Method
1. With snapchat open, navigate to the MEO passcode lock screen.
2. MonkeyRunner emulates screen taps and enters passcodes in traditional brute-force order: 1111, 1112, 1113, etc...
3. After 4 failed login attempts, MonekyRunner will tap the top left "down" arrow to close the passcode lock screen
4. MonkeyRunner will tap the top left again to open the user profile window.
5. MonkeyRunner will tap the Settings icon.
6. MonkeyRunner will scroll down to Log Out button and tap it. It will then tap the Log Out buttton in dialog box.
7. MonkeyRunner will wait 3 seconds, then tap "Log in as <lastLoggedInUsernameHere>" and wait 7 seconds to authenticate.
8. MonkeyRunner will tap the bottom middle icon to open the "Memories" section. From here, it will tap "My Eyes Only" and repeat starting at step 2.

## The Numbers
### A "set" is defined as 5 passcode attempts that lead to a 60 sec cooldown / lockout period where we must log out and in again to clear this cooldown
* A 4 digit passcode at max is 10,000 different combinations.
* We can enter 4 passcodes per "set"
* This means, at max, we will have 2,500 passcode attempt "sets".

**Brute force duration estimates are not currently used due to early development as we learn new things about the protection features of My Eyes Only**
