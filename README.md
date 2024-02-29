# Spotify-Packet-Analysis
> Analysis of Digital Audio Streaming Data

### Objective:
> Can we classify Spotify packets?

The high-level methodology of our research project encompasses the systematic collection of network data from the Spotify application. We will subsequently extract important features, apply classification models, and assess results based on precision and recall metrics.

### Tasks:
> What mechanisms are we using
- Collect network data using `tcpdump`
- Feature engineering/extraction
- Apply ML models to dataset

### Evaluation:
> How are we evaluating the ML models?
- Compare Precision/Recall and RMSE

### Deliverables:
> Generated outputs
- bash script (that performs data collection)
- Raw dataset (.pcap)
- Clean dataset
- ML model
- Final report

### File Structure
    .
    ├── script                  # .py and .sh 
    ├── data                    # .pcap and .csv
    └── README.md