import cv2
import os

# Create a directory to save frames if it doesn't exist
os.makedirs("./assets/frames", exist_ok=True)

# Note, the VideoCapture method generates a pointer that points to the current frame being read and keeps track of the previos one to update to the next frame correctly
clip = cv2.VideoCapture("./assets/wild_butterfly_in_nature_6891914.mp4")
fps = clip.get(cv2.CAP_PROP_FPS)  # Frames per second
count = 0

while True:
    ret, frame = clip.read()
    if not ret:
        print("Reached the end of the video or can't fetch the frame.")
        break

    # Resize the frame
    frame = cv2.resize(frame, (700, 400))
    
    # Save the current frame as an image
    cv2.imwrite(f"./assets/frames/img{count}.jpg", frame)
    
    # Display the frame
    cv2.imshow("res", frame)
    
    # Move to the next frame after a certain interval (1 second here)
    count += 1
    clip.set(cv2.CAP_PROP_POS_MSEC, (count * 100))  # Change 100 to control interval

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

clip.release()
cv2.destroyAllWindows()
