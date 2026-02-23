# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 13:17:46 2026

@author: Josep
"""

        
        
class Robot:
    def __init__(self, ID, status:bool = True, location: str = "A1"):
        self.ID = ID
        self.status = bool(status)
        self.location = str(location).upper()

    def move_bot(self, new_location: str) -> None:
        """Change the robot's location (e.g., 'B7')."""
        self.location = str(new_location).upper()

    def change_stat(self) -> None:
        """Toggle online/offline."""
        self.status = not self.status

    def __str__(self) -> str:
        state = "online" if self.status else "offline"
        return f"Robot(ID={self.ID}, status={state}, location={self.location})"

    def __repr__(self) -> str:
        return str(self)


# --- Short verification script ---
if __name__ == "__main__":
    r1 = Robot(ID=1, status=True, location="A3")
    print(r1)  # expect online @ A3

    r1.move_bot("C5")
    print("After move:", r1)  # expect @ C5

    r1.change_stat()
    print("After toggle:", r1)  # expect offline

    r2 = Robot(ID="X-17", status=False, location="b2")
    print("Second robot:", r2)  # expect location B2, offline
