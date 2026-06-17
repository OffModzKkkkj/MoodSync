
import numpy as np
import pandas as pd
import random

def simulate_typing_data(num_samples=1000, emotions=["focused", "stressed", "relaxed", "excited"]):
    data = []
    for _ in range(num_samples):
        emotion = random.choice(emotions)
        
        # Simulate WPM (Words Per Minute)
        if emotion == "focused":
            wpm = random.gauss(60, 10) # Higher WPM, less variance
        elif emotion == "stressed":
            wpm = random.gauss(45, 15) # Lower WPM, more variance
        elif emotion == "relaxed":
            wpm = random.gauss(55, 8)  # Moderate WPM, low variance
        elif emotion == "excited":
            wpm = random.gauss(70, 12) # Higher WPM, moderate variance
        wpm = max(10, wpm) # Ensure WPM is not too low

        # Simulate Key Press Duration (ms)
        if emotion == "focused":
            key_duration = random.gauss(80, 10) # Shorter duration, less variance
        elif emotion == "stressed":
            key_duration = random.gauss(120, 30) # Longer duration, more variance
        elif emotion == "relaxed":
            key_duration = random.gauss(90, 15)  # Moderate duration, moderate variance
        elif emotion == "excited":
            key_duration = random.gauss(75, 12) # Shorter duration, moderate variance
        key_duration = max(30, key_duration) # Ensure duration is not too low

        # Simulate Pause Duration (ms) between words
        if emotion == "focused":
            pause_duration = random.gauss(200, 50) # Shorter pauses, less variance
        elif emotion == "stressed":
            pause_duration = random.gauss(400, 150) # Longer pauses, more variance
        elif emotion == "relaxed":
            pause_duration = random.gauss(250, 70)  # Moderate pauses, moderate variance
        elif emotion == "excited":
            pause_duration = random.gauss(180, 40) # Shorter pauses, less variance
        pause_duration = max(50, pause_duration) # Ensure pause is not too low

        # Simulate Error Rate (errors per 100 words)
        if emotion == "focused":
            error_rate = random.gauss(1, 0.5) # Low error rate
        elif emotion == "stressed":
            error_rate = random.gauss(5, 2) # High error rate
        elif emotion == "relaxed":
            error_rate = random.gauss(2, 1) # Moderate error rate
        elif emotion == "excited":
            error_rate = random.gauss(1.5, 0.8) # Low error rate
        error_rate = max(0, error_rate)

        data.append({
            "wpm": wpm,
            "key_duration": key_duration,
            "pause_duration": pause_duration,
            "error_rate": error_rate,
            "emotion": emotion
        })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = simulate_typing_data(num_samples=2000)
    df.to_csv("typing_data.csv", index=False)
    print("Simulated typing_data.csv created with 2000 samples.")
    print(df.head())
