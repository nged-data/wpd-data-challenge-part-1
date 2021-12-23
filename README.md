# WPD Data Challenge (Part 1) 
This challenge is now CLOSED but the data and competition information are detailed here for information.

## Background
This was the first of three Western Power Distribution (WPD) short data challenges. It ran in Nov/Dec 2021. The aims of these challenges include:
- Demonstrating the value in making data openly available
- Increasing the visibility of some of the challenges network operators face
- Increase the understanding of the different ways to tackle some of these problems
- Providing high quality and accurate benchmarks with which to enable innovation and research

## The Goal: High Resolution Peak Estimation
This initial challenge aims to understand how accurately high resolution features can be estimated given only information from lower resolution data. Specifically we asked participants to estimate the highest peak value and lowest trough at a one minute resolution within each half hourly period given only half hourly measurements. This is an interesting problem to a distribution network operator as the spikes in demand can mean strain on their network. Such issues may become increasingly common, especially on the lower voltages of the network, due to the expanding use of lower carbon technologies such as electric vehicles, and heat pumps. However, monitoring can be expensive (especially in the long term) as it requires investment in additional storage, communications equipment and processing units.

## Challenge Details
The challenge was hosted on Codalab, with full details (including more details on the data) available [here](https://codalab.lisn.upsaclay.fr/competitions/213)

The original briefing call for the start of the challenge can be found [here](https://www.youtube.com/watch?v=RJK3KJmOyRM) and the LinkedIn group for this and future challenges is [here](https://www.linkedin.com/groups/9025332/)

### Data
The data is available on the [WPD Data Portal](https://connecteddata.westernpower.co.uk/dataset/western-power-distribution-data-challenge-1-high-resolution-peak-estimation). Note that this includes the final scoring data used in the competition (MW_Staplegrove_CB905_MW_target_variable_half_hourly_max_min_real_power_MW_september.csv).

The license terms for usage of the substation data can be found [here](https://www.westernpower.co.uk/open-data-licence) and weather data [here](https://disc.gsfc.nasa.gov/information/documents?title=data-policy)

### Results and Solutions
The competition had over 70 participants, with most working as part of teams. The final stage was scored based on a skill score of RMSE compared to the simple benchmark (using 30 minute average for both max and min)

| Place | Team/User                          | Skill Score | Code Links |
| ----- | ---------------------------------- | ----------- | ---------- |
| 1     | LFCE - Load Forecasting Crew Essen | 0.426       |            |
| 2     | WOJJ                               | 0.436       |            |
| 3     | code_green                         | 0.437       |            |
| 4     | Random Forresters                  | 0.443       |            |
| 5     | ghd-not-the-hair-straightener      | 0.459       |            |
| 6     | u_cvml                             | 0.460       |            |
| 7     | The Bad Bois                       | 0.466       |            |
| 8     | ESDA Dream Team                    | 0.480       |            |
| 9     | ecureuil                           | 0.486       |            |
| 10    | The Resistance                     | 0.511       |            |
| 11    | matthias                           | 0.520       |            |
| 12    | nzlads                             | 0.537       |            |
| 13    | szymon_p                           | 0.544       |            |
| 14    | Bathteam                           | 0.765       |            |
| N/A   | BENCHMARK                          | 1.000       |            |
| 15    | xyz                                | 1.972       |            |
| 16    | ucaTeam                            | 2.169       |            |

### Evaluation
If you want to give this challenge a go and see how you compare then you can find the scoring code in this repository as evaluate.py.

If you come up with a good solution please share with the community by forking the repo, adding the link to this readme and creating a pull request.
