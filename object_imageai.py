{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from imageai.Detection import VideoObjectDetection\n",
    "import os\n",
    "\n",
    "execution_path = os.getcwd()\n",
    "\n",
    "detector = VideoObjectDetection()\n",
    "detector.setModelTypeAsYOLOv3()\n",
    "detector.setModelPath( os.path.join(execution_path , \"yolo.h5\"))\n",
    "detector.loadModel()\n",
    "\n",
    "video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join( execution_path, \"traffic-mini.mp4\"),\n",
    "                                output_file_path=os.path.join(execution_path, \"traffic_mini_detected_1\")\n",
    "                                , frames_per_second=29, log_progress=True)\n",
    "print(video_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
