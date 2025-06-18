import pickle
import os
import pandas as pd
import numpy as np
from scipy.stats import f

# Define the variable names
variable_names = ["Speed Cars", "Speed Trucks", "Number of Cars", "Number of Trucks", "Flow Cars", "Flow Trucks"]

variable_names_francia = ["Speed Cars", "Number of Cars", "Flow Cars"]
# Define the mapping from variable names to their indices
variable_name_to_index = {
    "Speed Cars": 0,
    "Speed Trucks": 1,
    "Number of Cars": 2,
    "Number of Trucks": 3,
    "Flow Cars": 4,
    "Flow Trucks": 5
}

index_segments_k = {
    "Elicoidale Downstream": 0,
    "Lungomare Canepa": 1,
    "Elicoidale Upstream": 2,
    "Via di Francia": 3
}

segment_variable_count = {
    "Elicoidale Downstream": 6,
    "Lungomare Canepa": 6,
    "Elicoidale Upstream": 6,
    "Via di Francia": 3
}

def create_multimodal_dataset(dataset1, dataset2, ratio=0.7, total_runs=None, seed=42):
    # Set random seed
    np.random.seed(seed)

    if total_runs is None:
        total_runs = dataset1.shape[1]

    # Calculate number of runs to sample from each dataset
    num_dataset1_runs = int(total_runs * ratio) # 1200*0.7
    num_dataset2_runs = total_runs - num_dataset1_runs

    # Ensure the datasets are compatible
    if dataset1.shape[0] != dataset2.shape[0]:
        raise ValueError("Both datasets must have the same first dimension!")

    # Randomly sample from each dataset
    dataset1_sample = dataset1[:, np.random.choice(dataset1.shape[1], size=num_dataset1_runs, replace=False)]
    dataset2_sample = dataset2[:, np.random.choice(dataset2.shape[1], size=num_dataset2_runs, replace=False)]

    # Combine datasets along the 'runs' dimension (axis=1)
    multimodal_dataset = np.concatenate((dataset1_sample, dataset2_sample), axis=1)

    # Shuffle the runs to randomize their order
    shuffled_indices = np.random.permutation(multimodal_dataset.shape[1])
    multimodal_dataset = multimodal_dataset[:, shuffled_indices]

    return multimodal_dataset


def get_segment_data(data, segment_key):
    """
    Extracts data related to a single segment from the reaggregated data.

    Args:
        data (np.ndarray): The reaggregated data array.
        segment_key (str): The key of the segment in index_segments_k.

    Returns:
        np.ndarray: Data for the specified segment, or None if the segment key is invalid.
    """
    if segment_key not in index_segments_k:
        print(f"Error: Segment key '{segment_key}' not found in index_segments_k.")
        return None

    segment_index = index_segments_k[segment_key]
    num_variables = segment_variable_count[segment_key]
    start_index = segment_index * len(variable_names) #Use len(variable_names) as the initial number of variables per segment.
    end_index = start_index + num_variables -1

    return data[start_index : end_index+1, :]
