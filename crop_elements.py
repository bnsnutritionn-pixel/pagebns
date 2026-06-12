from PIL import Image

img_path = "original-screenshot.png"
img = Image.open(img_path)
width, height = img.size

# Let's inspect the pixels to find the coral block (avoiding the canister on the left by starting at x = 350)
left_coral = width
top_coral = height
right_coral = 0
bottom_coral = 0

for x in range(350, width):
    for y in range(height):
        r, g, b, *a = img.getpixel((x, y))
        # Coral check (high R, moderate G and B)
        if r > 200 and g < 170 and b < 170:
            if x < left_coral: left_coral = x
            if y < top_coral: top_coral = y
            if x > right_coral: right_coral = x
            if y > bottom_coral: bottom_coral = y

print(f"Detected Coral Bounding Box: left={left_coral}, top={top_coral}, right={right_coral}, bottom={bottom_coral}")

# Let's crop the coral block
if right_coral > left_coral and bottom_coral > top_coral:
    # Give a tiny margin of 2px
    coral_crop = img.crop((left_coral - 2, top_coral - 2, right_coral + 2, bottom_coral + 2))
    coral_crop.save("drink-banner.png")
    print("Saved drink-banner.png")

# Now let's crop the canister
# Let's make sure the canister is cropped nicely.
# We'll crop from x=100 to x=235, y=70 to y=205
canister_crop = img.crop((95, 75, 235, 205))
# Create a white background padding or keep as is
canister_crop.save("canister-product.png")
print("Saved canister-product.png")
