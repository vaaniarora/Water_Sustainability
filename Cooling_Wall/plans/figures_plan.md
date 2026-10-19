# Section 2 Figures: Plan

## Figures the paper needs (from section2.md)

| Fig | Content | Claim it supports | Data type |
|---|---|---|---|
| 2a | Processor power (W) vs. release year | Processor power is rising; AI accelerators sit at the top of the distribution | Empirical (spec sheet TDP) |
| 2b | Server power (W) vs. year | Measured server power is rising; accelerator servers have much higher power than general-purpose servers | Empirical (measured, plus vendor-rated) |
| 2c | Rack power (kW) by year or design generation | Rack power is rising, especially in AI infrastructure. Plot as discrete points, not a continuous series | Reported/spec values |
| 2.2 schematic | IT loop → facility loop → heat rejection, open and closed variants | Conceptual | Drawn by hand, no data |
| 3 | Cooling technologies shown as overlapping bands against rack kW | The cooling wall is a transition region | Literature ranges plus anchor racks |

Constraints from section2.md:
- Never imply processor → server → rack causality. These are three independent trends.
- Frame the comparison as AI/high-performance systems vs. earlier or general-purpose systems, with an explicit baseline population.
- Keep each source's power metric (TDP, TGP, rated max, measured) and mark it with the marker style.

## Which racks to focus on

**Updated direction:** cover multiple vendors (NVIDIA, AMD, Google, Intel, AWS, Microsoft, Meta, Tesla, Cerebras, Huawei, HPE/Cray, IBM, Fujitsu) over about 2005–2027. Use data-center hardware only, no consumer CPUs or GPUs. Announced racks are in, drawn as hollow markers. Outliers that break the trend are fine. The working table is `Data/generated/racks.csv`.

`racks.csv` conventions:
- Plain number: taken from data already in the repo. `processor_W_source` names the file (Epoch `ml_hardware.csv` or `chip_dataset_2026.csv`).
- `~number`: from memory or a secondary source; **must be verified**. Parse with `pd.to_numeric(s.str.lstrip('~'))` and `s.str.startswith('~')`.
- Blank: still needs to be found.
- `rack_kW_basis`: `spec` (vendor rated), `derived_top500` (system power / cabinet count), `derived` (server_W × servers_per_rack, or system kW / racks), `survey`.

The NVIDIA-only material below is one storyline within the multi-vendor set.

We can't collect everything, so pick **anchor systems**. For each one we collect the processor, server, and rack values together. The three panels then share labels and colours, so a reader can follow one system across the panels. The synthesis paragraph needs that, but we still show no quantitative mapping between levels.

### Spine: the NVIDIA DGX/HGX → NVL lineage
Why NVIDIA: GB200 accounts for about 10.7M of roughly 14M H100-equivalents in Epoch `gpu_clusters.csv`, and H100 SXM is next at about 1.7M. These are the systems actually being deployed. Within one vendor, the lineage goes from air cooling to required direct-to-chip liquid cooling (DLC).

| Year | Processor (W) | Server | Rack | Cooling | Status |
|---|---|---|---|---|---|
| 2016 | P100 SXM (300) | DGX-1 (~3.2 kW) | ~4 servers/rack | Air | Shipped |
| 2020 | A100 SXM (400) | DGX A100 (6.5 kW) | SuperPOD ref. arch., ~25 kW | Air | Shipped |
| 2022–23 | H100 SXM (700) | DGX H100 (10.2 kW) | SuperPOD ref. arch., ~40 kW; often 2/rack because of facility limits | Air (at the wall) | Shipped |
| 2024 | B200 (1000) | DGX B200 (~14.3 kW) | ~4/rack | Air | Shipped |
| 2024–25 | GB200 (1200) | GB200 compute tray | **GB200 NVL72, ~120–132 kW** | **DLC required** | Shipped |
| 2025 | GB300 (1400) | GB300 compute tray | GB300 NVL72, ~135–140 kW | DLC | Shipped |
| 2026 | Rubin | VR NVL144 tray | Vera Rubin NVL144 (kW TBD) | DLC | Announced |
| 2027 | Rubin Ultra | Kyber tray | Kyber NVL576, ~600 kW | DLC | Announced |

Every number marked `~` must be checked against a primary NVIDIA doc (DGX user guides, SuperPOD reference architectures, GTC keynotes) before use.

### Contrast cases (support "density drives but does not determine")
1. **AMD MI350X (1000 W, air) vs. MI355X (1400 W, liquid), 2025.** The same silicon generation is sold air- or liquid-cooled depending on power. This is the clearest processor-level example of the wall.
2. **Google TPU pods (v3 2018 → v4 → v7 Ironwood 2025).** Google moved to liquid cooling at much lower chip power than NVIDIA did. Cooling is a design choice inside a constrained space. Sources: Google blog posts, the TPU v4 ISCA 2023 paper, and Hot Chips talks.
3. **HPE Cray EX (Frontier 2022, El Capitan 2024).** Fully liquid-cooled HPC cabinets that predate the AI racks. Shows that DLC is not new and comes from HPC.
4. **Immersion example: Microsoft two-phase immersion pilot (2021, fluorinated fluid).** Not a density leader, but it links Fig 3 to the PFAS discussion in Section 3.3.
5. **Baseline: Uptime Institute average rack density.** Below 8 kW in 2024, mostly 10–30 kW in 2025, and reportedly about 11 kW modal in 2026 (verify against Uptime's own release). Plot as a reference line or band on 2c and Fig 3. This is the "general-purpose" baseline that section2.md asks for.

Optional, if we want a forward-looking point: OCP **Mt Diablo / Diablo 400** disaggregated power rack (Meta/Microsoft/Google, up to ~1 MW), from the OCP specs.

## Data sources per level

### 2a Processor
| Source | Coverage | Status |
|---|---|---|
| `Data/downloaded/ml_hardware.csv` (Epoch) | 175 AI accelerators, TDP, **through Mar 2026** (GB300, MI355X, TPU v7, Trainium3, MTIA 300) | Already have. Re-download from epoch.ai/data/machine-learning-hardware for any newer rows |
| `Data/downloaded/chip_dataset_2026.csv` | 4,945 CPUs/GPUs, **ends Jan 2024**, mixes consumer and server parts | Already have. Use as the general-purpose baseline only up to 2024 |
| Manual CSV: 2024–2026 server CPUs | AMD EPYC 9005 Turin (up to 500 W), Intel Xeon 6900P/6700E, NVIDIA Grace, AWS Graviton4, etc. | **To build** (~15–25 rows from AMD/Intel spec pages) |

Plot: general-purpose CPUs as a grey cloud, AI accelerators coloured, anchor chips labelled. Don't extend chip_dataset GPUs past 2024. Epoch covers the accelerators that matter.

### 2b Server
| Source | What it gives | Notes |
|---|---|---|
| **SPECpower_ssj2008** (spec.org/power_ssj2008/results) | Measured wall power at 100% load and idle, HW availability date (month-year), node count, socket count, PSU rating | **Downloaded:** `Data/downloaded/power_ssj2008-results-20261014-203943.csv`, 1,158 results, 2004–2026, latin-1 encoding. 1,138 use server CPUs (Xeon/EPYC/Opteron/Ampere); drop the 19 Core/Pentium results. Divide watts by `Nodes` (204 results are multi-node). Median 2-socket power at 100% load: ~250 W (2008–16) → ~700 W (2024–25). Use 2-socket servers as the main series, since 8-socket machines reach ~4 kW |
| **MLPerf Inference** (MLCommons GitHub `inference_results_v*`) | (a) Measured power for a few systems; (b) system-description JSON for *every* submission | See the MLCommons section below. Use mainly for cooling type and node configuration, not power |
| **Vendor-rated max system power** (DGX user guides; Dell XE9680, HPE, Supermicro HGX spec sheets; AMD MI300X/MI355X platforms) | Spec max | Use a different marker ("rated max"). Fills 2016–2026 for the anchors |

### 2c Rack
| Source | What it gives |
|---|---|
| NVIDIA DGX SuperPOD reference architectures (A100/H100/B200/GB200/GB300) and GTC keynotes | Anchor rack kW |
| AMD, Google, HPE docs | Contrast-case rack kW |
| Uptime Institute annual survey (2017–2026) | Baseline average/modal rack density |
| OCP specs (ORv3, ORv3 HPR, Mt Diablo) | Rack design envelopes |

Store every row with `value_type` (spec / reported / survey) and `status` (shipped / announced). Draw announced racks as hollow markers.

### Fig 3 Cooling regimes
- Band ranges from ASHRAE TC9.9 liquid cooling guidance, Uptime, and vendor white papers (Vertiv, Schneider Electric). Cite each band's source, and show ranges where sources disagree.
- Overlay the anchor racks coloured by their actual cooling type.
- Reuse `old_scripts/flowrate.ipynb` (airflow CFM needed per kW at a given ΔT) as a supporting panel or appendix figure for 2.3 paragraph 2.

### Not used for Section 2 (keep for later sections)
Epoch `data_centers/` (MW, chillers, cooling towers, water MGD) and `gpu_clusters.csv` power belong to facility power. They fit Section 3 (energy/water), or a fourth "facility" panel if we add one.

## File layout
`Cooling_Wall/` is self-contained: all data lives in `Cooling_Wall/Data/`, and scripts use relative paths (`../Data/...` from `scripts/` and `old_scripts/`). The repo-root `Data/` is left alone for `Cooling_Rebound_Effect/`.
```
Cooling_Wall/
  paper_outline.md, section2.md
  .gitignore                   # ignores Data/downloaded/mlcommons/raw/, checkpoints, .DS_Store
  plans/figures_plan.md        # this file
  Data/
    downloaded/                # external data, unmodified
      ml_hardware.csv (+ ml_hardware_README.md: CC-BY citation)
      chip_dataset_2026.csv
      power_ssj2008-results-20261014-203943.csv
      data_center_chillers.csv, data_center_cooling_towers.csv (+ data_centers_README.md)  # old_scripts only
      mlcommons/               # written by collect_mlcommons_systems.py
        raw/                   #   sparse clones (gitignored)
        systems.csv, power_results.csv
    generated/                 # ours: hand-curated or script output
      racks.csv                # hand-curated (~ = verify)
      processors_extra.csv     # hand-curated (~ = verify)
      processors_clean.csv     # written by fig2a notebook
      specpower_clean.csv      # written by fig2b notebook
      servers.csv              # TODO
      cooling_regimes.csv      # TODO
  scripts/
    fig2a_processor_power.ipynb      # done
    fig2c_rack_power.ipynb           # done (draft)
    collect_mlcommons_systems.py     # run Oct 2026 (raw/ is ~440 MB, gitignored)
    fig2b_server_power.ipynb         # SPECpower layer done; AI layers TODO
    fig3_cooling_regimes.ipynb       # TODO
  figures/                     # PDF + PNG outputs
  old_scripts/                 # earlier exploratory notebooks
```

## Order of work
1. ~~Build `racks.csv`~~ (draft done)
2. ~~Fig 2a~~ (done)
3. ~~Fig 2c draft~~ (done). Next: check the `~` values and fill the blank rack_kW rows (TPU v2–v5p, AMD, Intel, AWS, Maia, Cerebras)
4. ~~Download SPECpower~~, ~~SPECpower notebook~~ (`scripts/fig2b_server_power.ipynb`, baseline layer done), ~~MLCommons full run~~ (3,086 systems, 361 power rows). Next: decide how to build `servers.csv` for the AI-server layer
   - MLCommons power: only **3 data-center systems** with measured power (Fujitsu 8×H100-NVL 3.0–5.1 kW; Lenovo SR680a 8×B200 air-cooled 7.6–10.4 kW; Lenovo SR780a 8×B200 water-cooled 7.5–9.9 kW). The two Lenovo servers ran no benchmark in common, so they can't be compared for air vs. water
   - MLCommons `cooling` field is reliably filled only from inference v3.1 (2023) on (≥93%). Earlier rounds and all training rounds are 0–58% filled
   - Not parsed: older-round power logs (v3.1/v4.0, mostly MaxQ), training v0.6 system files (not JSON), 5 Alibaba v0.7 files (trailing commas)
5. Fig 3

## Reading MLCommons results

What I found (checked October 2026):
- `summary_results.json` exists only at the root of `inference_results_v5.0` and `v5.1`. It has one row per result with a `has_power` flag and `Power_Result` / `Power_Units` columns. Data-center power rows: v5.0 has 19, all from one Fujitsu 8×H100-NVL system. v5.1 has 12, all from one Lenovo 8×B200 system, measuring 10.4 kW on llama2-70b Offline.
- Older rounds (v3.1, v4.0) store power as raw logs under `closed/<submitter>/results/<system>/<model>/<scenario>/.../power/` (`server.json`, `ptd_logs.txt`). In v4.0 only about 10 systems have power data. Most are edge or workstation systems. The data-center ones (DGX-H100, Dell XE9680) are **MaxQ** (power-capped) runs, so they understate peak power.
- `closed/<submitter>/systems/*.json` exists for every submission, and those files are the useful part. Fields include `accelerator_model_name`, `accelerators_per_node`, `number_of_nodes`, `host_processor_model_name`, **`cooling`** (e.g. GB300 NVL72: "Mix of Liquid-cooled (CPU, GPU, CX7, NVLink Switches) and Air-cooled"), and `power_supply_quantity_and_rating_watts` (filled in only sometimes).

Recommended approach:
1. **Don't use MLPerf as a power time series.** It is too sparse and biased toward MaxQ runs. Use the handful of measured data-center points as "measured" markers on Fig 2b next to the vendor-rated values.
2. **Mine the system JSONs for all inference and training rounds (v1.0–v5.1).** Sparse-clone only `closed/*/systems/` from each repo, or fetch the files via the GitHub tree API. Build a table with these columns: round, submitter, system, accelerator, accelerators per node, nodes, cooling, and PSU rating. This gives a **multi-vendor record of which servers ship air- vs. liquid-cooled over 2021–2025**, which feeds both 2b and Fig 3.
3. **Use PSU rating × quantity only as an upper bound** on server power, and label it that way.
4. For v5.0 and later, get the power rows from `summary_results.json`. For older rounds, pull power only for the few data-center systems, and parse the average from `ptd_logs.txt` for runs that passed compliance.

## Open decisions
- ~~Include announced systems?~~ Yes, as hollow markers.
- ~~Consumer GPUs in the baseline?~~ No. Data-center hardware only. chip_dataset needs a filter: Xeon, EPYC, Opteron, POWER, plus data-center GPUs, which Epoch already covers.

## Decisions (Oct 19, 2026)

**Fig 2b dropped as a figure.** A research check found no consistent multi-vendor source of AI-server power:
- NVIDIA DGX user guides are the only first-party rated values (about 9 points, 2016–2025).
- OEMs (Dell, Supermicro, Gigabyte, Lenovo) publish only power-supply capacity. AMD, Google and AWS publish no server figure.
- LBNL 2024 (Shehabi et al.) uses the same DGX nameplate values as model inputs, with operating power assumed at 70% of rated and idle at 20%.
- Green500/Top500 lack node counts, and their power figures vary in method.
- Measurement papers (Patel et al., ASPLOS'24) cover one system each.
- GPU TDP × count is a stable 50–70% of DGX rated power, so the DGX points add little beyond Fig 2a.

What we use instead: one or two sentences, or a small inline table, of DGX rated power in Section 2.1, citing the DGX user guides and LBNL 2024. The SPECpower notebook stays as an optional appendix figure.

**Fig 2c main figure = AI vs. HPC only.** No Uptime line, no OCP points, no cooling encoding, no `~` on values. The earlier version is kept as `fig2c_rack_power_reference`. Every plotted AI/HPC value has a `source_url` and a `confidence` rating (high/medium/low) in `racks.csv`.

## Paper figures (Oct 2026)
- `scripts/paper_style.py`: shared print-size style (ACM column 3.33 in, text width 7.0 in; Arial, because Libertine isn't installed; fonts embedded). Blue = AI, orange = general-purpose/HPC.
- **Fig 2** = `scripts/fig2_power_trends.ipynb`: (a) processor and (b) rack side by side, full width. Run `fig2a_processor_power.ipynb` first, since it writes `processors_clean.csv`. Panel (b) leaves out Helios, CloudMatrix, DGX-2 and Catalina (`EXCLUDE_RACKS`).
- **Fig 3** = `scripts/fig3_cooling_regimes.ipynb`, using `Data/generated/cooling_regimes.csv` (35 rows, 13 sources). Forest-plot design: one bar per source per technology row, plus a 20–45 kW band for the stated limits of air cooling. Open decisions:
  - drop the uncited blogs (SERES, Servnet)?
  - drop the chart-read Vertiv 2024 values?
  - switch to the consolidated-band variant?
