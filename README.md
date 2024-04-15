# Field Segmentation

## Goals

- Design a tool for land and crop classification
- Terrain type detection
- Compare different segmentation pipelines
- Test the model on satellite resolution images
- Train on a provided dataset
- Develop a tool for sentinel data analysis
- Do single image classification
- Do temporal classification
- Real time? We will need to categorize on real data from sentinel hub.
- Crop coverage and detection
- Pytorch (with or without Keras)
- Use Openmmlab segmentation

## Possible datasets

### Recommended

- [DeepGlobe Land Cover Classification Dataset](https://www.kaggle.com/datasets/balraj98/deepglobe-land-cover-classification-dataset)
- [🌾 PASTIS 🌾 Panoptic Agricultural Satellite TIme Series](https://github.com/VSainteuf/pastis-benchmark)
- [Landcover AI](https://landcover.ai.linuxpolska.com/)
- [Agriculture-Vision](https://github.com/SHI-Labs/Agriculture-Vision?tab=readme-ov-file#dataset)
- [Sen4AgriNet](https://github.com/Orion-AI-Lab/S4A)
- [Landslide4Sense: Multi-sensor landslide detection competition & benchmark dataset](https://github.com/iarai/Landslide4Sense-2022)
- [AgriFieldNet India Challenge](https://zindi.africa/competitions/agrifieldnet-india-challenge)

### Additional

- [A large-scale climate-aware satellite image dataset for domain adaptive land-cover semantic segmentation](https://github.com/Linwei-Chen/CASID)
- [Forest Aerial Images for Segmentation](https://www.kaggle.com/datasets/quadeer15sh/augmented-forest-segmentation/data)
- [Semantic segmentation of aerial imagery](https://www.kaggle.com/datasets/humansintheloop/semantic-segmentation-of-aerial-imagery/data)
- [GeoNRW](https://www.kaggle.com/datasets/javidtheimmortal/geonrw)
- [Plant disease dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)

### Real time data
- [Dataspace Copernicus](https://dataspace.copernicus.eu/explore-data)
	- [Sentinel hub - Processing API](https://dataspace.copernicus.eu/analyse/apis/sentinel-hub) - Apparently the api to get images. Needs an access token. 
	- [Copernicus - Documentation](https://documentation.dataspace.copernicus.eu/Home.html)

## References

- [Openmmlab](https://github.com/open-mmlab)
- [Openmmlab Segmentation](https://github.com/open-mmlab/mmsegmentation)
- [Pytorch amp](https://pytorch.org/docs/stable/amp.html)
