# Galaxy-Zoo-Catalog
Galaxy Zoo is a Bayesian Deep Learning Model designed for classifying galaxies. It provides extensive and detailed morphology catalogs to facilitate research across various types of galaxies. This model employs Bayesian Convolutional Neural Networks (CNNs) for morphology classification, as detailed in [this paper](https://arxiv.org/abs/1905.07424). It utilizes a novel generative model derived from volunteer responses collected on [Galaxy Zoo](https://www.zooniverse.org/projects/zookeeper/galaxy-zoo/about/results) at Zooniverse.org to infer posterior probabilities for the visual morphology of galaxies.

Hosted on [Streamlit](https://writing-affiliate-sheet-royal.trycloudflare.com/)

## Dataset
The dataset comprises approximately 300,000 images of galaxies labeled by their shapes. Labels have been crowdsourced from volunteers on www.galaxyzoo.org and might contain noise. The images are sourced from the DECaLS telescope survey. Additionally, the dataset includes predictions from an ensemble of EfficientNets, each utilizing Monte Carlo Dropout and a unique probabilistic loss function.
