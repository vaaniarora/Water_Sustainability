# Handoff: Section 2 figures for the cooling-wall paper

Last updated: Oct 19, 2026. Covers the full working session that built the Section 2 figures. More detailed running notes are in [figures_plan.md](figures_plan.md). The paper context is in [paper_outline.md](paper_outline.md) and [section2.md](section2.md).

---

## 1. Goal and framing

**Paper:** *The Environmental Trade-offs of AI Datacenter Cooling* (ACM FAccT 2027).

**Section 2** argues: power is rising at several levels of the computing stack → how datacenters remove heat → the *cooling wall*. The cooling wall is a context-dependent transition region, not a universal kW threshold.

Rules from section2.md that every figure follows:
- **No causal chain.** Processor, server and rack are shown as independent trends: "power is increasing at multiple scales," not "processor power → server power → rack power."
- **Explicit baseline.** Compare AI-oriented systems against general-purpose ones.
- **Native power metrics.** Keep each source's metric (TDP, rated maximum, measured) rather than converting between them.
- **Overlapping regimes.** Cooling technologies are shown as overlapping ranges, not hard cut-offs.

**Data scope (decided):** multiple vendors, roughly 2000–2027, **data-center hardware only** (no consumer CPUs or GPUs). Announced systems are allowed. Points that break the trend are fine.

---

## 2. Final figure set (decided)

| Figure | Content | Status |
|---|---|---|
| **Fig 2a** | Processor power (TDP) vs. release date: server CPUs, data-center GPUs, other AI accelerators | **Paper-ready** (`figures/fig2a_paper.pdf`) |
| **Fig 2c** | Rack/cabinet power vs. year, AI systems vs. HPC systems | **Waiting on the y-axis decision** (§6, item 1) |
| ~~Fig 2b~~ | Server power | **Dropped as a figure.** Covered by text instead (see §5) |
| **Fig 3** | Cooling technologies (rows) vs. rack kW (x-axis); one bar per source's stated range | **Draft**, open decisions in §6 |
| 2.2 schematic | IT loop → facility loop → heat rejection | Not started (hand-drawn, no data) |

Fig 2a and 2c are **separate figures**, each one ACM column wide (3.33 in), so they can be placed side by side or stand alone.

---

## 3. Folder layout and how to run

`Cooling_Wall/` is self-contained. All its data is in `Cooling_Wall/Data/`. The repo-root `Data/` is left in place because `Cooling_Rebound_Effect/` also uses it.

```
Cooling_Wall/
  .gitignore                   # ignores Data/downloaded/mlcommons/raw/ (~440 MB), checkpoints, .DS_Store
  plans/                       # paper_outline.md, section2.md, figures_plan.md, handoff.md (this file)
  Data/
    downloaded/                # external data, unmodified
      ml_hardware.csv (+README: CC-BY citation)      Epoch AI ML hardware, through Mar 2026
      chip_dataset_2026.csv                          CPU/GPU dataset, ends Jan 2024
      power_ssj2008-results-20261014-203943.csv      SPECpower export (latin-1 encoding, headers with trailing tabs)
      data_center_chillers.csv, data_center_cooling_towers.csv (+README)   Epoch; old_scripts only
      mlcommons/systems.csv, power_results.csv       from collect_mlcommons_systems.py
    generated/                 # ours (hand-curated or script output)
      racks.csv                # hand-curated, sourced (see §4)
      processors_extra.csv     # 4 hand-entered 2024 server CPUs (values marked ~)
      cooling_regimes.csv      # 35 rows, 14 sources (research agent; see §4)
      processors_clean.csv     # written by fig2a_processor_power.ipynb
      specpower_clean.csv      # written by fig2b_server_power.ipynb
  scripts/
    paper_style.py             # shared print-size style (fonts, colours, black outline)
    fig2a_processor_power.ipynb      # builds processors_clean.csv + working version of 2a
    fig2c_rack_power.ipynb           # working versions of 2c (main + "reference" with cooling/Uptime/OCP)
    fig2_power_trends.ipynb          # PAPER versions: fig2a_paper + fig2c_paper
    fig3_cooling_regimes.ipynb       # PAPER version of Fig 3
    fig2b_server_power.ipynb         # SPECpower baseline (optional appendix)
    collect_mlcommons_systems.py     # MLPerf system-description collector (already run)
  figures/                     # PDF + PNG outputs
  old_scripts/                 # earlier exploratory notebooks (paths updated to ../Data/downloaded/)
```

**Run order:**
1. `fig2a_processor_power.ipynb`, which builds `processors_clean.csv`
2. `fig2_power_trends.ipynb`
3. `fig3_cooling_regimes.ipynb`

**Tooling notes:**
- **No Jupyter in this environment.** Notebooks were checked by running their code cells with plain Python and the non-interactive matplotlib backend (`MPLBACKEND=Agg`). With the default backend, `plt.show()` opens a window and blocks. They haven't been opened in Jupyter itself.
- **MLCommons collector:** `python3 collect_mlcommons_systems.py [--suites inference --rounds v5.1] [--skip-clone]`. It makes shallow, sparse git clones (system-description JSON files only) and never runs anything from the repos.

---

## 4. Data, sources and conventions

### Conventions in the CSVs
- **Plain number:** taken from existing data, or checked against a source listed in `source_url`.
- **`~number`:** from memory or a weak source; still needs checking. In code, `s.str.lstrip('~')` gives the number and `s.str.startswith('~')` flags it.
- **Blank:** not found.
- **`racks.csv` columns:**
  - `rack_kW_basis`: `spec` (vendor-rated), `derived_top500` (system power ÷ cabinet count), `derived` (server power × servers per rack, or system ÷ racks), `reported` (press or third party), `survey`
  - `confidence`: high, medium or low
  - `status`: shipped or announced
- **Paper figures don't show these distinctions.** Per your instruction, the paper figures show no `~` markers and no notes on how values were derived; that information lives in the CSVs.

### Fig 2a data (processor)
- **Accelerators, 2016 onward:** Epoch AI `ml_hardware.csv`, with consumer and workstation GPUs removed (GeForce, Quadro, RTX A-series, Titan, Radeon RX) and the Huawei Ascend 310 (an edge chip) removed.
- **Data-center GPUs before 2016:** `chip_dataset` (Tesla, FirePro S, Radeon Instinct). Multi-GPU appliances (Tesla S/D) and mobile parts are dropped.
- **Server CPUs to Jan 2024:** `chip_dataset` (Xeon, Opteron, EPYC, Xeon Phi). Desktop and edge Xeons (W, E3, E-, D) are dropped.
- **Server CPUs from 2024:** `processors_extra.csv` (Xeon 6780E/6980P, EPYC 9755/9965, all marked `~`).
- **Counts:** 489 server CPUs, 109 data-center GPUs, 47 other AI accelerators.
- **Type corrections:** Epoch labels some custom AI chips as "GPU". The notebook overrides by name: Trainium, Inferentia, Ascend, Maia, Dojo, Shensuan, TPU, Gaudi and MTIA count as *other AI accelerators*. Biren, Moore Threads, MetaX and Tianshu Zhixin stay GPUs.
- **Epoch GB200 TDP:** listed as 1200 W per GPU. The GB200 superchip (2 GPUs + Grace CPU) is about 2.7 kW.

### Fig 2c data (rack), `racks.csv`
53 rows; 30 have a rack kW value.

**Source check:** four research agents checked every plotted AI/HPC value. Each has a `source_url` and `confidence`.

**Key corrections from the check:**
- **DGX B200:** NVIDIA's reference architecture puts **2 servers per rack, about 29 kW** (not 4 per rack, 57 kW).
- **DGX-1:** 9 per rack in NVIDIA's DGX POD reference design, about 29 kW.
- **Fugaku:** 69 kW, using all 432 racks.
- **GB200 / GB300 NVL72:** 132 and 140 kW, from Vertiv and Gigabyte specs. NVIDIA publishes no per-rack figure.
- **Vera Rubin:** renamed NVL72, shipping in 2026, about 210 kW (midpoint of 190–230 kW).
- **AMD MI355X rack:** 120 kW for 64 GPUs (Supermicro and Gigabyte specs).
- **Huawei CloudMatrix:** compute racks are liquid-cooled.

**Top500 years:** HPC values use Top500 power ÷ cabinet count. Some power values come from a later list than the system's debut year:
- **Summit:** Jun 2019 list (the 2018 debut was 8.8 MW, which gives 34 kW).
- **Aurora:** Jun 2024 list (the 2023 debut was a partial run).

**No credible rack figure** (so not plotted): Google TPU v2–v5p (only chip-power floors available), AWS Trn2/Trn3, Microsoft Maia, Intel Gaudi 3, Cerebras CS-3 (23 kW per system, unknown per rack). **Tianhe-2** has conflicting evidence (about 142 kW vs. an 80 kW cooling unit per cabinet), so it's left unplotted.

**Left out of the paper figure** (`EXCLUDE_RACKS` in `fig2_power_trends.ipynb`):
- low confidence: AMD Helios (~240 kW, press estimate), Huawei CloudMatrix (47 kW, derived from a SemiAnalysis estimate), DGX-2 (40 kW, trade press)
- duplicate: Meta Catalina (a GB200 NVL72 variant)

**After 2026:** Kyber NVL576 (600 kW, 2027, announced) is outside the 2000–2026 x-axis.

**Reference rows** (Uptime survey averages, OCP Open Rack v3, OCP Mt Diablo at 1 MW) appear only in the "reference" figure in `fig2c_rack_power.ipynb`. You decided the Uptime average doesn't help the story.

### Fig 3 data, `cooling_regimes.csv`
35 rows, 14 sources:
- 4 industry bodies (Uptime ×2, ENERGY STAR, ASHRAE)
- 2 research (UC Davis WCEC 2026, Shah & Tuma 2024)
- 7 vendors (Vertiv ×2, Schneider ×2, GRC, Accelsius)
- 2 blogs (SERES, Servnet). These two and the Vertiv white paper came from your pointers.

**Gaps:** ASHRAE TC 9.9 gives no kW ranges. Schneider WP 133 was access-denied (Schneider blogs used instead). JLL was available only second-hand (left out).

**Agreement:** the practical air-cooling limit is about **20–45 kW per rack**. Liquid approaches go from about 20–100 kW up to 200–500 kW.

**Disagreement:** rear-door heat exchangers vary most. Vertiv's 2024 text says passive 5–25 kW and active 50–70 kW, while its own chart shows roughly 15–50 and 30–100 kW.

**Quality caveats:**
- "Vertiv 2024 (chart)" rows were read off a bar chart (approximate).
- Immersion research figures are **per tank**, not per rack.
- GRC (an immersion vendor rating rear doors, a rival technology), Accelsius and some Vertiv values are product claims.

### Other data (collected, not plotted)
- **SPECpower:** 1,138 server-CPU results, 2004–2026.
  - Median power of 2-socket servers at 100% load rose from about 190–290 W (2007–2016) to about 800 W (2024).
  - SPECpower measures full-throughput power on a Java server workload. It doesn't throttle the CPU, but it isn't a maximum-power test either.
  - Use 2-socket servers as the like-for-like baseline (1- and 4/8-socket machines distort the trend).
- **MLCommons** (3,086 system descriptions, 361 power rows):
  - **Measured power:** only 3 data-center systems — Fujitsu 8×H100-NVL (3.0–5.1 kW), Lenovo SR680a 8×B200 air-cooled (7.6–10.4 kW), Lenovo SR780a 8×B200 water-cooled (7.5–9.9 kW). The two Lenovo servers ran no benchmark in common, so **they can't be compared for air vs. water**.
  - **Cooling field:** reliable only from inference v3.1 (2023) onward (at least 93% filled). In v5.1: 156 air, 8 liquid, 8 liquid+air, 13 blank. MLPerf submitters aren't a representative sample of deployed servers.
  - **Not parsed:** older power logs (mostly power-capped "MaxQ" runs), training v0.6 system files (not JSON), 5 Alibaba v0.7 files (trailing commas).

---

## 5. Decisions made (and why)

1. **Data stays at the repo root; Cooling_Wall has its own copy.** `Cooling_Rebound_Effect/` uses the root `Data/`. Its notebooks load bare filenames with no local copies, so they're probably already broken; we didn't touch them.
2. **New scripts go in `scripts/`, old ones in `old_scripts/`, plans in `plans/`.**
3. **Fig 2b dropped.** A research check found no consistent multi-vendor source of AI-server power:
   - DGX user guides are NVIDIA-only (about 9 points).
   - OEMs publish only power-supply capacity.
   - AMD, Google and AWS publish no server figure.
   - LBNL 2024 reuses DGX nameplate values as model inputs.
   - Green500 lacks node counts.
   - Measurement papers cover one system each.

   GPU TDP × count is a steady 50–70% of DGX rated power, so the server level adds little beyond 2a. **Replacement:** one or two sentences, or a small inline table, in Section 2.1 — e.g. DGX A100 6.5 kW (2020), H100 10.2 kW (2022), B200 14.3 kW (2024), B300 ~15 kW (2025), with GPUs about half — citing the DGX user guides and LBNL 2024 (servers assumed to run at about 70% of rated power).
4. **Fig 2c shows AI vs. HPC only:**
   - colour: blue = AI, orange = HPC
   - shape: circle = AI, square = HPC (works in grayscale)
   - hollow = announced
   - no cooling encoding, no Uptime line, no OCP points
5. **Fig 2a legend:** Server CPUs / Data-center GPUs / Other AI accelerators. "CPUs vs GPUs" would be wrong, because about a quarter of the accelerators aren't GPUs.
6. **Paper formatting** (in `paper_style.py`):
   - print size: column 3.33 in, page 7.0 in
   - black outline on all four sides, black axis labels and ticks
   - legend at top centre, above the plot
   - x-axis 2000–2026; 2a y-axis 0–1500 W
   - Arial font (Libertine isn't installed), fonts embedded in the PDF
   - blue = AI, orange = general-purpose/HPC across figures
   - titles and sources go in LaTeX captions, not inside the figures
7. **Fig 3 layout:**
   - one row per technology, one bar per source
   - "up to X" drawn as a short dotted lead-in ending in a cap
   - "X and above" drawn as an arrow
   - single design points as diamonds
   - a grey band for the 20–45 kW air-cooling limit
   - colours grey → light aqua → aqua (air → rear-door → liquid)
   - not overlaid with the 2c racks (your decision)

---

## 6. Open decisions and questions

### Fig 2c (blocking)
1. **Y-axis.** You asked for linear 0–1000 kW with x from 2000 to 2026, but Kyber (the only system above 340 kW) is 2027, so the upper two-thirds is empty and the labels crowd. Options:
   - **(a) 0–400 kW, x to 2026 (recommended).** Rendered as `figures/fig2c_paper_0to400.png`. Mention Kyber's 600 kW in the text.
   - **(b) 0–1000 kW, x to 2027, with Kyber.**
   - **(c) Keep 0–1000 kW, x to 2026.** This is the current `fig2c_paper.png`; the low points stay cramped.
2. **Label fix after choosing:** the Fugaku and Google TPU v7 labels overlap in the 0–400 version, and the DGX group label touches the GB200 marker.

### Fig 3
3. **Uncited blogs:** drop SERES and Servnet, or keep them labelled?
4. **Chart-read values:** drop "Vertiv 2024 (chart)" and keep only text-stated numbers? Vertiv's chart and text disagree on rear-door ranges.
5. **Design:** keep one bar per source (shows disagreement, which is part of the argument; recommended), or switch to one band per technology with sources in an appendix table (cleaner, smaller)?
6. **Height:** it's 3.7 in tall at full width. Merging the three air rows into one would save about a third if page space is tight.
7. **Air-limit band:** confirm 20–45 kW as the band and its wording ("Stated limits of air cooling").

### Data checks still open
8. **`processors_extra.csv`:** the 4 server CPUs (2024) are still `~` and need checking against Intel ARK and AMD spec pages.
9. **Low-confidence values in `racks.csv`** (kept out of the paper figure): Helios (~240), CloudMatrix (47), DGX-2 (40), Tianhe-2 (unplotted).
10. **Medium-confidence values in the paper figure** worth a second look if a reviewer asks:
    - GB200 (132; NVIDIA gives no per-rack figure)
    - GB300 (140; OEM figure)
    - Vera Rubin (210; midpoint of a range)
    - Google TPU v7 (69; a pod average that includes network racks)
    - Tesla Dojo (200; Tesla said "more than 200")
    - El Capitan (340; cabinet count 87 at debut, 90 now)
11. **Rack year convention:** first availability year is used. Summit and Aurora use power values from a later Top500 list than their debut year (see §4).

### Text and paper
12. **Section 2.1 text** for the server level (the DGX sentence or table in §5, item 3). Not written yet.
13. **One finding worth using in Section 2.1 or 2.3:** in 2024, NVIDIA's air-cooled flagship (DGX B200) was deployed at about 29 kW per rack, half the server density of DGX H100. In the same year the liquid-cooled GB200 NVL72 reached about 132 kW. Related: the *design unit moved from server to rack*. Before about 2024, vendors sold servers and operators chose rack density; since GB200 NVL72, the rack itself is the product, designed as a liquid-cooled unit.
14. **Section2.md updates:**
    - 2.1 now has two figures (2a, 2c), not three, plus the server-level text.
    - Fig 3 is described as overlapping regimes, as it already is.
15. **Captions:** draft them with sources and caveats (TDP metrics differ and aren't normalized; HPC = Top500 power ÷ cabinets; Vertiv chart values approximate; immersion figures per tank).
16. **Optional appendix:** the SPECpower figure (`fig2b_server_power_specpower.pdf`).
17. **Font:** install Linux Libertine/Biolinum so the figure text matches ACM body text (a one-line change in `paper_style.py`), or keep Arial?
18. **2.2 schematic** (IT loop → facility loop → heat rejection, open/closed variants) is still to be drawn.

### Housekeeping
19. **Commit the new outputs:** `fig2a_paper.*`, `fig2c_paper*.*`, the updated `fig2_power_trends.ipynb` and `fig3_cooling_regimes.ipynb`, and this file are uncommitted. The working-version figures (`fig2a_processor_power.*`, `fig2c_rack_power*.*`, `fig2_power_trends.*`) could be pruned once the paper versions are final.
20. **Root `plan.md`** (about mostcool) and `mostcool/` are unrelated to this work; they're untracked and were left alone.
21. **MLCommons collector** could be extended to parse older power logs and the trailing-comma JSON files if the cooling record is ever used in the paper. Not needed for current figures.
