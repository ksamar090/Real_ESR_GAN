import cv2
import os

def extract_frames(video_path, output_folder, frame_interval=32, duration=15):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    video_capture = cv2.VideoCapture(video_path)
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    total_frames = fps * duration
    count = 0
    extracted_frame_count = 0

    while True:
        ret, frame = video_capture.read()
        if not ret or count >= total_frames:
            break
        if count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{count:05d}.png")
            cv2.imwrite(frame_filename, frame)
            extracted_frame_count += 1
            print(f"Extracted frame {count}")
        count += 1
    video_capture.release()
    print(f"Finished extracting frames. Total frames extracted: {extracted_frame_count}")

video_path = 'E:\\Video upscalling using GAN model\\Wildtrack\\cam1.mp4'
output_folder = 'E:\\Video upscalling using GAN model\\Wildtrack\\Image_subsets\\Test_frame extraction'

extract_frames(video_path, output_folder)
