# Run Guide: Lumiere Video Checker

This project uses computer vision to analyze AI-generated media for artifacts.

## Setup
Install the computer vision dependencies:
```bash
pip install opencv-python numpy pytest
```

## How to Run

### Analyze a Video
```bash
python checker.py <path_to_video_file>
```

### Analyze an Image
```bash
python image_checker.py <path_to_image_file>
```

### Run Logic Tests
To verify the artifact detection algorithms using mock data:
```bash
pytest test_checker.py
```
