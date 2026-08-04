# Graph CSV repair — 2026-08-04

Source file: `chokepoint-map-2026-08-04.csv`  
Backup: `chokepoint-map-2026-08-04.csv.bak-2026-08-04`

- rows before: **526**
- rows after: **480**
- supplier names cleaned: **15**
- rows dropped: **35**

Cause: comma-separated prose was written into `supplier_name` and then split
across rows by the CSV writer, turning descriptive text into fake suppliers.

## Names cleaned (row kept)

| Company | Before | After | Note moved to source |
|---|---|---|---|
| ASML Holding | Carl Zeiss SMT — NON-LISTED | Carl Zeiss SMT | NON-LISTED |
| ASML Holding | Trumpf SE — NON-LISTED | Trumpf SE | NON-LISTED |
| ASML Holding | VDL Groep — NON-LISTED Dutch family-owned | VDL Groep | NON-LISTED Dutch family-owned |
| Cognex Corporation | Nichia — NON-LISTED Japanese leader | Nichia | NON-LISTED Japanese leader |
| Intuitive Surgical | Heidenhain — NON-LISTED German | Heidenhain | NON-LISTED German |
| Intuitive Surgical | Tamagawa Seiki — NON-LISTED Japanese | Tamagawa Seiki | NON-LISTED Japanese |
| Keyence Corporation | Nichia Corporation — NON-LISTED Japanese LED | Nichia Corporation | NON-LISTED Japanese LED |
| Nabtesco Corporation | Kapp Niles — NON-LISTED | Kapp Niles | NON-LISTED |
| Nidec Corporation | Tamagawa Seiki — NON-LISTED Japanese specialist | Tamagawa Seiki | NON-LISTED Japanese specialist |
| Symbotic | SICK AG — NON-LISTED German sensor maker | SICK AG | NON-LISTED German sensor maker |
| Taiwan Semiconductor Manufacturing Co. | Trumpf SE — NON-LISTED | Trumpf SE | NON-LISTED |
| Taiwan Semiconductor Manufacturing Co. | Carl Zeiss SMT — NOT separately listed | Carl Zeiss SMT | NOT separately listed |
| Wuzhou Xinchun (五洲新春) | Marposs — NON-LISTED | Marposs | NON-LISTED |
| Yaskawa Electric | Tamagawa Seiki — NON-LISTED Japanese | Tamagawa Seiki | NON-LISTED Japanese |
| Yaskawa Electric | Heidenhain — NON-LISTED German | Heidenhain | NON-LISTED German |

## Rows dropped (text preserved in the preceding row's source)

| Company | Chokepoint | Dropped text | Disposition |
|---|---|---|---|
| Advantest | Probe cards - device-specific design lock and HBM/leading-edge qualification | several Japanese | merged into previous row |
| Advantest | Test sockets and interface hardware | ISC are low-disclosure specialists | merged into previous row |
| Applied Materials | Precision-machined parts & sub-assemblies | regional machining base | merged into previous row |
| ASML Holding | High-power pulsed CO2 drive laser | family-owned | merged into previous row |
| ASML Holding | Precision mechatronic modules & frames | major ASML module partner | merged into previous row |
| Broadcom | EML / DFB laser chips for optical interconnect | EML epitaxy capacity is concentrated | merged into previous row |
| Broadcom | EML / DFB laser chips for optical interconnect | thinly disclosed | merged into previous row |
| Chongqing Machinery & Electric (重庆机电) | Position in the domestic machine tool consolidation | Two of the four domestic leaders are non-listed | merged into previous row |
| Chongqing Machinery & Electric (重庆机电) | Precision spindles and bearings | domestic makers | merged into previous row |
| Chongqing Machinery & Electric (重庆机电) | Precision spindles and bearings | Domestic capability improving | merged into previous row |
| Cognex Corporation | Lens and optical assemblies | several Japanese optics makers are thinly covered | merged into previous row |
| Harmonic Drive Systems | Cross-roller bearings | Nippon Thompson is comparatively thinly covered | merged into previous row |
| Keyence Corporation | Laser diodes for displacement/profile sensors | laser diode leader | merged into previous row |
| Leaderdrive | Cross-roller bearings | domestic Chinese makers | merged into previous row |
| Marvell Technology | EML / DFB laser + InP epitaxy for optics | EML capacity concentrated | merged into previous row |
| Marvell Technology | EML / DFB laser + InP epitaxy for optics | thinly disclosed | merged into previous row |
| Marvell Technology | SerDes / high-speed IP | in-house | merged into previous row |
| Nabtesco Corporation | Ultra-clean bearing-quality steel melt capacity | thin coverage | merged into previous row |
| Nidec Corporation | Encoders for servo feedback | strong in precision robotics | merged into previous row |
| Nidec Corporation | Encoders for servo feedback | semiconductor equipment | merged into previous row |
| NVIDIA | ABF substrate + ABF film | >95% reported | merged into previous row |
| NVIDIA | ABF substrate + ABF film | not monopoly | merged into previous row |
| Qinchuan Machine Tool (秦川机床) | Precision bearings and spindles | domestic Chinese makers | merged into previous row |
| Qinchuan Machine Tool (秦川机床) | Precision bearings and spindles | indexing shafts | merged into previous row |
| Qinchuan Machine Tool (秦川机床) | Precision bearings and spindles | dressing shafts | merged into previous row |
| Qinchuan Machine Tool (秦川机床) | Precision bearings and spindles | servo tailstocks | merged into previous row |
| Sanhua Intelligent Controls | NdFeB magnets (Dy/Tb grades) | opaque below listed tier | merged into previous row |
| Symbotic | Vision and safety sensors | major in industrial safety | merged into previous row |
| Tesla | High-energy-density lithium cells (>=300 Wh/kg) - next-generation upgrade path | semi-solid | merged into previous row |
| Tesla | High-energy-density lithium cells (>=300 Wh/kg) - next-generation upgrade path | all-solid-state developers | merged into previous row |
| Tesla | Rare-earth separation & refining | is opaque | merged into previous row |
| UBTECH Robotics | AI compute (edge inference) | domestic Chinese SoCs | merged into previous row |
| UBTECH Robotics | High-energy-density lithium cells (>=300 Wh/kg) - next-generation upgrade path | semi-solid | merged into previous row |
| UBTECH Robotics | High-energy-density lithium cells (>=300 Wh/kg) - next-generation upgrade path | all-solid-state developers | merged into previous row |
| Yaskawa Electric | Encoders | in-house | merged into previous row |

## Duplicate relationships merged

Cleaning the annotations collapsed rows like `Carl Zeiss SMT — NON-LISTED`
onto the plain `Carl Zeiss SMT` row that already existed. Citations were
concatenated and the best-sourced evidence grade kept.

| Company | Chokepoint | Supplier |
|---|---|---|
| ASML Holding | EUV optics — Carl Zeiss SMT | Carl Zeiss SMT |
| ASML Holding | Precision mechatronic modules & frames | VDL Groep |
| Cognex Corporation | Illumination LEDs and laser diodes | Nichia |
| Intuitive Surgical | Encoders and position feedback | Heidenhain |
| Intuitive Surgical | Encoders and position feedback | Tamagawa Seiki |
| Nabtesco Corporation | Cycloidal gear machining equipment | Kapp Niles |
| Nidec Corporation | Encoders for servo feedback | Tamagawa Seiki |
| Taiwan Semiconductor Manufacturing Co. | EUV optical columns (mirrors, illuminators, collectors) | Carl Zeiss SMT |
| Wuzhou Xinchun (五洲新春) | Metrology and process capability | Marposs |
| Yaskawa Electric | Encoders | Tamagawa Seiki |
| Yaskawa Electric | Encoders | Heidenhain |

## Left deliberately alone

Category descriptors such as "Chinese magnet makers" and "Chinese SoC vendors"
are intentional stand-ins for non-listed groups and were not modified.
