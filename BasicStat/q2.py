"""
-- Standard Deviation --
Standard deviation is a measure of the amount of variation or dispersion in a set of values. In statistics, it provides a way to quantify the extent to which individual data points in a dataset differ from the mean (average) of the dataset.

In simpler terms, the standard deviation tells you how much the values in a dataset typically deviate from the mean. A low standard deviation indicates that the values are close to the mean, while a high standard deviation indicates that the values are spread out over a wider range.

-- Population Mean --
The population mean, often denoted by the Greek letter μ (mu), is a measure of central tendency that represents the average or expected value of a variable in an entire population. It is calculated by summing up all the values in the population and then dividing by the total number of values.


-- Confidence Interval --
A confidence interval is a statistical concept that provides a range of values which is likely to contain the true value of an unknown parameter, along with a level of confidence. It is a way to quantify the uncertainty or margin of error associated with a point estimate from a sample.


a) What is the mean in this scenario?
-- The mean in this scenario is 22.5. The mean is the average of a set of values. In this case, the mean is the average age of students in the sample.

b) What is the 99% confidence interval for the population mean age of students in the university based on the sample information provided?
-- The 99% confidence interval for the population mean age of students in the university based on the sample information provided is (21.8, 23.2). The 99% confidence interval for the population mean age of students in the university is calculated as follows:

1. Calculate the margin of error. The margin of error is calculated as follows:
	margin of error = t * (sample standard deviation / square root of sample size)
	where t is the t-statistic for the given confidence level and degrees of freedom.
	
	In this case, the t-statistic for the given confidence level and degrees of freedom is 2.680. 
	
	The margin of error is calculated as follows:
	margin of error = 2.680 * (2.5 / square root of 50)
					= 0.7. 2.
	
	Calculate the confidence interval. The confidence interval is calculated as follows:
	confidence interval = (sample mean - margin of error), (sample mean + margin of error)
						= (22.5 - 0.7), (22.5 + 0.7)
						= (21.8, 23.2).

c) What insights or conclusions can you draw about the population mean age of students in the university based on the sample information provided.
-- With 99% confidence, we estimate that the population mean age of students in the university lies within the calculated interval. In other words, we are 99% confident that the population mean age of students in the university lies within the calculated interval.

d) what is the interval?
-- The interval is (21.8, 23.2). The interval is a range of values which is likely to contain the true value of an unknown parameter, along with a level of confidence. In this case, the interval is a range of values which is likely to contain the population mean age of students in the university, along with a level of confidence.
"""

import numpy as np
from scipy.stats import t

# Given data
sample_mean = 22.5
sample_std_dev = 2.5
sample_size = 50
confidence_level = 0.99

# Margin of error calculation
margin_of_error = t.ppf((1 + confidence_level) / 2,
                        sample_size - 1) * (sample_std_dev / np.sqrt(sample_size))

# Confidence interval calculation
confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)

# Results
print(f'Mean age of students in the sample: {sample_mean}')
print(
    f'99% Confidence Interval for the population mean age: {confidence_interval}')

# Conclusion
# With 99% confidence, we estimate that the population mean age of students in the university lies within the calculated interval.
