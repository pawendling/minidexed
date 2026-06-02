#!/bin/bash

# ==========================================
# Launch 8 Dexed Instances on macOS
# Auto rename windows Bus1..Bus8
# ==========================================

APP="Dexed"

for i in {1..4}
do
    open -n -a "$APP"
    sleep 1
done

exit

# Give time for windows to appear
sleep 3

osascript <<EOF
tell application "System Events"

    tell process "Dexed"

        set frontmost to true
        delay 1

        set winList to every window

        repeat with i from 1 to count of winList
            set w to item i of winList

            try
                perform action "AXRaise" of w
            end try

            delay 0.2

            keystroke "l" using {command down}
            delay 0.2

            keystroke "Bus" & i
            delay 0.2

            key code 36
            delay 0.2

        end repeat

    end tell

end tell
EOF
