# Benchmark-for-Automatic-Glottis-Segmentation-(BAGLS)

This package contains several commands and utilities to easily use Semantic Segmentation models for automatic glottis segmentation.

## 🚀 Getting Started

To start using this package, install it using `pip`:

For example, for installing it in Ubuntu use:
```bash
pip3 install bagls
```

It is recommended to install it globally and not inside virtual environments.
Have been tested in Windows, Linux and MacOS.

## 👩‍💻 Usage
This package makes easier the use of the best trained model. For that purpose you have available 2 commands:
* `bagls image <inputImagePath> <outputFolder>` This method predict over an image. Supported types are: `.jpg`, `.png`, `.nd2`, `.tif` y `.tiff`.
* `bagls folder <inputFolder> <outputFolder>` This method predict in all the images of a folder.

You can use the abbreviation `bagls`.

In addition, you can use the GUI developed for preparing the dataset. For that purpose run: `bagls gui`. More information of the utilities in the next section.

You can also execute `bagls --help`, `bagls gui --help`, `bagls image --help`, `bagls folder --help` for a detailed help.

## 💻 GUI

This GUI contains 4 different utilities: predict, convert ".nd2" and ".tiff" 8 bits unsigned to ".png", transform ".roi" into a ".png" Mask and generating the Dataset.

<!-- ### Predict
![Predict](https://raw.githubusercontent.com/WaterKnight1998/Deep-Tumour-Spheroid/feature/python-package/python-package/readme_images/predict_tumour.png)

### Transform Image
![Transform Image](https://raw.githubusercontent.com/WaterKnight1998/Deep-Tumour-Spheroid/feature/python-package/python-package/readme_images/transform_image.png)

### Convert ROI to Mask
![Convert ROI to Mask](https://raw.githubusercontent.com/WaterKnight1998/Deep-Tumour-Spheroid/feature/python-package/python-package/readme_images/convert_roi_to_mask.png)

### Generate Dataset
![Generate Dataset](https://raw.githubusercontent.com/WaterKnight1998/Deep-Tumour-Spheroid/feature/python-package/python-package/readme_images/generate_dataset.png) -->


## 📩 Contact
📧 mahjouri.saamahn@gmail.com

💼 Linkedin [Saamahn Mahjouri](https://www.linkedin.com/in/saamahnmahjouri/)