import cv2
import pafy

# Set pafy to use yt-dlp backend
pafy.set_backend("yt-dlp")
print(f"Using backend: {pafy.backend}")  # This should print 'yt-dlp'

url = "https://www.youtube.com/watch?v=t0Q2otsqC4I"
data = pafy.new(url)
best = data.getbest(preftype="mp4")

clip = cv2.VideoCapture(best.url)
print(clip)

while True:
    ret, frame = clip.read()

    if ret:
        frame = cv2.resize(frame, (820, 450))
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

clip.release()
cv2.destroyAllWindows()
