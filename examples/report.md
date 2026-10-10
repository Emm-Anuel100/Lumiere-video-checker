# Video Quality Report: Sample Analysis

## Model: Lumiere-v1-Mock
**Overall Score: 78/100**

### 1. Temporal Consistency
- **Flicker Score:** 0.92 (Good)
- **Observations:** No major global lighting shifts. Background remains stable.

### 2. Object Permanence
- **Alerts:** Minor object "warping" detected between frames 45-60. 
- **Details:** The subject's left hand loses definition during fast motion (a common Diffusion model artifact).

### 3. Sharpness
- **Blur Score:** 145.2
- **Verdict:** Pass. The video maintains high detail in the foreground.

## Recommendations
The model struggles with high-velocity motion. Increasing the training weight on optical flow consistency or using a temporal attention mask might improve the results.
