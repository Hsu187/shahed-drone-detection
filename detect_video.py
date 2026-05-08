from ultralytics import YOLO
import cv2
import time

# Load model
model = YOLO('best.pt')

# Video in same folder
video_path = 'test.mp4'

# Output
output_path = 'output_with_fps.mp4'

# Process video
cap = cv2.VideoCapture(video_path)
fps_input = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps_input, (width, height))

print("Processing test.mp4...")
frame_count = 0
total_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    start = time.time()
    results = model(frame, verbose=False)
    total_time += time.time() - start
    frame_count += 1
    
    annotated = results[0].plot()
    fps = frame_count / total_time
    cv2.putText(annotated, f'FPS: {fps:.1f}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    out.write(annotated)

cap.release()
out.release()

print(f"\n✅ Output: output_with_fps.mp4")
print(f"✅ Frames: {frame_count}")
print(f"✅ FPS: {total_time/frame_count:.1f}")
