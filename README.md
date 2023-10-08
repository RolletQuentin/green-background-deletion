# Green Background Deletion

This is a little project to delete all green screen on a photo and replace it with an other image.

## Installation

You can create a virtual environment :
```
python3 -m venv .venv
source .venv/bin/activate
```

Then you can install the requirements :
```
pip install -r requirements.txt
```

## Configuration

- Open `main.py` file;
- Change `FOLDER_DIR` value with the route of your images directory
- Change `BACKGROUND_IMAGE_ROUTE` value with the route of the background picture
- You can also change `MINIMUM_ANGLE_COLOR`, `MAXIMUM_ANGLE_COLOR`, `MINIMUM_SATURATION`, `MAXIMUM_SATURATION` and `MINIMUM_BRIGHTNESS`. You can go on this [simulation](https://web.cs.uni-paderborn.de/cgvb/colormaster/web/color-systems/hsv.html) to see which value you can take. My script use HSV representation, an alternative for RGB representations [Wikipédia](https://en.wikipedia.org/wiki/HSL_and_HSV).

## Execution

To run the script :
```
python3 main.py
```

## Results

With these parameters, you can see some bugs, especially for dark green or white. I don't have a high quality dataset to find the best values for parameters, maybe I can find it later with a better dataset.

References :
- [CodinGame](https://www.codingame.com/playgrounds/53303/apprendre-python-dans-le-secondaire/manipulations-dimages-i)
- [Universität Paderborn](https://web.cs.uni-paderborn.de/cgvb/colormaster/web/color-systems/hsv.html)
- [StackLima](https://stacklima.com/comment-parcourir-les-images-d-un-dossier-python/)