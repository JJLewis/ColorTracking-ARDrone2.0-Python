RedBallTracking-ARDrone2.0-Python
=================================

Track a red ball with an ARDrone 2.0 through its camera.
Follows a fairly large red object (a ball maybe) by rotating around in the air and ascending and descending.

Depenencies
=================================

1. Python -> 2.7+ Not 3
2. Homebrew
3. OpenCV -> 2.4.9
4. PIP (Optional, but handy)
5. Python Imaging Library (PIL) -> 1.1.7+
6. Mock -> 1.0.1+
7. Numpy -> 1.7.1+ (May be installed with OpenCV)
8. ffmpeg
9. libardrone

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
