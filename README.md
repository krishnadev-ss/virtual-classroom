# CamBoard
![CamBoard](https://t4.ftcdn.net/jpg/03/54/66/41/360_F_354664160_cCx8yZX9cpOf0XDb7aLLamG18SPiuSjN.jpg)


CamBoard is a cutting-edge project designed to revolutionize classroom interaction by utilizing hand gestures for various controls. With CamBoard, you can write on the classroom board in the air with your fingers, control presentations using gestures, and manipulate external applications by controlling the mouse. It also incorporates Optical Character Recognition (OCR) for word recognition using the IAM dataset.

## Features

- **Air Writing**: Write on the classroom board in the air using your fingers.
- **Gesture Control**: Control presentations and other applications using hand gestures.
- **Mouse Control**: Manipulate external applications by controlling the mouse with gestures.
- **OCR Integration**: Recognize handwritten words using OCR with the IAM dataset.

## Technologies Used

- **Python**: The core programming language used for developing CamBoard.
- **OpenCV**: For computer vision tasks such as hand tracking and gesture recognition.
- **pdf2image**: To convert PDF pages to images for processing.
- **TensorFlow**: For machine learning tasks and OCR implementation.
- **Keras**: A high-level neural networks API for building and training models.
- **AutoPy**: For automating mouse and keyboard actions.
- **MediaPipe**: For real-time hand and finger tracking.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/krishnadev-ss/virtual-classroom.git
    cd virtual-classroom
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Use the following gestures** to control the application:
    - **Write in the air**: Use your index finger to write on the virtual board.
    - **Control presentations**: Use predefined gestures to navigate through slides.
    - **Control mouse**: Use hand gestures to move the mouse cursor and perform clicks.

## Configuration

You can configure various aspects of the application in the `config.json` file. This includes gesture sensitivity, OCR settings, and more.

## Contributing

We welcome contributions from the community! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- Thanks to the contributors of OpenCV, TensorFlow, Keras, AutoPy, and MediaPipe.
- Special thanks to the IAM dataset providers for their OCR data.

## Contact

For any inquiries, please contact [krishnadevsreekumar2002@gmail.com](mailto:krishnadevsreekumar2002@gmail.com).

---

We hope you find CamBoard useful and look forward to your contributions!
