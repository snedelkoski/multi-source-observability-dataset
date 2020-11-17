# Multi-Source Distributed System Data for AI-powered Analytics
This repository contains the simple scripts for data statistics, and link to the multi-source distributed system dataset.

You may find details of this dataset from the original paper: 

*Sasho Nedelkoski, Jasmin Bogatinovski, Ajay Kumar Mandapati, Soeren Becker, Jorge Cardoso, Odej Kao, "Multi-Source Distributed System Data for AI-powered Analytics".*

<code>
@inproceedings{nedelkoski2020multi,
  title={Multi-source Distributed System Data for AI-Powered Analytics},
  author={Nedelkoski, Sasho and Bogatinovski, Jasmin and Mandapati, Ajay Kumar and Becker, Soeren and Cardoso, Jorge and Kao, Odej},
  booktitle={European Conference on Service-Oriented and Cloud Computing},
  pages={161--176},
  year={2020},
  organization={Springer}
}
  </code>

<b>If you use the data, implementation, or any details of the paper, please cite!</b>

Abstract:

In recent years there has been an increased interest in Artificial Intelligence for IT Operations (AIOps). This field utilizes monitoring data from IT systems, big data platforms, and machine learning to automate various operations and maintenance (O&M) tasks for distributed systems.
The major contributions have been materialized in the form of novel algorithms.
Typically, researchers took the challenge of exploring one specific type of observability data sources, such as application logs, metrics, and distributed traces, to create new algorithms.
Nonetheless, due to the low signal-to-noise ratio of monitoring data, there is a consensus that only the analysis of multi-source monitoring data will enable the development of useful algorithms that have better performance.  
Unfortunately, existing datasets usually contain only a single source of data, often logs or metrics. This limits the possibilities for greater advances in AIOps research.
Thus, we generated high-quality multi-source data composed of distributed traces, application logs, and metrics from a complex distributed system. This paper provides detailed descriptions of the experiment, statistics of the data, and identifies how such data can be analyzed to support O&M tasks such as anomaly detection, root cause analysis, and remediation.

General Information:

This repository contains the simple scripts for data statistics, and link to the multi-source distributed system dataset.

The multi-source/multimodal dataset is composed of distributed traces, application logs, and metrics produced from running a complex distributed system (Openstack). In addition, we also provide the workload and fault scripts together with the Rally report which can serve as ground truth (all at the Zenodo link below). We provide two datasets, which differ on how the workload is executed. The sequential_data is generated via executing workload of sequential user requests. The concurrent_data is generated via executing workload of concurrent user requests.

Important: The logs and the metrics are synchronized with respect time and they are both recorded on CEST (central european standard time). The traces are on UTC (Coordinated Universal Time -2 hours). They should be synchronized if the user develops multimodal methods. Please read the IMPORTANT_experiment_start_end.txt file before working with the data.

If you are interested in these data, please request the data via <a href="url">Zenodo</a>. Kindly note that the affiliation, and information about the utilization of the dataset. If you do not receive any response from Zenodo within one week, please check your spam mailbox or consider to resubmit your data request with the required information.
