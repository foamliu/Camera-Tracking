import cv2 as cv

if __name__ == '__main__':
    cap = cv.VideoCapture('video/movie.mp4')
    surf = cv.xfeatures2d.SURF_create()
    fourcc = cv.VideoWriter_fourcc(*'MPEG')
    out = cv.VideoWriter('video/output.avi', fourcc, 24.0, (1080, 720))

    while True:
        ret, frame = cap.read()
        if not ret: break

        kp, des = surf.detectAndCompute(frame, None)
        print(len(kp))
        img2 = cv.drawKeypoints(frame, kp, None, (255, 0, 0), flags=cv.DRAW_MATCHES_FLAGS_DEFAULT)
        cv.imshow('frame', img2)
        out.write(img2)

        ch = cv.waitKey(1)
        if ch == 27:
            break

    cv.destroyAllWindows()
    cap.release()
