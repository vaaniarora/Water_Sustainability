ACM FAccT CFP: https://facctconference.org/2027/cfp.html

Working title: The Environmental Trade-offs of AI Datacenter Cooling

Abstract: 
The increasing power demands of AI computing systems have prompted changes in datacenter cooling and heat rejection, potentially shifting environmental pressures across energy, water use, coolant composition and material use, and geographic regions. Yet, prevailing datacenter sustainability metrics, including Power Usage Effectiveness (PUE) and Water Usage Effectiveness (WUE), capture only selected dimensions of datacenter environmental impacts and cannot, on their own, establish whether changes in cooling techniques reduce these impacts or shift them elsewhere. This creates challenges for environmental assessment and public reporting, particularly when these metrics inform infrastructure investment, procurement, and policy decisions. In this work we analyze the datacenter "cooling wall", which  describes the practical limits of existing cooling systems under the rising power density and thermal loads in datacenters, and we examine how resulting changes in cooling infrastructure introduce different environmental impact challenges. We argue that datacenter environmental reporting should complement efficiency metrics with information on absolute energy and water use, cooling and heat rejection methods, and the chemical composition and life-cycle impacts of coolants, including those containing per- and polyfluoro alkyl substances (PFAS), also known as forever chemicals. Reporting should also account for local electricity supplies and water availability, which shape the environmental consequences of resource use. Public disclosure of these dimensions would enable theus to quantify how to design of more environmentally sustainable datacenters and strengthen the basis for environmental assessment and policy decisions.



Section I: Introduction

AI is physical infrastructure
AI is often discussed through models, algorithms, tokens, and computation, but computation produces heat that must continuously be removed. AI energy use is not the only important aspect. 
It is: compute-->electrical power-->heat-->physical cooling infrastructure.

Compute density is changing
Processor power requirements increase --> server power requirements increase --> rack power requirements increase
increasing device and rack power densities create increasingly demanding thermal-management requirements.

Cooling architecture change 
air --> (liquid) rear-door heat exchanger --> direct-to-chip liquid  --> immersion liquid 
As thermal density increases, the infrastructure used to remove heat can change qualitatively rather than merely scale quantitatively.

Cooling Wall 
The transition point at which a cooling architecture can no longer practically accommodate increasing thermal density is a cooling wall. 
It is dependent on rack density, chip/package power, allowable temperatures, airflow/coolant conditions, facility design, climate, reliability requirements, economics.

Crossing the Cooling wall 
Crossing a cooling wall does not simply increase cooling efficiency or reduce resource consumption. It changes the infrastructure through which heat is removed and therefore changes the environmental impacts associated with computation.
air cooling --> liquid cooling : This transition can change electricity requirements, water requirements, coolant chemistry, materials, infrastructure, maintenance, geographic dependencies, reliability risks.
Changes in cooling technologies and facility infrastructure can alter environmental impacts across energy use, water consumption, coolant chemistry, material requirements, and geographic locations.
Cite: https://www.nature.com/articles/s41586-025-08832-3

Existing metrics 
PUE, WUE, CUE, energy per computation, carbon intensity 
These metrics are useful but each defines a particular measurement boundary.
Efficiency metrics such as Power Usage Effectiveness (PUE) and Water Usage Effectiveness (WUE) capture important dimensions of data-center performance but do not, by themselves, characterize all environmental impacts associated with different cooling configurations.
For instance, WUE tells us water intensity but not necessarily where water is consumed, whether the location is water-stressed, what cooling architecture caused it, what materials/chemicals were introduced to reduce water, what impacts were shifted elsewhere.
Cite: https://pubs.acs.org/doi/10.1021/acs.est.6c08380

What does an environmental metric make visible, and what does it make invisible? 
cooling transitions provide a useful lens for identifying which environmental impacts are measured, which may be overlooked by common efficiency metrics, and which may already be covered by broader reporting requirements.
Cite: https://doi.org/10.1145/3593013.3594014

Contributions: 
Characterize the progression from processor power to server power to rack power and its relationship to cooling requirements.
characterizeintroduce the cooling wall as a lens for understanding cooling transitions as socio-technical infrastructure transitions.
these transitions create environmental impact shifts that are not fully represented by conventional efficiency metrics, and propose a contextual reporting framework.
Assess how existing sustainability metrics and reporting requirements capture these impacts.
Identify specific environmental information that could improve data-center reporting where existing requirements leave meaningful gaps.


Section 2: From Growing Compute Demand to the Cooling Wall : Why does the cooling wall emerge?

2.1 Increasing Power Demands Across the Computing Stack
Distinguish processor and accelerator power, server power, rack power, and total facility power.
the relationship between computing power, heat generation, and thermal-management requirements. why these measures matter for cooling design?

2.2 How Datacenters are Cooled
the path from heat generated by computing equipment to heat rejection into the surrounding environment.
the operating principles and infrastructure requirements of:
Air cooling.
Rear-door heat exchangers.
Direct-to-chip liquid cooling.
Immersion cooling.
Identify supporting equipment, including fans, pumps, chillers, cooling towers, dry coolers, heat exchangers, and coolant distribution systems.
Distinguish the IT-side cooling loop from facility-side heat rejection.
why a closed liquid loop at the server level does not necessarily mean that the overall facility consumes no water.
Clarify that cooling configurations can overlap, be combined, and vary within the same facility.

2.3 Defining the Cooling Wall
Introduce the cooling wall as a proposed analytical concept, rather than an established engineering threshold.
Define it as the practical limits of an existing cooling configuration under particular technical, operational, reliability, and facility constraints.
Discuss relevant conditions:
Processor and rack power.
Heat flux and operating temperatures.
Airflow and coolant operating conditions.
Heat-exchange and facility heat-rejection capacity.
Reliability, maintenance, and cost.


From Cooling Constraints to Infrastructure Changes
Explain why increasing thermal demands may lead operators to modify cooling equipment, coolant systems, heat-rejection infrastructure, or facility design.
Distinguish changes in how heat is transferred away from computing equipment from changes in how that heat is ultimately rejected.
Identify the associated changes in equipment, fluids, materials, maintenance, and operating requirements.
Establish the connection between infrastructure changes and potential environmental impacts 


Section 3: Cooling Systems and their Environmental Impacts : What changes when we cross the cooling wall?

3.1 Energy Use
What are energy-consuming components:
Fans and air-moving equipment.
Pumps and coolant distribution systems.
Chillers and refrigeration equipment.
Cooling towers, dry coolers, and other heat-rejection systems.
cooling configuration, facility design, climate, and operating conditions influence energy use.
Distinguish cooling-system energy from total facility energy.
what PUE measures and what it cannot establish about absolute energy consumption or overall environmental impacts.
the role of local electricity generation and grid emissions.


3.2 Water 
Identify how water use varies with heat-rejection methods, including evaporative cooling, cooling towers, and dry cooling.
Difference between water used or circulated within a cooling loop and water withdrawn from external sources.
Distinguish water withdrawal from water consumption, including losses through evaporation.
what WUE captures and what it does not reveal about local environmental consequences.
Absolute water withdrawal and consumption.
Water source, including potable, reclaimed, or other supplies where applicable.
Local water availability and water stress.
Seasonal and temporal variation in water demand.
Indirect water use associated with electricity generation.
why similar WUE values may have different implications in different locations.

3.3 Coolant Chemistry, PFAS, and Chemical Management
What different types of fluids are used in cooling systems and distinguish them by composition and function.
why coolant composition is an environmental reporting concern, rather than treating all liquid coolants as environmentally equivalent.
Examine the relevance of PFAS in particular cooling applications:
Identify whether PFAS-containing substances are used in the coolant or associated cooling equipment.
Explain the relevance of persistence, potential environmental release, toxicity, and regulatory status.
Discuss how 3M stopped making PFAS coolants but now other companies have started making them for AI Cooling, and how the trajectory of AI Cooling indicates that we are not too far from using these cooling technologies
the possible impacts in the coolant lifecycle:
Initial coolant filling and quantities used.
Leakage, spills, and accidental releases.
Coolant replacement and maintenance.
Recovery, recycling, treatment, and disposal.
Distinguish documented environmental impacts from potential hazards or impacts that remain insufficiently characterized.
a transition in cooling technology may change the types and quantities of chemicals used, the likelihood of release, and end-of-life management requirements.

3.4 Materials, Equipment, and Life-Cycle Impacts
Identify the equipment and material requirements associated with different cooling configurations:
Cold plates, tubing, seals, and coolant distribution units.
Pumps, heat exchangers, and cooling towers.
Immersion tanks and associated system components.
Additional facility infrastructure required for heat rejection.
Examine relevant material production, manufacturing, replacement, maintenance, and end-of-life impacts.
show whether changes in cooling configurations affect equipment lifetimes, replacement requirements, or waste streams.


3.5 Geographic Distribution of Environmental Impacts
the same cooling configuration can produce different environmental consequences depending on where it operates.
Local climate and ambient temperatures.
Electricity supply and associated emissions.
Local water availability and competing water demands.
Proximity to and dependence on particular water sources.
Locations where coolant production, equipment manufacturing, and waste treatment occur.
a reduction in one facility-level impact may coexist with impacts elsewhere in the supply chain or electricity system.


What does this mean?
different cooling configurations affect energy, water, chemical use, material requirements, and the location of impacts.
Identify documented cases where reducing one impact is associated with an increase in, or redistribution of, another.
no cooling configuration can be assumed to have the lowest overall environmental impact in every setting.
what information is needed to assess these impacts consistently, beyond the efficiency of cooling or facility operations?


Section 4: Metrics for Measuring Environmental Impact

4.1 What Existing Sustainability Metrics Measure 
Explain what each metric measures, its system boundary, and its limitations:
Power Usage Effectiveness (PUE).
Water Usage Effectiveness (WUE).
Carbon Usage Effectiveness (CUE).
Absolute IT energy and total facility energy.
Relevant computing capacity or utilization measures.
Which metrics are reported by the datacenter operators vs which are reported by the regulatory authorities and at what granularity? 


4.2 What Existing Metrics Do Not Capture?
why PUE and WUE alone cannot establish:
Which coolants and associated chemicals are used.
Whether PFAS-containing substances are present in a particular application.
How coolant leakage, replacement, recovery, and disposal are managed.
Which materials and equipment are required and what their life-cycle impacts are.
How local water conditions and electricity supply affect environmental consequences.
Issue is the limits of particular metrics for assessing environmental trade-offs, not as proof that these impacts are universally unreported.
Explain why the environmental significance of resource use depends on:
Electricity generation and grid emissions.
Water source and local water stress.
The distinction between on-site and upstream impacts.
The time period and system boundary used in measurement.


4.3 What Existing Data-Center Reporting Requirements Already Cover
Examine relevant EU data-center sustainability reporting requirements, including the information collected on energy, water, cooling conditions, and other facility characteristics. 
Cite: https://energy.ec.europa.eu/topics/energy-efficiency/energy-efficiency-targets-directive-and-rules/energy-efficiency-directive/energy-performance-data-centres_en?prefLang=en
Distinguish information submitted to public authorities from information made publicly available and the level of aggregation used in public disclosure.
Examine relevant US federal, state, and local requirements, including applicable environmental permits, water-related requirements, and any data-center-specific disclosure rules.
Compare existing requirements against the environmental dimensions identified in Section 3. Assess which metrics are:
Already collected and publicly available.
Collected but available only to authorities or facility operators.
Reported using definitions that limit comparison.
Not required or not consistently available.
Identify specific gaps 
absence of PFAS in datacenter metrics doesn’t mean other regulation doesn’t exist for PFAS, but how can it be applied to datacenters is the question.

4.4 Recommendations for Specific Environmental Information for Data-Center Reporting
proposed reporting dimensions needed to understand the impacts identified in Section 3.

Energy 
Absolute IT energy consumption and total facility energy consumption.
PUE, with a clearly specified measurement boundary and reporting period.
Cooling and heat-rejection configuration, including relevant air- and liquid-cooling technologies.
Energy consumed by cooling and heat-rejection equipment, where it can be measured reliably.
Electricity supply characteristics relevant to emissions assessment like percentage of renewable vs non-renewable sources.
Water use
Absolute water withdrawals and consumption, reported separately.
Water source and relevant categories of water quality or supply.
WUE, with its definition and system boundary.
Local water-stress or availability information relevant to interpreting facility water use.
Relevant seasonal variation, where it materially affects local impacts.
Distinction between direct facility water use and estimated indirect water use associated with electricity generation.
Coolant composition and chemical impacts
Coolant type, chemical identity, and composition to the extent relevant and reliably reportable.
Whether PFAS-containing substances are used, where applicable.
More specific chemical identification or quantity information where necessary to assess environmental risk and permitted disclosure allows it.
Coolant quantities used, replenished, or replaced.
Reported leakage or release incidents, where applicable.
Coolant recovery, recycling, treatment, and disposal practices.
Relevant chemical hazards, regulatory classifications, and environmental impacts supported by available evidence.
Cooling equipment and material requirements
Major cooling and heat-rejection equipment categories.
Relevant material inputs where they can be identified and measured meaningfully.
Equipment replacement, maintenance, and end-of-life management
Clear distinctions between measured facility data and estimates based on product-level or industry-average data.
Geography
Facility location at an appropriate reporting resolution.
Electricity supply and emissions assumptions used in environmental calculations.
Water-source and local water-stress context.
Reporting period, units, definitions, and system boundaries.
Whether values are measured, calculated, estimated, or modeled.
Data uncertainty, missing information, and relevant limitations.

4.5 How More Complete Reporting Could Support Decisions?
comparable information could help operators and researchers assess environmental trade-offs to enable better datacenter design.
public authorities could use the information in relevant permitting, environmental assessment, and oversight processes.
public disclosure could help researchers and affected communities examine local environmental implications.
Distinguish reporting and transparency from substantive environmental regulation: disclosure can make impacts more visible but does not itself ensure that impacts are reduced.
Identify where additional standards, thresholds, or other interventions would require further evidence and policy analysis.


Discussion

Cooling Efficiency and the Growth of AI Computing
Discuss the relationship between improvements in cooling efficiency and changes in total computing demand.
Explain why improvements in PUE or WUE should not automatically be interpreted as reductions in overall environmental impacts.
Discuss rebound effects only where the paper has evidence supporting them.
Real-life examples of where these metrics have failed to capture the environmental impacts of a datacenter

Environmental Reporting as a Basis for Datacenter design Decisions
the selection of metrics and reporting boundaries affects which environmental impacts can be compared.
Discuss cooling transitions as a case that reveals the limits of existing metrics
the role and limits of reporting in supporting better-informed decisions.
Real-life examples of where environmental reporting has helped with better datacenter design, potentially some example after the EU regulation 

The Distribution of Environmental Impacts
Discuss how energy, water, chemical, and material impacts may occur in different locations.
Explain why local context matters when interpreting facility-level metrics.
Connect the reporting problem to environmental justice and sociotechnical accountability.
Cite real-life evidence that a particular community is disproportionately impacted.

Limitations and Future Research
The cooling wall is not a universal engineering threshold.
Cooling configurations, facility designs, and operating conditions vary considerably.
PFAS-related concerns must be assessed in relation to particular substances, applications, and pathways of exposure or release.
The regulatory comparison may not cover every jurisdiction or reporting regime.
Future research could examine standardized coolant reporting, comparable life-cycle assessments, facility-level disclosure, and whether additional reporting changes infrastructure decisions.


Conclusion 
