# Multi-source Dataset of IT Observability Data forAIOps Research
This repository contains the implementation details, code, and the multi-source distributed system dataset.

You may find details of this dataset from the original paper: 

*Sasho Nedelkoski, Ajay Kumar Mandapati, Jasmin Bogatinovski, Soeren Becker, Jorge Cardoso, Odej Kao, "A Multi-source Dataset of IT Observability Data for AIOps Research".*

<b>If you use the data, implementation, or any details of the paper, please cite!</b>

The multi-source/multimodal dataset is composed of distributed traces, application logs, and metrics produced from running a complex distributed system (Openstack). In addition, we also provide the workload and fault scripts together with the Rally report which can serve as ground truth (all at the Zenodo link below). We provide two datasets, which differ on how the workload is executed. The <b>*multimodal sequential-workload data*</b> is generated via executing workload of sequential user requests. The <b>*multimodal concurrent-workload data*</b> is generated via executing workload of concurrent user requests. 

The difference of the *<b>concurrent</b>* dataset is that:
1. Due to the heavy load on the control node, the metric data for wally113 (control node) is not representative and we excluded it.
2. Three rally actions are executed in parallel: boot_and_delete, create_and_delete_networks, create_and_delete_image, whereas for the *<b>sequential</b>* there were 5 actions executed. 

The raw logs in both datasets contain the same files. If the user wants the logs filetered by time with respect to the two datasets, should refer to the timestamps at the metrics (they provide the time window). <b>In addition, we suggest to use the provided aggregated time ranged logs for both datasets in CSV format.

If you are interested in these data, please request the data via <a href="url">Zenodo</a>. Kindly note that the affiliation, and information about the utilization of the dataset. If you do not receive any response from Zenodo within one week, please check your spam mailbox or consider to resubmit your data request with the required information.
