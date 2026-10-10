# Lumiere Video Checker

This project demonstrates the ability to perform multimodal (Video/Image) evaluation using computer vision techniques. It is designed to detect common artifacts in AI-generated media.

## What this proves
1. **Computer Vision Proficiency:** Using OpenCV and NumPy to analyze pixel-level data.
2. **Quality Metric Design:** Implementing specific checks for:
   - **Flicker Detection:** Identifying sudden global lighting changes via histogram analysis.
   - **Temporal Consistency:** Detecting "ghosting" or disappearing objects using contour differences between frames.
   - **Sharpness/Blur:** Measuring image quality using Laplacian variance.
3. **Automated Reporting:** Generating structured consistency reports that can be used to score AI models.

## Components
- `checker.py`: Main video analysis script.
- `image_checker.py`: Script for static image prompt adherence and artifact checks.
- `test_checker.py`: Mock test suite to verify the detection logic.
"# Lumiere-video-checker" 
