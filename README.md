**ArUco Distance Calculator**

This Python project uses OpenCV to estimate the distance to an object in real-time using a camera and an ArUco marker.

**How to Use**

1. Make sure you have OpenCV (`cv2`), NumPy (`np`), and pickle libraries installed. You can install them using `pip installopencv-python numpy pickle`.
2. Place an ArUco marker (of the specified dictionary type) in front of the camera.
3. Run the script: `python main.py`
4. The program will display the video stream with the detected marker and the estimated distance to the object displayed on the frame.
5. You can collect distance and area data points for calibration by pressing the 'f' key. This data will be saved to a file named `mapa.pickle`.

**Requirements**

* Python 3.x
* OpenCV (`cv2`)
* NumPy (`np`)
* pickle

**Optional**

* A camera

**Code Structure**

* `main.py`: The main script containing the program logic.
* `README.md` (This file): Contains instructions on how to use the project.

**Notes**

* The formula used to estimate the real-world distance might need adjustments based on your specific camera setup and marker size. You can modify the formula in the `main.py` script.
* This project is provided as-is for educational purposes.

**Contributing**

Feel free to submit pull requests if you have improvements or modifications for this code.
