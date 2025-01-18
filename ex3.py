import cv2 as cv

# Lae pilt samast kaustast
image_path = "testpic.jpg"
image = cv.imread(image_path)

if image is None:
    print("Pildi laadimine ebaõnnestus. Veendu, et pilt asub õiges kaustas ja nimega '3.png'.")
    exit()

while True:
    print("\nValikud:")
    print("1: Threshold")
    print("2: Blur")
    print("3: Dilate")
    print("4: Erode")
    print("5: Canny")
    print("0: Välju")

    choice = input("Sisesta oma valik: ")

    if choice == "0":
        print("Programm lõpetab töö.")
        break

    if choice == "1":
        value = int(input("Sisesta threshold väärtus (0-255): "))
        _, processed_image = cv.threshold(image, value, 255, cv.THRESH_BINARY)
    elif choice == "2":
        value = int(input("Sisesta blur väärtus (paaritu arv, nt 3, 5, 7): "))
        if value % 2 == 0:
            value += 1
            print(f"Paarisarv korrigeeriti: {value}")
        processed_image = cv.GaussianBlur(image, (value, value), 0)
    elif choice == "3":
        value = int(input("Sisesta dilate kernel suurus (nt 3, 5, 7): "))
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (value, value))
        processed_image = cv.dilate(image, kernel, iterations=1)
    elif choice == "4":
        value = int(input("Sisesta erode kernel suurus (nt 3, 5, 7): "))
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (value, value))
        processed_image = cv.erode(image, kernel, iterations=1)
    elif choice == "5":
        value1 = int(input("Sisesta Canny alumine väärtus: "))
        value2 = int(input("Sisesta Canny ülemine väärtus: "))
        processed_image = cv.Canny(image, value1, value2)
    else:
        print("Vigane valik. Palun proovi uuesti.")
        continue

    # Näita töödeldud pilti
    cv.imshow("Töödeldud pilt", processed_image)
    cv.waitKey(0)
    cv.destroyAllWindows()