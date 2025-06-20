def estimate_distance(pixel_width, known_width=30, focal_length=600):
    if pixel_width == 0:
        return float('inf')
    return (known_width * focal_length) / pixel_width
