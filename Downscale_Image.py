from PIL import Image
import os

def severely_reduce_image_quality(input_folder, output_folder, quality):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")

        try:
            with Image.open(input_path) as img:
                img = img.convert("RGB")
                img.save(output_path, "JPEG", quality=quality)
            print(f"Saved {output_path} with quality={quality}")
        except PermissionError:
            print(f"Permission denied: {output_path}. Try running as administrator or check directory permissions.")
        except Exception as e:
            print(f"An error occurred with {filename}: {e}")


# Example usage
input_folder = 'E:\\Video upscalling using GAN model\\Wildtrack\\Image_subsets\\C7'
output_folder = 'E:\\Video upscalling using GAN model\\cam 7 video_purpose'
severely_reduce_image_quality(input_folder, output_folder, quality=20)