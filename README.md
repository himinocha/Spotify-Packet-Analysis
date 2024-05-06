# Spotify-Packet-Analysis
> Analysis of Digital Audio Streaming Data

> Final Report: https://docs.google.com/document/d/14NxwLCIXSc70cwK8Ixc9oYui0Q0etwYuHvfFpOe2gqk/edit?usp=sharing

### Objective:
> Can we classify Spotify packets?

The high-level methodology of our research project encompasses the systematic collection of network data from the Spotify application and Web Browser. We will subsequently extract important features, apply classification models, and evaluate based on precision and recall as metrics.

### Data:
> .pcap and .csv
- .pcap files will be processed using python (`pcapkit`)
- raw data (direct features):
    - headers of protocols
    - source and destination IP
    - payload data of the packets
- processed data (derivative features):
    - inter-arrival time between packets
    - average packet inter-arrival time per destination (Spotify server)

### Tasks:
> What mechanisms are we using
- Collect network data using `tcpdump` and `scapy`
- Feature engineering/extraction
- Apply ML models to dataset

### Evaluation:
> How are we evaluating the ML models?
- Compare Precision/Recall and RMSE
- Confusion Matrix

| Actual Class      | Classified as non-Spotify | Classified as Spotify |
|-------------------|---------------------------|-----------------------|
| non-Spotify data  | True Negative             | False Positive        |
| Spotify data      | False Negative            | True Positive         |


### Deliverables:
> Generated outputs
- bash/py script (that performs automated data collection)
- Raw dataset (.pcap)
- Clean dataset
- ML model (Decision Tree, Random Forest, XGBoost)
- Final report

### File Structure
    .
    ├── script                  # .py and .sh to collect packets
    ├── data                    # .pcap and .csv
    ├── notebook                # .ipynb for feature engineering, visualization and modeling
    ├── visualization           # .png or .pdf (saved visualizations)
    ├── .env                    # to save API keys
    ├── .gitignore
    ├── requirements.txt
    ├── environment.yml
    └── README.md