import os, sys
from PIL import Image



def resize_image(img_path):
	if not os.path.isfile(img_path):
		print(f"Input file NOT found: \"{img_path}\"")
		return

	print(f"Input file found: \"{img_path}\"")

	filename = img_path.split(".")[0]
	extension = img_path.split(".")[-1]

	img = Image.open(img_path)

	sizes = [16, 32, 48, 64, 128, 256, 512]
	for idx, size in enumerate(sizes):
		print(f"\t[{idx+1}/{len(sizes)}] Size {size}x{size}:")
		output_filename = f"{filename}_{size}x{size}.png"

		resized_image = img.resize((size, size), Image.Resampling.LANCZOS)
		resized_image.save(output_filename)
		print(f"\t\tsaved: \"{output_filename}\"")
		# break


def main():
	if len(sys.argv) < 2:
		print(f"Too few args!")
		print(f"\tpython resize.py logo-path.png")
		return

	for img_path in sys.argv[1:]:
		resize_image(img_path)

if __name__ == '__main__':
	main()
