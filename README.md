# Mythos
A procedural mythology generator written in Python made for world builders.  


## How Mythos works
This is a brief overview of the system.

1.) Generate the world and society based on input files given. This is done by randomly selecting elements to stich together a world and society that inhabits the region.

Myth Generation Cycle
* Myths are created every seasonal period. There are 4 seasonal period for each year. The system will run based for however amount of years given. 
* Seasonal Periods are: Spring, Summer, Fall, Winter

1.) Enter Seasonal period, and update world stats. This includes changing animal avaibilty, climate harshness(i.e breeding season, harsh winter)

2.) Based on the Society's predisposition to certain behaviors, current resources, etc. Queue up a list of actions for the society to take this period(i.e go hunting, perform sacrifice, create art). There is also a delta variable that can slightly modify a societies willingness to take an action. This allows the society to "evolve" rather then repeat the same actions each season. 

3.) Calculate the likelyhood of each actions succeeded. Certain actions such as hunting require agents to navigate the world graph which further impacts the success or failure rate. Based on the outcome it will modify the society's prediposition towards actions. (i.e A society that has several successful hunts will hunt more often)

4.) Go back to Step 1 until the final year is reached. 


# Instructions

During the Rework Mythos cannot be ran

