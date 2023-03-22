from .asone import ASOne
import asone.detectors
import asone.trackers
import asone.recognizers


BYTETRACK = 0
DEEPSORT = 1
NORFAIR = 2
MOTPY = 3


YOLOV5X6_PYTORCH = 0
YOLOV5S_PYTORCH = 2
YOLOV5N_PYTORCH = 4
YOLOV5M_PYTORCH = 6
YOLOV5L_PYTORCH = 8
YOLOV5X_PYTORCH = 10
YOLOV5N6_PYTORCH = 12
YOLOV5S6_PYTORCH = 14
YOLOV5M6_PYTORCH = 16
YOLOV5L6_PYTORCH = 18


YOLOV6N_PYTORCH = 20
YOLOV6T_PYTORCH = 22
YOLOV6S_PYTORCH = 24
YOLOV6M_PYTORCH = 26
YOLOV6L_PYTORCH = 28 
YOLOV6L_RELU_PYTORCH = 30
YOLOV6S_REPOPT_PYTORCH = 32

YOLOV7_TINY_PYTORCH = 34
YOLOV7_PYTORCH = 36
YOLOV7_X_PYTORCH = 38
YOLOV7_W6_PYTORCH = 40
YOLOV7_E6_PYTORCH = 42
YOLOV7_D6_PYTORCH = 44
YOLOV7_E6E_PYTORCH = 46

YOLOR_CSP_X_PYTORCH = 48
YOLOR_CSP_X_STAR_PYTORCH = 50 
YOLOR_CSP_STAR_PYTORCH = 52
YOLOR_CSP_PYTORCH = 54
YOLOR_P6_PYTORCH = 56




YOLOX_L_PYTORCH = 58
YOLOX_NANO_PYTORCH = 60 
YOLOX_TINY_PYTORCH = 62
YOLOX_DARKNET_PYTORCH = 64 
YOLOX_S_PYTORCH = 66
YOLOX_M_PYTORCH = 68
YOLOX_X_PYTORCH = 70

#ONNX

YOLOV5X6_ONNX = 1
YOLOV5S_ONNX = 3
YOLOV5N_ONNX = 5
YOLOV5M_ONNX = 7
YOLOV5L_ONNX = 9
YOLOV5X_ONNX = 11
YOLOV5N6_ONNX = 13
YOLOV5S6_ONNX = 15
YOLOV5M6_ONNX = 17
YOLOV5L6_ONNX = 19


YOLOV6N_ONNX = 21
YOLOV6T_ONNX = 23
YOLOV6S_ONNX = 25
YOLOV6M_ONNX = 27
YOLOV6L_ONNX = 29 
YOLOV6L_RELU_ONNX = 31
YOLOV6S_REPOPT_ONNX = 33

YOLOV7_TINY_ONNX = 35
YOLOV7_ONNX = 37
YOLOV7_X_ONNX = 39
YOLOV7_W6_ONNX = 41
YOLOV7_E6_ONNX = 43
YOLOV7_D6_ONNX = 45
YOLOV7_E6E_ONNX = 47

YOLOR_CSP_X_ONNX = 49
YOLOR_CSP_X_STAR_ONNX = 51
YOLOR_CSP_STAR_ONNX = 53
YOLOR_CSP_ONNX = 55
YOLOR_P6_ONNX = 57


YOLOX_L_ONNX = 59
YOLOX_NANO_ONNX = 61 
YOLOX_TINY_ONNX = 63
YOLOX_DARKNET_ONNX = 65 
YOLOX_S_ONNX = 67
YOLOX_M_ONNX = 69
YOLOX_X_ONNX = 71

# YOLOv8
YOLOV8N_PYTORCH = 72
YOLOV8N_ONNX = 73
YOLOV8S_PYTORCH = 74
YOLOV8S_ONNX = 75
YOLOV8M_PYTORCH = 76
YOLOV8M_ONNX = 77
YOLOV8L_PYTORCH = 78
YOLOV8L_ONNX = 79
YOLOV8X_PYTORCH = 80
YOLOV8X_ONNX = 81

# coreml

YOLOV5N_MLMODEL = 120



# Text Detectors
# easyocr
CRAFT = 82
DBNET18 = 83

# Text Recognizers
EASYOCR = 200



__all__ = ['ASOne', 'detectors', 'trackers', 'recognizers'] 
