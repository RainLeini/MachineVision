import cv2 as cv


def on_change(value):
    pass


# Videofail
video_path = 'coins.mp4'

# Open video file
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open the video file.")
    exit()

frame_delay = 50  # Slowdown in milliseconds

window_name = 'Kontuuride tuvastus'
cv.namedWindow(window_name)

while True:
    ret, frame = cap.read()
    if not ret:
        print("l6pp või viga")
        break

    # Step 1: hall
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Step 2: blur
    blurred = cv.GaussianBlur(gray, (15, 15), 0)

    # Step 3: ääred
    edges = cv.Canny(blurred, 50, 150)

    # Step 4: kontuurid
    contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Step 5: filtreeri ja joonista
    filtered_contours = []
    for contour in contours:
        # Filtreeri suuruse järgi
        if 5000 < cv.contourArea(contour) < 10000:  #vastavalt vajadusele sättida
            filtered_contours.append(contour)
            (x, y, w, h) = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #Tekst ja numbrid
    cv.putText(frame, "Total Contours:", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv.putText(frame, str(len(contours)), (200, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv.putText(frame, "Filtered Contours:", (10, 60), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv.putText(frame, str(len(filtered_contours)), (200, 60), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # raam
    cv.imshow(window_name, frame)

    # Exit q
    if cv.waitKey(frame_delay) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()