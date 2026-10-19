Yes — I think this is **substantially better**. In particular, I agree with your decision **not to force a quantitative processor → server → rack relationship** when the data come from different sources. That would introduce a level of inference that the dataset cannot support.

I would make only a few changes.

### 1. Keep the first part deliberately descriptive

The first part should establish an empirical fact:

> **The power associated with AI computing has increased substantially at multiple hardware scales over time.**
> 

Then show three independent trends:

1. **Processor power** — W per accelerator/CPU
2. **Server power** — W per server
3. **Rack power** — kW per rack

I would **not** say that processor power causes server power or that server power causes rack power. Instead, use the three graphs as evidence that **power density is increasing across multiple levels of the computing stack**.

One nuance: I would avoid saying simply that "AI processors/servers/racks have much larger values." The comparison should be framed as **AI-oriented/high-performance systems versus earlier/general-purpose systems**, because otherwise the reader may ask what the baseline population is.

---

### 2. The cooling-system description should come before the cooling wall

I strongly agree with your ordering:

> power trends → how cooling works → why cooling architectures eventually change
> 

That gives the reader the physical vocabulary needed to understand the cooling wall.

I would also make the loop discussion **architecture-neutral**. Rather than implying every data center literally has three discrete loops, say that cooling systems can be understood through three functional stages:

**IT-side heat transport → facility-side heat transport → heat rejection**

Depending on architecture, some stages may be integrated, separated, recirculating, or absent.

That distinction matters because otherwise someone could challenge the paper on a technicality such as "this facility only has two loops."

Similarly, treat **open vs. closed loop as a property of the particular cooling subsystem**, rather than saying a whole data center is simply open-loop or closed-loop.

---

### 3. The cooling-wall section should be careful about causality

I think your formulation is exactly the right direction:

> **Rack power density drives pressure toward a cooling transition, but does not uniquely determine it.**
> 

The cooling wall is therefore not a universal number such as "air cooling ends at 20 kW/rack."

It depends on things such as:

- rack power density
- allowable chip/junction temperatures
- air temperature and humidity
- airflow and fan capability
- server/rack geometry
- heat-transfer characteristics
- supply/return temperatures
- facility infrastructure
- reliability requirements
- acceptable energy overhead
- economic constraints

So I would explicitly distinguish:

> **cooling architecture is a design choice, but the feasible design space is physically constrained.**
> 

That is a much stronger formulation than "high-density racks require liquid cooling," because the latter is too absolute.

For the figure, therefore, I would show **overlapping feasible/transition regions**, rather than hard vertical boundaries between air, direct-to-chip, immersion, etc.

---

# Proposed structure for Section 2

I would actually give Section 2 **three subsections**, exactly corresponding to the three conceptual movements you described:

## 2. From Compute Density to the Cooling Wall

### 2.1 Increasing Power Across the Computing Stack

**Paragraph 1 — Processor power**

Introduce processor-level power and explain what is being measured. Establish that modern AI accelerators and high-performance processors have substantially higher power envelopes than earlier processors. Explain the dataset and metric carefully, especially because manufacturers use different terminology such as TDP, TGP, TDP-like power, or maximum/sustained power.

Then make the modest observation:

> Across the historical sample, processor power generally increases over time, with contemporary AI accelerators occupying the upper end of the distribution.
> 

**Figure 2a: Processor power over time.**

Don't interpret this as server power.

---

**Paragraph 2 — Server power**

Move one level up.

Explain that a server's electrical power includes much more than the processor: accelerators/CPUs, memory, motherboard, storage, networking, power conversion, fans, etc.

Then introduce your measured server-power dataset, probably SPECpower as the historical backbone, with MLPerf systems as a complementary AI-oriented dataset if appropriate.

Again, the claim is descriptive:

> Measured server power also exhibits an upward trend over time, with accelerator-rich/high-performance systems occupying substantially higher power ranges than conventional servers.
> 

**Figure 2b: Server power over time.**

Explicitly state that these measurements should **not be interpreted as a direct continuation of the processor dataset**, because the datasets differ in systems, workloads, measurement protocols, and populations.

That disclaimer is actually scientifically valuable.

---

**Paragraph 3 — Rack power**

Move to the rack.

Explain that rack power aggregates the power requirements of the servers and associated rack-level infrastructure, and that modern AI/HPC deployments can reach power levels substantially above traditional enterprise racks.

Use OCP/rack-scale designs and documented AI infrastructure examples.

Again:

> Rack-level power has likewise increased, particularly in contemporary AI-oriented infrastructure.
> 

**Figure 2c: Rack power over time / representative rack power.**

Here I would be especially careful with "over time" because your rack dataset may not be as historically continuous as processor/server data. If the data are sparse, call it **reported rack power by year/design generation**, rather than implying a continuous time series.

---

**Paragraph 4 — Synthesis without causal inference**

I think this paragraph is important.

Put the three graphs together and say something like:

> Taken together, these datasets show a consistent directional pattern: the power associated with computing has increased at the processor, server, and rack scales. Because these observations are drawn from different datasets and measurement conventions, we do not infer a quantitative mapping between the three levels. Instead, they establish the changing power-density context in which contemporary data-center cooling systems operate.
> 

This paragraph protects you methodologically and sets up the next subsection beautifully.

---

# 2.2 How Data Centers Remove Heat

I would make this a somewhat longer subsection because this is where you give readers enough engineering context to understand the later argument.

### Paragraph 1 — Why computing requires cooling

Start from a simple physical fact:

> Nearly all electrical power consumed by computing equipment ultimately becomes heat that must be removed to maintain components within their allowable operating temperatures.
> 

Introduce the relationship between IT power and heat generation without overcomplicating it.

Then explain that cooling is therefore not an optional accessory to computation; it is part of the infrastructure required to operate the computing system.

---

### Paragraph 2 — From the chip to the rack

Describe the physical heat path:

**chip → package → cold plate/heatsink → server → rack → facility → environment**

Explain that cooling can happen at different points along this path.

Air cooling primarily transports heat away from components using air and fans.

Liquid cooling places a liquid closer to the heat-generating components, allowing heat to be transported through a liquid loop.

Immersion places components directly in a dielectric fluid.

Keep this paragraph conceptual. Don't yet argue that one is better.

---

### Paragraph 3 — The IT cooling loop

Introduce the **IT-side cooling loop**.

For direct liquid cooling, for example:

> cold plate → warm coolant → heat exchanger/CDU → cooled coolant → cold plate
> 

Explain the role of the CDU/heat exchanger where relevant.

Crucially, say that this loop may be:

- open or closed,
- water-based or dielectric-fluid-based,
- directly connected to the facility system or thermally separated from it.

This is where you introduce the idea that **"liquid cooling" is not a single technology**.

---

### Paragraph 4 — The facility cooling loop

Then move outside the rack.

The IT loop transfers heat to a facility-side system, which transports that heat toward the heat-rejection infrastructure.

For example:

> IT loop → CDU/heat exchanger → facility water loop → chiller/cooling tower/dry cooler → ambient environment
> 

Explain that the facility loop can have different configurations depending on climate, facility design, cooling technology, and whether heat rejection uses mechanical refrigeration, evaporative processes, dry cooling, or other approaches.

---

### Paragraph 5 — Heat rejection

I would give heat rejection its own paragraph because it becomes important later for your water argument.

The key point:

> **The fact that a rack uses a liquid coolant does not by itself determine whether the facility consumes water.**
> 

A closed-loop liquid system can circulate coolant repeatedly while rejecting heat through a facility system that may itself use:

- evaporative cooling,
- dry cooling,
- hybrid cooling,
- chillers,
- other heat-rejection approaches.

This is an important conceptual distinction for the paper.

It also prevents the simplistic:

> liquid cooling = water consumption
> 

argument.

---

### Paragraph 6 — Open-loop and closed-loop systems

Then explicitly define the terms.

**Closed loop:** fluid is recirculated within the cooling system, with heat transferred elsewhere rather than continuously replacing the working fluid.

**Open loop:** the working fluid is introduced and discharged/replaced as part of the heat-transfer process, or interacts directly with the environment.

But I would add:

> The terms describe a particular cooling subsystem rather than necessarily the entire data center.
> 

This avoids a lot of ambiguity.

---

### Paragraph 7 — Coolants and cooling architectures

Now introduce coolant diversity.

Potential categories:

- air
- water
- water/glycol mixtures
- dielectric fluids
- fluorinated fluids in some applications

The important point is not to create a coolant catalog. Instead:

> Different cooling architectures place different demands on the physical and chemical properties of the working fluid.
> 

That sets up your later Section 3 discussion of:

**water → chemistry → materials → lifecycle → environmental burden.**

You can mention PFAS/fluorinated fluids here briefly, but **save the environmental implications for Section 3**.

---

### Paragraph 8 — Closing transition

End the subsection with the key observation:

> Cooling systems therefore differ not simply in how much heat they remove, but in where heat is transferred, which fluids and equipment are required, how those fluids circulate, and how heat is ultimately rejected to the environment.
> 

Then transition:

> These differences become increasingly consequential as the amount of heat generated within a given physical footprint increases.
> 

That gives you the doorway into the cooling wall.

---

# 2.3 The Cooling Wall

This is where I think the paper becomes conceptually interesting.

### Paragraph 1 — Introduce the problem

Start with:

> Increasing rack power does not merely increase the amount of heat that a cooling system must remove; it can change the feasibility of the cooling architecture itself.
> 

That's the central sentence.

Then explain that every cooling technology has an operating envelope.

---

### Paragraph 2 — What determines the envelope?

Discuss the physical constraints.

For air cooling, increasing rack density means more heat must be transported through the air-handling system. That creates increasing demands on:

- airflow,
- pressure drop,
- fan power,
- heat-exchanger area,
- temperature gradients,
- component thermal limits.

Eventually, simply increasing airflow is no longer an attractive or physically practical solution.

You don't need to give a universal threshold.

---

### Paragraph 3 — Why liquid cooling changes the problem

Explain why liquid cooling becomes attractive.

Liquids generally provide much greater heat-transfer capacity per unit volume than air, allowing heat to be transported away from high-power components more effectively.

The important point isn't:

> liquid is always better.
> 

It is:

> **changing the cooling medium changes the feasible thermal design space.**
> 

That is precisely what you need for the cooling-wall argument.

---

### Paragraph 4 — Define the cooling wall

Now formally define your term.

Something along these lines:

> We use **cooling wall** to describe the context-dependent boundary beyond which an incumbent cooling architecture can no longer meet the thermal, operational, reliability, or economic requirements of a computing system without a substantial change in cooling design.
> 

Then immediately clarify:

> The cooling wall is therefore not a universal rack-power threshold. Rather, it is a transition region whose location depends on the computing hardware, rack configuration, environmental conditions, facility infrastructure, and design requirements.
> 

This definition is important enough that I would probably give it a highlighted definition box or italicized sentence in the paper.

---

### Paragraph 5 — Rack density drives, but does not determine, the wall

This is the nuance you specifically want.

Something like:

> Rack power density is an important driver of this transition because it determines how much heat must be removed from a given physical space. However, it does not uniquely determine the cooling architecture. Two systems with similar rack power can have different feasible cooling configurations because of differences in component layout, allowable temperatures, ambient conditions, heat-rejection infrastructure, and operational requirements.
> 

This protects you from making the claim that:

kW/rack→specific cooling technology\text{kW/rack} \rightarrow \text{specific cooling technology}

which your data cannot establish.

Instead:

higher power density→greater cooling requirements→shrinking feasible envelope of incumbent architecture→increasing pressure for architectural transition\text{higher power density} \rightarrow \text{greater cooling requirements} \rightarrow \text{shrinking feasible envelope of incumbent architecture} \rightarrow \text{increasing pressure for architectural transition}

That's the relationship I think the paper should actually claim.

---

### Paragraph 6 — Cooling technologies as overlapping regimes

Then introduce your figure.

Rather than:

```
0 ───── 20 ───── 40 ───── 60 ───── 100 kW/rack
     AIR | LIQUID | IMMERSION
```

I'd strongly recommend something visually closer to:

```
Rack power density
──────────────────────────────────────────────>

      Air cooling
   ────────────────────────
             Enhanced air
          ───────────────────────
                    Direct liquid
                ───────────────────────────
                            Immersion
                     ────────────────────────
```

with **overlapping regions**.

The figure communicates:

> technologies have feasible operating ranges rather than single transition points.
> 

You can then explain that the boundaries represent approximate regimes or reported applications, not universal physical thresholds.

---

### Paragraph 7 — The wall is an infrastructure transition

This is the paragraph that should connect Section 2 to the rest of your paper.

Crossing the wall means more than replacing a heatsink with a cold plate.

It may change:

- pumps,
- CDUs,
- heat exchangers,
- piping,
- coolant inventories,
- facility-side temperatures,
- heat-rejection equipment,
- water requirements,
- electricity consumption,
- maintenance procedures,
- materials,
- chemical exposure.

And **this is exactly why the cooling wall matters for environmental accountability.**

You don't need to analyze those impacts here. Just establish that the architecture transition changes the infrastructure through which environmental burdens arise.

---

### Paragraph 8 — Transition into Section 3

End Section 2 with something like:

> The cooling wall therefore marks a transition not only in thermal engineering but in the infrastructure required to sustain computation. As computing moves across this boundary, environmental consequences are redistributed across energy, water, materials, coolant chemistry, and geographic infrastructure. The next section examines these consequences as a problem of environmental burden shifting.
> 

That gives you a very clean bridge into Section 3.

---

# So the final Section 2 structure would be

## **2. From Compute Density to the Cooling Wall**

### **2.1 Increasing Power Across the Computing Stack**

1. Processor power
2. Server power
3. Rack power
4. Cross-dataset synthesis / methodological caution

**Figures:**

- Processor power vs. year
- Server power vs. year
- Rack power vs. year/design generation

### **2.2 How Data Centers Remove Heat**

1. Computing → heat
2. Chip/server/rack heat path
3. IT cooling loop
4. Facility cooling loop
5. Heat rejection
6. Open vs. closed loops
7. Cooling fluids and architectures
8. Transition to cooling wall

**Figure:** schematic of IT loop → facility loop → heat rejection, with open/closed-loop variants.

### **2.3 The Cooling Wall**

1. Increasing power changes cooling requirements
2. Physical/engineering limits of incumbent cooling
3. Why liquid/other approaches expand feasible thermal design space
4. Definition of cooling wall
5. Rack density drives but does not determine transition
6. Cooling technologies as overlapping regimes
7. Architectural/infrastructure consequences
8. Transition to burden shifting

**Figure:** cooling technology vs. rack power-density regimes.

---

## One thing I would *not* do

I would **not call 2.1 "From Processor Power to Rack Power."**

That title subtly implies that you're establishing a causal/quantitative chain between the datasets.

I'd use:

> **Increasing Power Across the Computing Stack**
> 

because your actual empirical claim is:

power is increasing at multiple scales\boxed{ \text{power is increasing at multiple scales} }

not:

Pprocessor→Pserver→Prack\boxed{ P_\text{processor}\rightarrow P_\text{server}\rightarrow P_\text{rack} }

That distinction will make the paper much more defensible.

Overall, I strongly agree with your proposed structure. It also gives Section 2 a very clean narrative: **empirical observation → engineering context → conceptual transition.** Then Section 3 can begin exactly where Section 2 ends: **what environmental burdens change when that transition occurs?**

---

## 2. From Compute Density to the Cooling Wall

### 2.1 Increasing Power Across the Computing Stack

The increasing computational demands of contemporary artificial intelligence (AI) systems have been accompanied by increases in the power associated with computing hardware at multiple scales. At the processor level, recent generations of data-center CPUs, GPUs, and other accelerators operate at substantially higher power levels than earlier processors. This trend is particularly pronounced for AI accelerators, whose architectures are designed to support highly parallel workloads and increasingly large computational throughput. Figure 2a presents the power specifications of representative data-center processors and accelerators over time. Because manufacturers report power using different metrics—including thermal design power (TDP), total graphics power (TGP), maximum turbo power, and related measures—we retain the manufacturer's reported metric rather than treating these values as directly equivalent. The resulting trajectory nevertheless shows a broad increase in the power associated with individual high-performance processors and accelerators over time.

Processor-level power, however, does not represent the power consumption of a complete computing system. A server includes processors or accelerators as well as memory, storage, networking, voltage regulation and power-conversion components, cooling fans, and other supporting hardware. Figure 2b therefore considers measured server-level power using publicly reported benchmark and system measurements. These measurements likewise show an increase in the power of high-performance computing systems over time, with contemporary accelerator-rich systems occupying substantially higher power ranges than many earlier general-purpose servers. Server-level measurements are particularly useful because they capture the combined electrical demand of the computing system rather than the nominal power specification of an individual processor. At the same time, these measurements depend on the workload, configuration, measurement protocol, and system architecture and should therefore not be interpreted as a universal maximum power for a given server model.

At the rack level, multiple servers are aggregated into a common physical and electrical infrastructure. The resulting rack power can therefore reach levels substantially above those associated with individual servers. Recent AI-oriented and high-performance computing deployments report rack power densities that are considerably higher than those historically associated with conventional enterprise computing infrastructure. Figure 2c presents representative reported rack-level power values across system generations and rack designs. Unlike the processor and server datasets, rack-level data are more heterogeneous and are often reported as design specifications or deployment characteristics rather than standardized benchmark measurements. We therefore use these observations to characterize the range of rack power associated with contemporary computing infrastructure rather than to construct a continuous historical series.

Taken together, the three datasets show a consistent directional pattern: the power associated with computing has increased at the processor, server, and rack scales. We do not infer a quantitative mapping between these levels because the observations are drawn from different sources, populations, measurement conventions, and system configurations. In particular, processor power specifications cannot be summed to obtain measured server power, and server-level measurements cannot be directly interpreted as measurements of rack-level power. Instead, the three views establish the changing power-density context in which data-center cooling systems must operate. As more electrical power is concentrated into processors, servers, and racks, increasingly large quantities of heat must be transported away from computing equipment within the physical and operational constraints of the data center.

### 2.2 How Data Centers Remove Heat

Electrical power consumed by computing equipment is ultimately converted largely into heat. Maintaining processors, memory, power electronics, and other components within their allowable operating temperatures therefore requires a continuous mechanism for transporting this heat away from the computing equipment. Cooling is consequently not an auxiliary function added to computation after the fact; it is part of the physical infrastructure that enables computing systems to operate. The design of that infrastructure determines how heat is transported from the component generating it, through the server and facility, and ultimately to the surrounding environment.

At the component level, heat can be transferred from a processor or accelerator through a thermal interface and into a heat sink, cold plate, or other heat-transfer structure. In conventional air-cooled systems, fans drive air through the server and across heat-transfer surfaces, carrying heat away from the components. In liquid-cooled systems, a liquid is brought closer to the heat source and transports heat away from the component through a circulating fluid. Direct-to-chip cooling, for example, places a cold plate in thermal contact with selected high-power components, while immersion cooling places computing components in direct contact with a dielectric fluid. These approaches differ substantially in their physical implementation, but they perform the same basic function: transporting heat away from the computing hardware.

For liquid-cooled systems, it is useful to distinguish an **IT-side cooling loop** from the infrastructure that ultimately rejects heat from the facility. In a direct-to-chip configuration, coolant may circulate through cold plates attached to processors or accelerators, absorb heat, and return at a higher temperature. The warmed coolant can then pass through a coolant distribution unit (CDU) or heat exchanger, where heat is transferred to another cooling system before the coolant returns to the computing equipment. The IT-side loop may therefore be physically separated from the facility cooling system while remaining thermally coupled to it. This separation allows the fluid properties, pressure, flow rate, and operating conditions of the equipment-side cooling system to be managed independently from those of the facility.

A facility-side cooling loop transports heat away from the IT equipment toward a heat-rejection system. Depending on the facility architecture, heat may pass from the IT loop through a CDU or heat exchanger into a facility water loop, and from there to chillers, cooling towers, dry coolers, heat exchangers, or other heat-rejection equipment. The facility system may also be configured differently depending on the climate, desired operating temperatures, available infrastructure, and cooling technology. Thus, there is no single physical configuration that defines a "data-center cooling loop." Rather, cooling systems can contain multiple thermally coupled loops with different functions and operating conditions.

The final stage is **heat rejection**, through which heat is transferred from the facility to the surrounding environment. This distinction is important because the cooling technology used at the rack does not by itself determine how much water a facility consumes. A rack can use a closed-loop liquid cooling system in which the IT-side coolant is continuously recirculated, while the facility ultimately rejects heat through an evaporative cooling tower. Conversely, a liquid-cooled system may reject heat through a dry cooler or other air-based mechanism with little or no direct evaporative water consumption. Water use is therefore determined by the combination of the IT cooling architecture, facility-side cooling system, and heat-rejection technology rather than simply by whether a rack is described as "liquid cooled."

The terms **open loop** and **closed loop** describe another important distinction in cooling-system design. In a closed-loop system, the working fluid is recirculated within the cooling system and heat is transferred to another medium or ultimately to the environment without continuously replacing the primary working fluid. In an open-loop configuration, the working fluid is introduced, discharged, or otherwise exchanged with the surrounding environment as part of the cooling process. These terms can apply to particular subsystems rather than to an entire data center. A facility can therefore contain a closed IT-side loop together with a different facility-side or heat-rejection system that has different flow and replenishment characteristics.

Cooling systems also differ in the fluids used to transport heat. Depending on the architecture and application, these fluids can include air, water, water-based mixtures such as water and glycol, and dielectric fluids used in immersion or other specialized systems. Some advanced cooling architectures may also use fluorinated fluids or other specialized chemical formulations. The choice of coolant is constrained by requirements including heat-transfer performance, electrical properties, operating temperature, material compatibility, pressure, safety, maintenance, and system lifetime. Consequently, changing the cooling architecture can also change the materials and chemical substances incorporated into the computing infrastructure. These differences become environmentally relevant because the impacts associated with a cooling system extend beyond the energy required to operate pumps and fans to include water consumption, material production, chemical manufacture and handling, leakage, maintenance, and end-of-life management.

The resulting cooling infrastructure can therefore be understood as a sequence of thermally coupled functions: heat is generated within the computing equipment, transported through an IT-side cooling system, transferred to facility infrastructure where applicable, and ultimately rejected to the environment. Different cooling technologies implement these functions in different ways and can combine or separate individual stages. As computing power becomes increasingly concentrated within a fixed physical footprint, the feasibility of these different implementations becomes an increasingly important constraint on system design.

### 2.3 The Cooling Wall

Increasing rack power does not simply increase the amount of heat that a cooling system must remove. At sufficiently high power densities, it can also change which cooling architectures are physically and operationally feasible. Every cooling approach has an operating envelope determined by factors such as heat-transfer capability, allowable component temperatures, airflow or coolant-flow requirements, pressure losses, available heat-transfer area, environmental conditions, and the infrastructure required to transport and reject heat. As the thermal load of a computing system increases, an incumbent cooling architecture may approach the limits of this envelope.

This constraint is particularly visible in air-cooled systems. Increasing the power generated by a rack requires a corresponding increase in the rate at which heat must be transported away from the equipment. An air-cooled system can respond by increasing airflow, increasing heat-transfer surface area, changing temperature differentials, or employing more capable fans and heat exchangers. Each of these responses, however, is subject to physical and engineering constraints. Increasing airflow can increase fan power and pressure losses; increasing heat-transfer area requires additional physical space; and increasing temperature differences can be constrained by component operating limits and facility conditions. The resulting challenge is therefore not simply that more cooling is needed, but that the available design space for providing that cooling can become progressively narrower.

Liquid cooling changes this design space by moving heat transport closer to the heat-generating components and by exploiting the substantially greater heat-transfer capacity of liquids relative to air. Direct-to-chip cooling can remove heat from high-power processors through cold plates and circulating coolant, while immersion systems bring the cooling fluid into direct contact with computing components. These approaches do not eliminate thermal constraints, nor are they universally preferable. Rather, they provide alternative mechanisms for transporting heat when the requirements of a computing system increasingly exceed what can be practically achieved with the incumbent architecture.

We use the term **cooling wall** to describe this transition boundary: the context-dependent point at which an incumbent cooling architecture can no longer satisfy the thermal, operational, reliability, or economic requirements of a computing system without a substantial change in cooling design. The cooling wall is not a universal rack-power threshold. Its location depends on the characteristics of the computing equipment, rack configuration, allowable temperatures, environmental conditions, facility infrastructure, reliability requirements, and other design constraints. A rack power level that is challenging for one cooling configuration may be readily accommodated by another.

Rack power density is nevertheless an important driver of the cooling wall. As more power is concentrated within a given physical space, more heat must be transported away from that space, increasing the demands placed on the cooling system. Higher rack density can therefore progressively reduce the feasible operating envelope of an incumbent cooling architecture and increase the pressure to adopt an alternative architecture. The relationship is consequently directional rather than deterministic: increasing power density does not uniquely determine a cooling technology, but it changes the physical requirements that any viable cooling technology must satisfy.

Figure 3 illustrates this concept by positioning major cooling approaches against increasing rack power density. The regions should be interpreted as overlapping operating regimes rather than as universal thresholds. Conventional air cooling, enhanced air cooling, direct-to-chip liquid cooling, and immersion cooling can each be implemented across ranges of system configurations, and the boundaries between them depend on system design and operating conditions. The purpose of the figure is therefore not to identify a single rack-power value at which one technology "ends" and another begins. Instead, it illustrates the narrowing of the feasible design space for an incumbent architecture as thermal density increases and the resulting emergence of alternative cooling approaches.

Crossing a cooling wall can consequently require changes throughout the physical infrastructure supporting computation. Moving from air cooling toward direct liquid cooling, for example, can introduce cold plates, pumps, CDUs, heat exchangers, piping, coolant inventories, and different facility-side temperature requirements. Other transitions can alter the requirements for heat rejection, power distribution, maintenance, monitoring, and equipment servicing. The transition is therefore architectural rather than merely incremental: the infrastructure through which computation is cooled changes as the requirements imposed by the computing system change.

This observation is central to the environmental analysis that follows. A cooling transition does not simply determine how efficiently a fixed amount of heat is removed. It can change the energy required for cooling, the quantity and type of water used, the materials incorporated into cooling equipment, the chemical composition and management of coolants, and the geographic infrastructure required to reject heat. The cooling wall therefore marks a point at which increasing computational density can make previously less visible environmental dimensions of computing infrastructure more consequential. The next section examines these consequences as a problem of environmental burden shifting across energy, water, materials, chemistry, and geography.