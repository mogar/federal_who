
# Who wrote the Federalist Papers

Sharon Bertsch McGrayne's book on Bayesian history, The Theory That Would Not Die, has an entire chapter on how Bayesian data analysis was used to analyze The Federalist Papers. There are 85 of these papers, each written by one of three authors during the formation of the United States as a country. Most of these papers have a known author, but for 11 of the papers we aren't sure who exactly wrote it. Figuring out who wrote those papers (Hamilton or Madison) was apparently one of the first major achievements of academic Bayesian reasoning after WWII.

After reading in "Unix: a history and a memoir" that one of Kernighan's colleagues at Bell Labs was also interested in the Federalist Papers, I figured I'd get in on the act.

This repo is my experimentation on figuring out who wrote those questionable Federalist Papers. I'm not a data analyst by training, so I'm primarily using this as an excuse to learn more about how it's done. Back in the 60s it took a team of PhDs and students years to figure this stuff out. Here's hoping I can do better on my own by using modern tools and methods.

I'm going into this without looking up the results of prior investigations, but at the end I'll compare what I find to them.

See here for a good overview of the Federalist Papers history: https://priceonomics.com/how-statistics-solved-a-175-year-old-mystery-about/

# Pre-Reqs

* python3
* requests
* Beautiful Soup
* scipy

# Usage

git clone ...
cd federal_who
./get_fedurls.py # get all the federalist papers from the Library of Congress
./federalyze.py # perform analysis and print results


## Federalize Markov


file: papers/unknown/FederalistNo.49.txt
* AlexanderHamilton: 9.443617638347116e-111
* JamesMadison: 1.0
* JohnJay: 0.0
file: papers/unknown/FederalistNo.50.txt
* AlexanderHamilton: 1.8727134398441352e-33
* JamesMadison: 1.0
* JohnJay: 5.256240469342864e-29
file: papers/unknown/FederalistNo.51.txt
* AlexanderHamilton: 1.8955210608118475e-228
* JamesMadison: 1.0
* JohnJay: 0.0
file: papers/unknown/FederalistNo.52.txt
* AlexanderHamilton: 4.661556287831538e-40
* JamesMadison: 1.0
* JohnJay: 0.0
file: papers/unknown/FederalistNo.53.txt
* AlexanderHamilton: 7.135449665091098e-154
* JamesMadison: 1.0
* JohnJay: 7.054953147582555e-186
file: papers/unknown/FederalistNo.54.txt
* AlexanderHamilton: 0.0
* JamesMadison: 1.0
* JohnJay: 0.0
file: papers/unknown/FederalistNo.55.txt
* AlexanderHamilton: 1.0
* JamesMadison: 4.68672501230136e-41
* JohnJay: 6.88158342129063e-158
file: papers/unknown/FederalistNo.56.txt
* AlexanderHamilton: 1.0
* JamesMadison: 1.9559503215634695e-153
* JohnJay: 0.0
file: papers/unknown/FederalistNo.57.txt
* AlexanderHamilton: 1.0
* JamesMadison: 4.672316591574561e-39
* JohnJay: 4.844247997608867e-204
file: papers/unknown/FederalistNo.62.txt
* AlexanderHamilton: 6.883091011385395e-209
* JamesMadison: 1.0
* JohnJay: 2.942184949009688e-20
file: papers/unknown/FederalistNo.63.txt
* AlexanderHamilton: 4.945100607575191e-285
* JamesMadison: 1.0
* JohnJay: 3.5034436013929836e-208



# Analysis Methods and Results

Ideas:

* histogram of words, then nearest neighbor
* look up some methods