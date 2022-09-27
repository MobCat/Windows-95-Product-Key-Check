## Windows 95 Product Key Check ##

**Info:**<br>
This is a python implementation of the windows 95 product key check.<br>
This was just a bit of fun and a massive 5 hour "I got distracted from what I was working on" thing
so at the end of the day it was just something fun to work on and isn't meant to be taken seriously, 
we are just seeing how other people have done things so we can learn from them.<br>
And yeah because it was "just for fun" it's kinda shitty and my check isn't 100% the same as how Microsoft did it but if this script said it's valid then it should also be valid for the windows 95 install disk. However there is a <sup>very small</sup> chance there is a key that works on the legit windows 95 install but not on my check, but will cross that bridge when I find a way to legit install win 95 and mess with the real key checker.
<br><br>

**How to use:**<br>
First off you need to have python 3 installed and that's about it.<br>
Download the scrip then run `python win95check.py` in the same folder as you downloaded it to and it will ask you for a key. If your getting and error, try `python3 win95check.py`.<br>
type or paste in the key **WITH** the **-** then press enter.<sup>\*1</sup><br>
The scrip will auto detect if it's a Retail or OEM key and then will tell you if it's valid or not.<br>
The scrip will just keep asking you for a valid key until you enter a valid one, then it quits.<br>
You can force a quit by pressing `crtl+c`.<br>

**Updates:**<br>
20211023: So I finally fix my VM issues and got win 95 working / installing so I can poke at the OEM installer.<br>
Yeah this one is odd. A little ground work to save some time<br>
11101-OEM-0222222-33333<br>
bank 1 - OEM Bank - Bank 2 - Bank 3<br>
Can confirm that bank 1 can be separated from the rest of the key, so you can use a date from another key, or any valid date really eg. 36695 is a valid date according to the check but not IRL as 1995 was not a leap year.<br>
And that the 3rd bank can be separated aswell, just type the first 2 banks and then enter random numbers and the key should work fine.<br>
It also appears to pass the Y2K issue fine aswell, so yeah might of just fluked that one as they are combining and checking the day and year into one int. and i'm just using a list for the year.. so we both just barely pass..<br>
Even know the first and second - are checked kinda according to the decompile and the third - is not.<br>
You can't edit or change any of the -'s or the OEM text, you only get 3 text boxes to enter the 3 banks of the key, not one big box like the Retail install. So I've added a single check for the leading 0 on the mod7 and the 3rd - to error out if they are missing, it's not the cleanest but it works.<br>
As I'v never installed OEM win 95 I did not know you couldn't change the OEM bank either so my -OEM- check is fine. Also makes sense why the decompile didn't check it as you can't change it in the first place.<br>
Also can confirm the 3rd bank has to be numbers, it can't be text but it looks like I already had an error for this anyways. Just wanted to check if it matched the legit installer.<br>
I also change the terminology from key type to key weight to better suite whatever this made up value is.<br>
To get a "legit" key you want a weight of 2.0~4.0. There are a few 5.0 keys but most of the legit ones I have found so far are always 3.0 or 4.0 and very sometimes 2.0 but enough to me not a fluke.
 

**Retail key layout and check:**<br>
111-1111111<br>
000-0000007<br>
123-0926792<br>
Check the first 3 numbers to see if they are black listed,<br>
The black listed numbers are 333, 444, 555, 666, 777, 888 and 999.<sup>\*2</sup><br>
Then sum the remaining numbers (sum = 0+9+2+6+7+9+2).<br>
Then divide that sum by the length of the string, in this and all cases, 7 (sum/7).<br>
In the decompile this is referred to as "mod7" so I'll refer to it as that as well.<br>
Then if this mod7 can be divided without remainders and returns a "key weight" of something like 4.0 then it's a valid key<br>
If it returns a "key weight" of something like 3.142857142857143 then it's not a valid key.<br>
So basically, if the sum of the key can be divided into 7 then the installer thinks it's a valid key.
not sure if the remaining hole number was ever used eg.<br>
1.0 is a valid win 95 key and 3.0 is a valid 95 B (OSR2) key.<br>
I originally made up this "key weight" function as all the legit keys I found where always coming back as 4.0
and any of the fake made up ones where 1.0 and sometimes 2.0, but then I started to find some legit 2.0, 3.0 ones.<br>
So far though legit keys (as in I can find a scan of a product sticker or booklet on Google images) only return a key weight of 2.0, 3.0 and 4.0, no higher or lower, but I'll keep looking. But yeah it seems if you want to make a "legit" key you want a weight of around 3.0 or 4.0 and as less repeating numbers as possible. so 000-9999956 is a valid key according to the checker but MS would of never used it.<br>

**Retail key layout and check:**<br>
11101-OEM-1111111-11111<br>
00100-OEM-0000000-00000<br>
12395-OEM-0926792-36579<br>
The first 5 numbers is the date in DDDYY where D is on what day of the year the key was generated.<sup>\*3</sup><br>
-OEM- is static and never changes.<sup>\*4</sup><br>
The 3rd part of our key is the same mod7 check as the retail key.<br>
The last part of the key appears to be a random integer and doesn't seem to affect the check however,
it will fail if you enter a string or letters of any kind, only numbers are allowed.<br>

**Citations oddities and improvements:**<br>
Citation \*1:<br>
It doesn't appear that the - is correctly checked in the Retail installer.<br>
Its only checking for length not that the character is correct,<br>
so yol-1111111 and yolo1111111 is a valid key.<br>
However the - is checked in the OEM key, but poorly.<br>
I'm not that good at this but from what I read from the decompile, it checks the key length is 23, then checks if - is at position 6 and 10, and that's it, it skips / doesn't check the - at position 18 so<br>
12395-OEM-0926792-36579 and 12395-OEM-0926792136579 *should* be a valid key, however I haven't got a way of checking this right now.<br>
My key check just checks for "`-OEM-`" checking for the - and if it's a OEM key at the same time.<br>

Citation \*2:<br>
This blacklist outside of how week it is that ima skip over is very odd. It's only purpose is to check for those numbers on the blacklist and nothing else, it's skips 000, 111 and 222 for some reason, and it's also not blocking things like 123, 321, 987, etc.. So this blacklist really needs to be changed to a whitelist of allowed key types for eg. 371-1111111 is Home and 574-1111111 is Pro and everything else is blocked. Audodesk products have the same sorta check for reference, a key that contains 001H1 is always AutoCAD 2016.
Also how the blacklist is parsed by the legit installer it's only checking for integers, strings are ignored / skipped,
So yol-1111111 is a valid key. Or if your old enough to remember old key cracking groups, FFF-1111111 is a valid key too.
My key check will error out if the number is not an integer, however I have "bypassed" (\***cough**\* print ("") to skip cos I don't remember how to do a "do nothing" in a try statement \***cough cough**\*) that error to be more authentic to the original MS key checker.<br>

Citation \*3:<br>
This one is kinda fun. So yes the first 5 numbers are checked to be a date, it is believed this is the date the
key was generated as the date only goes from 1995 to 2002 so this is more or less believable.<br>
The fun thing is as far as I read this decompile it is accounting for the leap year in 1996 and 2000 but,<br>
36695, 36602, etc are valid keys but not valid dates as 1995 and 2002 are not leap years / don't have 366 days in them.<br>
Also just to rub salt into this wound, this date check is not Y2K compliant. I'm not 100% if it's just my code that's not or it's both but in my code the year 00 returns just 0 and 01 returns just 1. 95 will return 95 though.<br>
It doesn't affect the check as to do this in python I had to do a list for the year not a range as you can't
well overflow a range from 99 back to 0 but year 0 is on the list so the key is valid.<br>
However hypothetically, if you just did a check for is year == 1 then it would always pass, as 1 will be passed as a bool not a number.

Citation \*4:<br>
As far as I know the OEM text is always the same for a OEM key. I saw *only one* screen shot of someone in Greece trying to install win 95 and they did type OEM in Greek but there was a message on the screen but I can't read Greek to know what it was. From what I can read of the decompile though, the OEM part isn't check or at least not with a string soo 12395-FFF-0926792-36579 *might be* a valid OEM key but have not checked.<br>
My key check will fail though if you type anything else but -OEM- as I'm checking both the - and OEM at the same time and the legit check does check for those - there.<br>

**Differences:**<br>
My key check will automatically detect what key you have entered, check the right key, then set a Retail or OEM flag to be used in the other parts of the installer.<br>
The legit windows 95 key check has what version it is set by the disk it's self / another part of the installer, so the legit check will check the disk if it's OEM or Retail and then only let you enter a OEM or Retail key according to your disk type. You would have to recompile / rebuild the disk to change what type of win95 you wanted to install instead of all versions of windows being on the disk and you just select which to install with the key.<br>
Pros and cons of doing this of course, less disks to print however, the trial versions of quake 1 had the full ver of quake on the disk, you just rang up, give them money and they would give you a key to re-install with or just add to the game, but as soon as the key got cracked all the free demo disks are now free full versions of the game.<br>
Curiously according to the decompile this OEM vs Retail check has 9 checks, check no.5 is about the retail key length I think, no.6 is the retail key check, no.9 is the OEM key check, no.8 is another OEM key check but it's not setting the ret variable like the rest of the checks are so might be broken, but on the subject of broken the other 6 disk types don't have a check sooo I'm guessing if you set your disk to type no.1 it will just skip the key check screen entirely *or* will fail to the next check until it hits a check that lets you check a key. Not sure and that one would be really hard to check.<br>
Either way, it's still weird to check for 9 different things and only use like 2.5 of them...<br>
The way I'm doing my mod7 check is a little cleaner then how it's done in the legit install.<br>
Python just has a math function for does this number divide equally or not, return a 0 or 1.<br>
However I am unpacking the OEM key into 23 separate variables soo, you win some you lose some.<br>


**Sources:**<br>
The stacksmashing video on win95 keys<br>
https://www.youtube.com/watch?v=cwyH59nACzQ<br>
The decompile of the OEM key check function<br>
https://gist.github.com/nezza/a25bee13f25a1733a4c7a1d3d1cf5882<br>

In conclusion, thank you for coming to my long ted talk about checking windows 95 keys. I don't think the real windows 95 key has been fully cracked open yet as all the legit ones seem to only return a very specific "key weight" range and our generated ones just return whatever but for now what we have works with the legit win 95 install and matches what we can gleam from the decompile soo this was a fun ride but, I really have to get back to my day job now.... That I got distracted from like 2 days.
