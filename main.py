# Cursor Control With Hand Gestures 
import cv2
import mediapipe as mp
import pyautogui
import time
import math
from util import get_angle, get_distance

# initialize mediapipe hands
mp_hands = mp.solutions.hands  # hand detection
mp_drawing = mp.solutions.drawing_utils  # drawing utilities
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)  # camera open

# gesture time control
click_start_time = None
click_times = []
click_cooldown = 0.5
scroll_mode = False
freeze_cursor = False
screenshot_cooldown = 2
last_screenshot_time = 0

screen_w, screen_h = pyautogui.size()
print("\n Smart Hand")
prev_screen_x, prev_screen_y = 0, 0  # cursor speed ke liye


if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()  # read frame by frame
    if not ret:
        print("Error: Could not read frame.")
        break

    frame = cv2.flip(frame, 1)  # flip the frame horizontally

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # get finger tip
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[
                mp_hands.HandLandmark.MIDDLE_FINGER_TIP
            ]
            ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

            fingers = [
                (
                    1
                    if hand_landmarks.landmark[tip].y
                    < hand_landmarks.landmark[tip - 2].y
                    else 0
                )
                for tip in [8, 12, 16, 20]
            ]
            # distance between thumb and index
            dist = math.hypot(thumb_tip.x - index_tip.x, thumb_tip.y - index_tip.y)
            if dist < 0.06:
                if not freeze_cursor:
                    freeze_cursor = True
                    click_times.append(time.time())

                    # double click check
                    if (
                        len(click_times) >= 2
                        and click_times[-1] - click_times[-2] < 0.4
                    ):
                        pyautogui.doubleClick()
                        cv2.putText(
                            frame,
                            "Double Click",
                            (100, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 0),
                            2,
                        )
                        click_times = []
                    else:
                        pyautogui.click()
                        cv2.putText(
                            frame,
                            "Single Click",
                            (100, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 0),
                            2,
                        )
                else:
                    if freeze_cursor:
                        time.sleep(0.1)
                    freeze_cursor = False

            # move cursor by index_finger
            if not freeze_cursor:
                screen_x = int(index_tip.x * screen_w)
                screen_y = int(index_tip.y * screen_h)
                pyautogui.moveTo(screen_x, screen_y, duration=0.05)
                # smooth cursor movement because the duration is set to 0.05
                prev_screen_x, prev_screen_y = screen_x, screen_y

            # scroll  mode
            if (
                sum(fingers) == 4
            ):  # this line of code means that the number of total fingers to be detected is 4
                scroll_mode = True
            else:
                scroll_mode = False

            # scroll actions
            if scroll_mode:
                if index_tip.y < 0.4:
                    pyautogui.scroll(60)
                    cv2.putText(
                        frame,
                        "Scrolling Up",
                        (100, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2,
                    )
                elif index_tip.y > 0.6:
                    pyautogui.scroll(-60)
                    cv2.putText(
                        frame,
                        "Scrolling Down",
                        (100, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 255),
                        2,
                    )  # putText is used to display the text on webcam

            # screenshot actions
            if sum(fingers) == 0:
                current_time = time.time()
                if current_time - last_screenshot_time > screenshot_cooldown:
                    pyautogui.screenshot(f"screenshot_{int(current_time)}.png")
                    cv2.putText(
                        frame,
                        "Screenshot Taken",
                        (10, 130),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 255, 0),
                        2,
                    )
                    last_screenshot_time = current_time

    cv2.imshow("Video0", frame)  # display the frame

    if cv2.waitKey(1) == ord("q"):  # press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
