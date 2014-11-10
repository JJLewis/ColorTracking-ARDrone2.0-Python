RedBallTracking-ARDrone2.0-Python
=================================

Track a red ball with an ARDrone 2.0 through its camera.

Follows a fairly large red object (a ball maybe) by rotating around in the air and ascending and descending.

Important Notes Before Continuing
=================================

The following are not currently in the documentation but should be in the near future.
1. Xcode Command Line Tools must be installed before anything else.
2. If you are running into issues with being unable to import PIL.Image into the program, simply comment it out with a # as it is not longer required.
```Python
# import PIL.Image
```
3. If you are getting warnings about battery percentage and the drone won't take off. Find the following section of code:
```Python
        # Get battery status of the drone
				bat = drone.navdata.get(0, dict()).get('battery', 0)
				#print str(bat)
				if bat < 20:
					running = False
					print "Low Battery: "+str(bat)
```
Once you have found it. You can:
  1. Remove the whole section
  2. Comment out
    ```Python
    running = False
    ```
    or
    ```Python
    print "Low Battery: "+str(bat)
    ```
    The first option will stop it from landing and disconnecting, and the second option will stop it from printing the warnings.
    If you want to comment out both you, it must look like this:
    ```Python
        # Get battery status of the drone
				bat = drone.navdata.get(0, dict()).get('battery', 0)
				#print str(bat)
				if bat < 20:
					#running = False
					#print "Low Battery: "+str(bat)
					pass
    ```
3. If you would like to change the target color of the object you are tracking, find the following lines of code near the top of the program:
```Python
TARGET_COLOR_MIN = np.array([0,100,100], np.uint8)
TARGET_COLOR_MAX = np.array([5,255,255], np.uint8)
```
Here, the values inside the square brackets are HSV values.
Note that in OpenCV the range is 'compressed' to 180 instead of 360, so find the Hue value range of the color you would like to track, halve it and replace the first numbers in the square brackets (the first values in the arrays). In this case replace 0 and 5.

Depenencies
=================================

1. Xcode Command Line Tools
2. Python -> 2.7+ Not 3
3. Homebrew
4. OpenCV -> 2.4.9
5. PIP (Optional, but handy)
6. Python Imaging Library (PIL) -> 1.1.7+
7. Mock -> 1.0.1+
8. Numpy -> 1.7.1+ (May be installed with OpenCV)
9. ffmpeg
10. libardrone

Usage
=================================
```Bash
python track-red.py
```

Todo
=================================
- [x] Set up environment (Dependencies)
- [x] Proof of Concept Tracking with Computer Camera
- [x] Connect to the ARDrone
- [x] Get video from ARDrone in OpenCV Format
- [x] Find the largest Red Object
- [x] Track the Red Ball
- [x] Land if low on battery
- [x] Land action with keybinding Q
- [ ] Use PID (Proportional Integral Differentiation) to make adjustments smooth
- [ ] Make a take off action and a land action with key bindings T for takeoff and L for land

Disclaimer
=================================

IN NO EVENT SHALL JORDAN LEWIS BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING DAMAGE OF ANY SORT TO THE DRONE OR SURROUNDINGS OR INJURY, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF JORDAN LEWIS HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

JORDAN LEWIS SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE AND ACCOMPANYING DOCUMENTATION, IF ANY, PROVIDED HEREUNDER IS PROVIDED "AS IS". REGENTS HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.

YOU ARE RESPONSIBLE FOR YOUR ACTIONS AND YOUR DRONE. BE CAREFUL!

License
=================================
This OpenSource project is licensed under the Creative Commons-Attribution-ShareAlike 3.0 License.
Below is the human readable version of the license:

You are free to:
Share — copy and redistribute the material in any medium or format
Adapt — remix, transform, and build upon the material
for any purpose, even commercially.
The licensor cannot revoke these freedoms as long as you follow the license terms.
Under the following terms:

Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Notices:
You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.
No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.

The full license is available in the license document and here: https://creativecommons.org/licenses/by-sa/3.0/au/legalcode
