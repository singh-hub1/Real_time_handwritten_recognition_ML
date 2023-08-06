# Real_time_handwritten_recognition_ML
Worked on a Machine Learning Project where the method of Real-Time Handwriting Recognition is used by computers to identify and read the array
of characters which is written in free hand in front of a web camera.


What is OCR?
Optical character recognition is the conversion of images of typed, handwritten, or printed text into machine-encoded text, whether from a scanned document, a photo of a document, a scene photo, or subtitle text superimposed on an image.

OCR converts text in an Image to machine-readable text format.

Use cases of OCR
Capturing-invoices — Companies can quickly extract data from bills using a combination of OCR and other AI approaches.
OCR in the Banking sector — With mobile banking apps, through OCR-based check depositing tools, your checks can be deposited digitally and processed in no time.
Healthcare industry — Data from X-ray reports, patient histories, treatments or diagnostics, tests, and general hospital records can be digitized using OCR technology.
Next, we will be going over the implementation of an OCR engine that comprises of The ssd_mobilenet for ROI(Region of interest) Text detection and EasyOCR model for Text Recognition. The complete code for this post is hosted here on my Github account. Please Enjoy!

Implementation
We will start by creating and annotating our dataset. A great tool to annotate our dataset is labelImg.

The goal of this project is to use OCR to extract ‘chapter’ and ‘title’ from a textbook. This moderate project implementation will showcase the features and innovations in the frameworks and tools we are about to use.

The core software technologies used in this project are:

TFOD( Tensorflow Object Detection ) API.
OpenCV.
EasyOCR.
LabelImg

OpenCV
OpenCV is the huge open-source library for the computer vision, machine learning, and image processing and now it plays a major role in real-time operation which is very important in today’s systems. By using it, one can process images and videos to identify objects, faces, or even handwriting of a human. When it integrated with various libraries, such as NumPy, python is capable of processing the OpenCV array structure for analysis. To Identify image pattern and its various features we use vector space and perform mathematical operations on these features. 

The first OpenCV version was 1.0. OpenCV is released under a BSD license and hence it’s free for both academic and commercial use. It has C++, C, Python and Java interfaces and supports Windows, Linux, Mac OS, iOS and Android. When OpenCV was designed the main focus was real-time applications for computational efficiency. All things are written in optimized C/C++ to take advantage of multi-core processing. 








































#Screenshots



![fifth](https://github.com/singh-hub1/Real_time_handwritten_recognition_ML/assets/63784168/727b2dff-ea05-4aef-8e1b-54ac8e795df8)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





![first](https://github.com/singh-hub1/Real_time_handwritten_recognition_ML/assets/63784168/8d936f8c-6cdb-47c6-b6fd-810722f0c7bf)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






![second](https://github.com/singh-hub1/Real_time_handwritten_recognition_ML/assets/63784168/19f58bc4-7548-49a3-9baa-bc9065f80e47)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







![fourth](https://github.com/singh-hub1/Real_time_handwritten_recognition_ML/assets/63784168/e0c08504-0622-4f6e-9ba9-3b560511f532)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




![sixth](https://github.com/singh-hub1/Real_time_handwritten_recognition_ML/assets/63784168/e3967131-6a05-48ad-82e3-3c4331be048a)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





![third](https://github.com/singh-hub1/Real_time_handwritten_recognition_ML/assets/63784168/cb4adfa3-1f28-46b2-abaa-d944df96bc01)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



