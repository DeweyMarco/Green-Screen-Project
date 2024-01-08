# Green Screen Image Processing Software

## Overview

This software is designed to create a composite image by applying a green screen effect. It takes a green screen image, a background image, and performs a series of operations to produce an output image where the green screen is replaced with the background.

## Features

- **Cropping**: The software automatically crops the center of the large image to match the size of the small image, providing a focused area for the green screen effect.

- **Green Screen Removal**: Green pixels in the green screen image are identified and replaced with black, while non-green pixels are replaced with white, creating a black and white mask.

- **Composition**: The black and white mask is then combined with a new image, creating a composite image where the green screen is replaced with the new content.

- **Output**: The final output image is saved in the "output/" directory with a filename based on the current date and time.

## Prerequisites

- Python 3.x
- OpenCV library

## Installation
1. Install Python 3.x: [Python Downloads](https://www.python.org/downloads/)

2. Install required libraries using pip:
   ```bash
   pip install opencv-python
   ```
## Usage
1. Run the script from the command line:
   ```bash
   python green_screen.py <green_screen_image> <background_image>
   ```
   Replace <green_screen_image> and <background_image> with the paths to your green screen image and background image, respectively.
2. The output image will be saved in the "output/" directory.

## Example
   ```bash
   python green_screen.py green_screen_examples/greenscreen.jpg background_examples/wolfberg.jpg
   ```

## Contributing

If you'd like to contribute to this project, please follow the [Contributing Guidelines](CONTRIBUTING.md).

## Bug Reports and Feature Requests

If you encounter any issues or have ideas for improvements, please open an issue on the [Issue Tracker](https://github.com/your-username/your-repository/issues).

## Directory Structure

- **cropped/**: Contains cropped images.
- **masks/**: Contains black and white masks.
- **output/**: Contains the final composite images.

## License

This software is released under the [MIT License](LICENSE).

---

**Author:** Your Name
**Contact:** your.email@example.com
**Project URL:** [GitHub Repository](https://github.com/your-username/your-repository)

