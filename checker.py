import cv2
import numpy as np
from typing import Dict, List, Any

class VideoConsistencyChecker:
    """
    Analyzes a video for temporal artifacts common in generative AI.
    """

    def __init__(self, video_path: str):
        self.video_path = video_path
        self.results = {
            "flicker_score": 0.0,
            "motion_stability": 0.0,
            "blur_score": 0.0,
            "alerts": []
        }

    def analyze(self) -> Dict[str, Any]:
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            return {"error": "Could not open video"}

        prev_frame = None
        prev_hist = None
        flicker_deltas = []
        blur_values = []
        motion_diffs = []

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # 1. Check for Blur (Laplacian Variance)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur_map = cv2.Laplacian(gray, cv2.CV_64F).var()
            blur_values.append(blur_map)

            # 2. Check for Global Flicker (Histogram Correlation)
            hist = cv2.calcHist([frame], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
            cv2.normalize(hist, hist)
            
            if prev_hist is not None:
                # 1.0 is perfect match, lower is flicker
                corr = cv2.compareHist(prev_hist, hist, cv2.HISTCMP_CORREL)
                flicker_deltas.append(corr)

            # 3. Check for Object Disappearance (Frame Diff)
            if prev_frame is not None:
                diff = cv2.absdiff(gray, prev_frame)
                _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
                motion_score = np.sum(thresh) / thresh.size
                motion_diffs.append(motion_score)

            prev_frame = gray
            prev_hist = hist

        cap.release()

        # Aggregate Results
        if flicker_deltas:
            self.results["flicker_score"] = float(np.mean(flicker_deltas))
            if min(flicker_deltas) < 0.8:
                self.results["alerts"].append("High flicker detected in some frames.")

        if blur_values:
            self.results["blur_score"] = float(np.mean(blur_values))

        return self.results

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        checker = VideoConsistencyChecker(sys.argv[1])
        print(checker.analyze())
    else:
        print("Please provide a video path.")
